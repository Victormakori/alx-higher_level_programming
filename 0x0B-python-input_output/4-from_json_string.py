#!/usr/bin/python3

""" defines a function that returns an object """

import json


def from_json_string(my_str):
    """ This function get string from json """
    return json.loads(my_str)
