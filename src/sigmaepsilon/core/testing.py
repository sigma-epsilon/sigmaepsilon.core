"""
This module contains reusable stuff for unittesting.
"""
import unittest
from typing import Callable


__all__ = ["SigmaEpsilonTestCase"]


class SigmaEpsilonTestCase(unittest.TestCase):
    """
    A base class for test cases in SigmaEpsilon projects.
    """
    def assertFailsProperly(self, exc:Exception, fnc:Callable, *args, **kwargs):
        """
        Checks if a certain call fails the way it is expected to.
        """
        failed_properly = False
        try:
            fnc(*args, **kwargs)
        except exc:
            failed_properly = True
        finally:
            self.assertTrue(failed_properly)