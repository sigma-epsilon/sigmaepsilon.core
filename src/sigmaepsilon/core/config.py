import toml
import os
from typing import Union, Iterable


def find_pyproject_toml(start_dir: str = None, max_depth: int = 10) -> Union[str, None]:
    """
    Returns the path of the pyproject.toml file of the project.

    Parameters
    ----------
    start_dir: str, Optional
        The dictionary to start with. If not provided, the search starts in the current
        working directory. Default is None.
    max_depth: int, Optional
        The maximum folderwise distance from the starting directory. If provided,
        it must be an integer >= 0. Default is 10.
    """
    if start_dir is None:
        start_dir = os.getcwd()

    if not isinstance(start_dir, str):
        raise TypeError("start_dir must be a string")

    current_dir = start_dir
    depth = 0

    if not isinstance(max_depth, int):
        raise TypeError("max_depth must be an integer")

    if not max_depth >= 0:
        raise ValueError("max_depth must be a positive integer")

    while depth <= max_depth:
        pyproject_path = os.path.join(current_dir, "pyproject.toml")

        if os.path.isfile(pyproject_path):
            return pyproject_path

        parent_dir = os.path.dirname(current_dir)

        current_dir = parent_dir
        depth += 1

    return None


def load_pyproject_config(
    filepath: str = None, section: Union[str, Iterable[str]] = None
) -> Union[dict, Iterable[dict]]:
    """
    Returns the contents of the project configuration file (pyproject.toml)
    or sections of it.

    Parameters
    ----------
    filepath: str, Optional
        The path of the config file. If not specified, an attempt is made to locate it.
        Default is None.
    section: Union[str, Iterable[str]], Optional
        One or more section of the config file. If not specified, the entire content is returned.
        Default is None.
    """
    if not filepath:
        filepath = find_pyproject_toml()

    with open(filepath, "r") as f:
        config_toml = toml.load(f)
        
    has_poetry = "tool" in config_toml and "poetry" in config_toml["tool"]
    if has_poetry and not section:
        config_toml = config_toml['tool']['poetry']
        
    if section:
        if isinstance(section, str):
            config = config_toml.get(section, {})
        else:
            config = [config_toml.get(s, {}) for s in section]
    else:
        config = config_toml
        
    return config


def namespace_package_name(start_dir: str = None, max_depth: int = 10) -> str:
    """
    Returns the name of the SigmaEpsilon namespace package.
    
    Parameters
    ----------
    start_dir: str, Optional
        The dictionary to start with. If not provided, the search starts in the current
        working directory. Default is None.
    max_depth: int, Optional
        The maximum folderwise distance from the starting directory. If provided,
        it must be an integer >= 0. Default is 10.
    """
    if start_dir is None:
        start_dir = os.getcwd()

    if not isinstance(start_dir, str):
        raise TypeError("start_dir must be a string")
    
    current_dir = start_dir
    depth = 0

    if not isinstance(max_depth, int):
        raise TypeError("max_depth must be an integer")

    if not max_depth >= 0:
        raise ValueError("max_depth must be a positive integer")

    while depth <= max_depth:        
        parent_dir_path, current_dir_name = os.path.split(current_dir)
        parent_dir_name = os.path.split(parent_dir_path)[-1]
        
        if os.path.isdir(current_dir) and parent_dir_name=="sigmaepsilon":
            return ".".join([parent_dir_name, current_dir_name])

        parent_dir = os.path.dirname(current_dir)

        current_dir = parent_dir
        depth += 1

    return None
