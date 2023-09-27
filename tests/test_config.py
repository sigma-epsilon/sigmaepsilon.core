# -*- coding: utf-8 -*-
import unittest, os
from os.path import dirname, abspath

import sigmaepsilon.core as sc
from sigmaepsilon.core.config import (
    find_pyproject_toml,
    load_pyproject_config,
    namespace_package_name,
)
from sigmaepsilon.core.testing import SigmaEpsilonTestCase


class TestConfig(SigmaEpsilonTestCase):
    def test_config(self):
        start_dir = os.getcwd()
        pyproject_toml_path = find_pyproject_toml(start_dir, max_depth=0)
        config = load_pyproject_config(filepath=pyproject_toml_path)
        self.assertTrue(isinstance(config, dict))
        config = load_pyproject_config(filepath=pyproject_toml_path, section="project")
        self.assertTrue(isinstance(config, dict))
        config = load_pyproject_config(
            filepath=pyproject_toml_path, section=["project", "build-system"]
        )
        self.assertTrue(isinstance(config, list))
        self.assertTrue(len(config) == 2)
        self.assertTrue(isinstance(config[0], dict))
        self.assertTrue(isinstance(config[1], dict))
        self.assertFailsProperly(
            TypeError, find_pyproject_toml, start_dir, max_depth="0"
        )
        self.assertFailsProperly(
            ValueError, find_pyproject_toml, start_dir, max_depth=-1
        )
        self.assertFailsProperly(TypeError, find_pyproject_toml, 1, max_depth=-1)
        
        config = load_pyproject_config(filepath=pyproject_toml_path, section="project")
        package_name = namespace_package_name(dirname(abspath(sc.__file__)), 10)
        self.assertEqual(package_name, config["name"])
        
        self.assertFailsProperly(
            TypeError, namespace_package_name, start_dir, max_depth="0"
        )
        self.assertFailsProperly(
            ValueError, namespace_package_name, start_dir, max_depth=-1
        )
        self.assertFailsProperly(TypeError, namespace_package_name, 1, max_depth=-1)
        

if __name__ == "__main__":
    unittest.main()
