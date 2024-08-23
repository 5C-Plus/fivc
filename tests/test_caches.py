import unittest

from fivc.interfaces import caches
from fivc.interfaces.utils import query_component
from fivc.implements.utils import load_component_site


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
