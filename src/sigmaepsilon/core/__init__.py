import os
import appdirs
import warnings
from typing import Optional
import importlib.metadata

from .wrapping import Wrapper
from .typing import ishashable, issequence
from .cp import classproperty
from .infix import InfixOperator
from .attr import attributor

__pkg_name__ = "sigmaepsilon.core"
__version__ = importlib.metadata.version(__pkg_name__)

# catch annoying numpy/vtk future warning:
warnings.simplefilter(action="ignore", category=FutureWarning)

# If available, a local vtk-data instance will be used for examples
SIGMAEPSILON_DATA_PATH: Optional[str] = None
if "SIGMAEPSILON_DATA_PATH" in os.environ:
    SIGMAEPSILON_DATA_PATH = os.environ["SIGMAEPSILON_DATA_PATH"]
    if not os.path.isdir(SIGMAEPSILON_DATA_PATH):
        warnings.warn(
            f"SIGMAEPSILON_DATA_PATH: {SIGMAEPSILON_DATA_PATH} is an invalid path"
        )
    if not os.path.isdir(os.path.join(SIGMAEPSILON_DATA_PATH, "Data")):
        warnings.warn(
            f"SIGMAEPSILON_DATA_PATH: {os.path.join(SIGMAEPSILON_DATA_PATH, 'Data')} does not exist"
        )

# allow user to override the examples path
if "SIGMAEPSILON_USERDATA_PATH" in os.environ:
    USER_DATA_PATH = os.environ["SIGMAEPSILON_USERDATA_PATH"]
    if not os.path.isdir(USER_DATA_PATH):
        raise FileNotFoundError(
            f"Invalid SIGMAEPSILON_USERDATA_PATH at {USER_DATA_PATH}"
        )
else:
    USER_DATA_PATH = appdirs.user_data_dir("SIGMAEPSILON")
    try:
        # Set up data directory
        os.makedirs(USER_DATA_PATH, exist_ok=True)
    except Exception as e:
        warnings.warn(
            f'Unable to create `SIGMAEPSILON_USERDATA_PATH` at "{USER_DATA_PATH}"\n'
            f"Error: {e}\n\n"
            "Override the default path by setting the environmental variable "
            "`SIGMAEPSILON_USERDATA_PATH` to a writable path."
        )
        USER_DATA_PATH = ""

EXAMPLES_PATH = os.path.join(USER_DATA_PATH, "examples")
try:
    os.makedirs(EXAMPLES_PATH, exist_ok=True)
except Exception as e:
    warnings.warn(
        f'Unable to create `EXAMPLES_PATH` at "{EXAMPLES_PATH}"\n'
        f"Error: {e}\n\n"
        "Override the default path by setting the environmental variable "
        "`SIGMAEPSILON_USERDATA_PATH` to a writable path."
    )
    EXAMPLES_PATH = ""


# Set a parameter to control default print format for floats outside
# of the plotter
FLOAT_FORMAT = "{:.3e}"


__all__ = [
    "Wrapper",
    "ishashable",
    "issequence",
    "classproperty",
    "InfixOperator",
    "attributor",
]
