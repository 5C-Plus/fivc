import os
import unittest

from fivc.core.implements.utils import load_component_site
from fivc.core.interfaces import configs
from fivc.core.interfaces.utils import query_component


class TestConfigs(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        os.environ['CONFIG_JSON'] = 'fixtures/test_env.json'
        os.environ['CONFIG_YAML'] = 'fixtures/test_env.yml'

        cls.component_site = load_component_site(
            'fixtures/test_components.yml', fmt='yaml')

    def test_config_json(self):
        config = query_component(
            self.component_site, configs.IConfig, 'Json')
        self.assertIsNotNone(config)
        config_sess = config.get_session('test')
        self.assertIsNotNone(config_sess)
        config_val = config_sess.get_value('key1')
        self.assertEqual(config_val, 'haha')

    def test_config_yaml(self):
        config = query_component(
            self.component_site, configs.IConfig, 'Yaml')
        self.assertIsNotNone(config)
        config_sess = config.get_session('test')
        self.assertIsNotNone(config_sess)
        config_val = config_sess.get_value('key1')
        self.assertEqual(config_val, 'haha')
