from datetime import timedelta
from typing import Optional
from fivc.interfaces import (
    abstractmethod,
    IComponent,
)


class ICache(IComponent):
    """
    cache service
    """

    @abstractmethod
    def get_value(self, key_name: str) -> Optional[bytes]:
        """
        get value by key name
        """

    @abstractmethod
    def set_value(
            self,
            key_name: str,
            value: Optional[bytes],
            expire: timedelta,  # always set expire time
    ) -> bool:
        """
        set value
        """
