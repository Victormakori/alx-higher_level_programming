#!/usr/bin/python3

"""
This module is to writes a string to a text file """


def write_file(filename="", text=""):
    """
    This function write content to a file

    Return: content of the file
    """
    with open(filename, 'w', encoding='utf-8') as f:
        content = f.write(text)
        return content
