from importlib import import_module
from typing import (
    Any,
    Callable,
    List,
    Optional,
    Type,
    TypeVar,
    Union,
)

from . import IComponent, IComponentSite

_Int = TypeVar('_Int')  # interface class
_Imp = TypeVar('_Imp')  # implement class


def cast_component(
        instance: Any,
        instance_type: Type[_Int],
) -> Optional[_Int]:
    return (
        instance if
        isinstance(instance, instance_type) else
        None
    )


def query_component(
        interface_site: IComponentSite,
        interface_type: Type[_Int],
        name: str = '',
) -> Optional[_Int]:
    i = interface_site.query_component(interface_type, name=name)
    return cast_component(i, interface_type) if i else None


def implements(
        interfaces: Union[Type[_Int], List[Type[_Int]]]
) -> Callable[[Type[_Imp]], Type[_Imp]]:
    if issubclass(interfaces, IComponent):
        interfaces = [interfaces]
    else:
        assert isinstance(interfaces, list)
        for i in interfaces:
            assert issubclass(i, IComponent)

    def _wrapper(cls: Type[_Imp]) -> Type[_Imp]:

        class _Wrapper(cls, *interfaces):

            def query_component(
                    self,
                    interface: type,
                    name: str = '',
            ) -> Optional[IComponent]:
                if interface in interfaces:
                    return self
                return None

        return _Wrapper

    return _wrapper


def import_string(dotted_path: str):
    """
    Import a dotted module path and return the attribute/class
    designated by the last name in the path.
    Raise ImportError if the import failed.
    """
    try:
        module_path, class_name = dotted_path.rsplit('.', 1)
    except ValueError:
        msg = '%s doesn\'t look like a module path' % dotted_path
        raise ImportError(msg)

    module = import_module(module_path)

    try:

        return getattr(module, class_name)
    except AttributeError:
        msg = 'Module "%s" does not define a "%s" attribute/class' % (
            module_path, class_name)
        raise ImportError(msg)
