# -*- coding: utf-8 -*-
import json

__all__ = ["json2dict", "dict2json"]


def json2dict(jsonpath: str) -> dict:
    """
    Reads and returns dictionary from a json file.
    """
    with open(jsonpath, "r") as jsonfile:
        return json.loads(jsonfile.read())


def dict2json(jsonpath: str, d: dict, mode:str="w") -> None:
    """Writes a dictionary to a json file."""
    with open(jsonpath, mode) as outfile:
        json.dump(d, outfile)
