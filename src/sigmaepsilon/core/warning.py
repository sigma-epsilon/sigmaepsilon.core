"""
Warnings used in SigmaEpsilon projects.
"""

__all__ = ["SigmaEpsilonPerformanceWarning"]


class SigmaEpsilonPerformanceWarning(Warning):
    """
    Base class for warnings in SigmaEpsilon projects.
    """
    def __init__(self, message: str):
        pre = "SigmaEpsilon Performance Warning: "
        self.message = pre + message