from datetime import timedelta
from typing import Optional

from . import IComponent, abstractmethod


class IMutex(IComponent):
    """
    mutex session
    """

    @abstractmethod
    def acquire(
            self,
            expire: timedelta,
            blocking: bool = True,
    ) -> bool:
        """
        acquire mutex
        """

    @abstractmethod
    def release(self) -> bool:
        """
        release mutex
        """


class IMutexSite(IComponent):
    """
    mutex site
    """

    @abstractmethod
    def get_mutex(
            self,
            mtx_name: str
    ) -> Optional[IMutex]:
        """
        get mutex by name
        """
