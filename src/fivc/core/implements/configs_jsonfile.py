import json
import os
from typing import Optional

from fivc.core.interfaces import IComponentSite, configs
from fivc.core.interfaces.utils import implements


@implements(configs.IConfigSession)
class ConfigSessionImp:

    def __init__(self, **kwargs):
        self.kwargs = kwargs

    def get_value(self, key_name: str) -> Optional[str]:
        return self.kwargs.get(key_name)


@implements(configs.IConfig)
class ConfigImpl:
    """
    implement config
    """

    def __init__(self, component_site: IComponentSite, **kwargs):
        print('create config component of json file')
        try:
            filename = os.environ.setdefault('CONFIG_JSON', '.env.json')
            with open(filename) as file:
                self.sessions = json.loads(file.read())
        except (FileNotFoundError, ValueError, TypeError):
            self.sessions = {}

    def get_session(self, name: str) -> ConfigSessionImp:
        kwargs = self.sessions.get(name)
        kwargs = kwargs if isinstance(kwargs, dict) else {}
        return ConfigSessionImp(**kwargs)
