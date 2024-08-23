from datetime import timedelta
from typing import Optional

from fivc.interfaces import IComponentSite
from fivc.interfaces import caches
from fivc.interfaces.utils import implements


@implements(caches.ICache)
class CacheImpl(object):

    def __init__(
            self,
            component_site: IComponentSite,
            **kwargs,
    ):
        print('create cache of redis')

    def get_value(
            self,
            key_name: str,
    ) -> Optional[bytes]:
        pass

    def set_value(
            self,
            key_name: str,
            value: Optional[bytes],
            expire: timedelta,
    ) -> bool:
        pass
