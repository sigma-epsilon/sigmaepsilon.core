# -*- coding: utf-8 -*-
import unittest

from sigmaepsilon.core.colors import RGB
from sigmaepsilon.core.testing import SigmaEpsilonTestCase


class TestColors(SigmaEpsilonTestCase):
    def test_colors(self):
        RGB(240, 248, 255).hex_format()
       

if __name__ == "__main__":
    unittest.main()