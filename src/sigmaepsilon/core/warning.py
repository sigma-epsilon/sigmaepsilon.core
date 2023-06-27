"""
Warnings used in DewLoosh projects.
"""

class PerformanceWarning(Warning):
    
    def __init__(self, message: str):
        pre = "SigmaEpsilon Performance Warning: "
        self.message = pre + message