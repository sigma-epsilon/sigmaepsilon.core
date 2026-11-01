# -*- coding: utf-8 -*-
import importlib
import sys
import unittest
from unittest import mock

import numpy as np

import sigmaepsilon.core.jit as jitmodule


def _sum(a):
    res = 0.0
    for i in jitmodule.prange(len(a)):
        res += a[i]
    return res


def _add(x, y):
    return x + y


class TestJitFallback(unittest.TestCase):
    """Tests the pure Python fallbacks, with Numba hidden."""

    def setUp(self):
        with mock.patch.dict(sys.modules, {"numba": None}):
            self.jit = importlib.reload(jitmodule)

    def tearDown(self):
        importlib.reload(jitmodule)

    def test_availability(self):
        self.assertFalse(self.jit.NUMBA_AVAILABLE)
        self.assertIs(self.jit.prange, range)

    def test_decorator_forms(self):
        for deco in (self.jit.njit, self.jit.jit):
            self.assertIs(deco(_add), _add)
            self.assertIs(deco(_add, cache=True), _add)
            self.assertIs(deco()(_add), _add)
            self.assertIs(deco(nogil=True, parallel=True, cache=True)(_add), _add)
            self.assertIs(deco("f8(f8, f8)", fastmath=True)(_add), _add)
            self.assertIs(deco(["f8(f8, f8)", "i8(i8, i8)"])(_add), _add)

    def test_prange(self):
        f = self.jit.njit(parallel=True)(_sum)
        self.assertEqual(f(np.arange(5.0)), 10.0)

    def test_vectorize(self):
        x, y = np.arange(3.0), np.ones(3)
        expected = np.array([1.0, 2.0, 3.0])
        f = self.jit.vectorize(_add)
        self.assertTrue(np.allclose(f(x, y), expected))
        f = self.jit.vectorize("f8(f8, f8)", target="parallel", cache=True)(_add)
        self.assertTrue(np.allclose(f(x, y), expected))


class TestJitNumba(unittest.TestCase):
    """Tests that the Numba objects are exposed, if Numba is installed."""

    def setUp(self):
        try:
            self.numba = importlib.import_module("numba")
        except ImportError:  # pragma: no cover
            self.skipTest("Numba is not installed")

    def test_numba_objects(self):
        self.assertTrue(jitmodule.NUMBA_AVAILABLE)
        self.assertIs(jitmodule.njit, self.numba.njit)
        self.assertIs(jitmodule.jit, self.numba.jit)
        self.assertIs(jitmodule.prange, self.numba.prange)
        self.assertIs(jitmodule.vectorize, self.numba.vectorize)

    def test_compiled(self):
        f = jitmodule.njit(nogil=True, parallel=True, cache=False)(_sum)
        self.assertEqual(f(np.arange(5.0)), 10.0)
        self.assertTrue(hasattr(f, "py_func"))


if __name__ == "__main__":
    unittest.main()
