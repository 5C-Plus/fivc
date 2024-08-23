from typing import (
    Dict,
    Optional,
    TextIO,
    Union,
)

from fivc.interfaces import (
    IComponent,
    IComponentSite,
    IComponentSiteBuilder,
)
from fivc.interfaces.utils import (
    import_string,
)


class ComponentSite(IComponentSite):
    """
    default implementation of IComponentSite
    """

    def __init__(self):
        self.service_mapping: Dict[type, Dict[str, IComponent]] = {}

    def get_component(
            self,
            interface: type,
            name: str = '',
    ) -> IComponent:
        component = self.query_component(interface, name=name)
        if not component:
            raise LookupError('component not found')
        return component

    def query_component(
            self,
            interface: type,
            name: str = '',
    ) -> Optional['IComponent']:
        component = self.service_mapping.get(interface)
        return component and component.get(name)

    def register_component(
            self,
            interface: type,
            implement: IComponent,
            name: str = '',
    ) -> IComponent:
        if not issubclass(implement.__class__, interface):
            raise ValueError(
                'incorrect implementation for component interface')

        mapping = self.service_mapping.setdefault(interface, {})
        mapping.update({name: implement})
        return implement


class ComponentSiteBuilder(IComponentSiteBuilder):
    """
    default implementation of ServiceBuilder
    """

    @staticmethod
    def _loads(
            component_site: IComponentSite,
            configs: Union[tuple, list]
    ):
        if not isinstance(configs, (tuple, list)):
            raise ValueError('invalid component configuration file')

        for config_item in configs:
            service_class_name = config_item.pop('class', '')
            service_entries_name = config_item.pop('entries', [])
            if not isinstance(service_entries_name, (tuple, list)):
                raise ValueError(
                    'invalid component entries in configuration file')
            try:
                service_class = import_string(service_class_name)
            except ImportError:
                raise ValueError(
                    'invalid component class {}'.format(service_class_name))

            service_instance = service_class(component_site, **config_item)
            for e in service_entries_name:
                if not isinstance(e, dict):
                    raise ValueError(
                        'invalid component entry in configuration file')

                service_name = e.get('name', '')
                service_interface_name = e.get('interface', '')
                try:
                    service_interface = import_string(service_interface_name)
                except ImportError:
                    raise ValueError('invalid component interface {}'.format(
                        service_interface_name))

                component_site.register_component(
                    service_interface, service_instance, name=service_name)

    def _parse(self, configs: TextIO, fmt: str = 'json'):
        if fmt == 'json':
            import json
            return json.loads(configs.read())

        if fmt in ['yaml', 'yml']:
            import yaml
            return yaml.safe_load(configs.read())

        raise NotImplementedError(f'Unknown file format {fmt}')

    def loads(
            self,
            component_site: IComponentSite,
            configs: TextIO,
            fmt: str = 'json',
    ):
        self._loads(component_site, self._parse(configs, fmt))

    def dumps(
            self,
            component_site: IComponentSite,
            configs: TextIO,
            fmt: str = 'json',
    ):
        raise NotImplementedError()
