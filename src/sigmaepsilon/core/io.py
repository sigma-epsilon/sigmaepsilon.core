# -*- coding: utf-8 -*-
import json

__all__ = ["json2dict", "dict2json"]


def json2dict(jsonpath: str):
    with open(jsonpath, "r") as jsonfile:
        return json.loads(jsonfile.read())


def dict2json(jsonpath: str, d: dict):
    with open(jsonpath, "w") as outfile:
        json.dump(d, outfile)
