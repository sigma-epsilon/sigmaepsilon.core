"""
Warnings used in SigmaEpsilon projects.
"""

__all__ = ["SigmaEpsilonWarning", "SigmaEpsilonPerformanceWarning"]


class SigmaEpsilonWarning(Warning):
    """
    Base class for warnings in SigmaEpsilon projects.
    """
    ...


class SigmaEpsilonPerformanceWarning(SigmaEpsilonWarning):
    """
    Performance warning in SigmaEpsilon projects.
    """
    def __init__(self, message: str):
        pre = "SigmaEpsilon Performance Warning: "
        self.message = pre + message