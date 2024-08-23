import os
from typing import Optional

from fivc.interfaces import IComponentSite
from fivc.interfaces import configs
from fivc.interfaces.utils import implements


@implements(configs.IConfigSession)
class ConfigSessionImpl(object):

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def get_value(self, key_name: str) -> Optional[str]:
        return self.kwargs.get(key_name)


@implements(configs.IConfig)
class ConfigImpl(object):
    """
    implement config
    """

    def __init__(self, component_site: IComponentSite, **kwargs):
        print('create config component of yml file')
        try:
            import yaml
            with open(os.environ.setdefault(
                    'CONFIG_YAML', '.env.yml'), 'r') as f:
                self.sessions = yaml.safe_load(f)
        except (FileNotFoundError, ValueError, TypeError):
            self.sessions = {}

    def get_session(self, name: str) -> ConfigSessionImpl:
        kwargs = self.sessions.get(name)
        kwargs = kwargs if isinstance(kwargs, dict) else {}
        return ConfigSessionImpl(**kwargs)
