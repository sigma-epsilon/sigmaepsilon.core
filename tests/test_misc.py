# -*- coding: utf-8 -*-
import unittest

from sigmaepsilon.core.misc import get_index_suffix


class TestIndexSuffix(unittest.TestCase):

    def test_1st(self):
        self.assertEqual(get_index_suffix(1), 'st')

    def test_2nd(self):
        self.assertEqual(get_index_suffix(2), 'nd')

    def test_3rd(self):
        self.assertEqual(get_index_suffix(3), 'rd')

    def test_4th(self):
        self.assertEqual(get_index_suffix(4), 'th')

    def test_11th(self):
        self.assertEqual(get_index_suffix(11), 'th')

    def test_12th(self):
        self.assertEqual(get_index_suffix(12), 'th')

    def test_13th(self):
        self.assertEqual(get_index_suffix(13), 'th')

    def test_21st(self):
        self.assertEqual(get_index_suffix(21), 'st')

    def test_22nd(self):
        self.assertEqual(get_index_suffix(22), 'nd')

    def test_23rd(self):
        self.assertEqual(get_index_suffix(23), 'rd')

    def test_24th(self):
        self.assertEqual(get_index_suffix(24), 'th')
        

if __name__ == '__main__':
    unittest.main()