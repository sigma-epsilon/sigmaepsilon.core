# -*- coding: utf-8 -*-
import unittest, os

from sigmaepsilon.core.config import find_pyproject_toml, load_pyproject_config
from sigmaepsilon.core.testing import SigmaEpsilonTestCase


class TestConfig(SigmaEpsilonTestCase):
    def test_config(self):
        start_dir = os.getcwd()
        pyproject_toml_path = find_pyproject_toml(start_dir, max_depth=0)
        config = load_pyproject_config(filepath=pyproject_toml_path)
        self.assertTrue(isinstance(config, dict))
        config = load_pyproject_config(
            filepath=pyproject_toml_path, section="project"
        )
        self.assertTrue(isinstance(config, dict))
        config = load_pyproject_config(
            filepath=pyproject_toml_path, section=["project", "build-system"]
        )
        self.assertTrue(isinstance(config, list))
        self.assertTrue(len(config)==2)
        self.assertTrue(isinstance(config[0], dict))
        self.assertTrue(isinstance(config[1], dict))
        self.assertFailsProperly(
            TypeError, find_pyproject_toml, start_dir, max_depth="0"
        )
        self.assertFailsProperly(
            ValueError, find_pyproject_toml, start_dir, max_depth=-1
        )
        self.assertFailsProperly(
            TypeError, find_pyproject_toml, 1, max_depth=-1
        )
       

if __name__ == "__main__":
    unittest.main()
