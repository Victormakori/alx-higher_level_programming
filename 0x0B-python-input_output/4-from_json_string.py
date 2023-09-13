#!/usr/bin/python3

""" defines a function that returns an object """

import json


def from_json_string(my_str):

    string_converted = json.loads(my_str)
    return (string_converted)
