import unittest

from fivc.core.implements.utils import load_component_site
from fivc.core.interfaces import caches
from fivc.core.interfaces.utils import query_component


class TestCaches(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.component_site = load_component_site(
            'fixtures/test_components.yml', fmt='yaml')

    def test_cache_redis(self):
        cache = query_component(
            self.component_site, caches.ICache, 'Redis')
        self.assertIsNotNone(cache)
        cache.get_value('test')
