#!/usr/bin/python3
def safe_function(function, *args):
    '''Executes a function safely'''
    import sys
    try:
        result = function(*args)
        return (result)
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return (None)
