from typing import Optional
from fivc.interfaces import (
    abstractmethod,
    IComponent,
)


class IConfigSession(IComponent):
    """
    config session
    """

    @abstractmethod
    def get_value(
            self,
            key_name: str,
    ) -> Optional[str]:
        """
        get value by key
        """


class IConfig(IComponent):
    """
    config
    """

    @abstractmethod
    def get_session(
            self,
            session_name: str,
    ) -> Optional[IConfigSession]:
        """
        get config session by name
        """
