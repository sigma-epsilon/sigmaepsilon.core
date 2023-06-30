# -*- coding: utf-8 -*-
import unittest

from sigmaepsilon.core import InfixOperator


class TestInfix(unittest.TestCase):

    def test_infix(self):
        x = InfixOperator(lambda x, y: x * y)
        self.assertEqual(2 | x | 4, 8)
        x = InfixOperator(lambda x, y: x + y)
        self.assertEqual(2 << x >> 4, 6)


if __name__ == "__main__":
    
    unittest.main()