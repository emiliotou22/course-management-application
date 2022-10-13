"""
Pickling process to serialize and de-serialize an object inot different either JSON, XML, or binary format
"""

import json, pickle
from dicttoxml import dicttoxml

def to_json(object: dict()) :
    """
    Converts "object" to JSON and returns it

    Parameters:
        object (dict): a dictionary list 
    """
    return json.dumps(object).encode("utf-8")


def to_xml(object: dict()):
    """
    Converts "object" to XML and returns it
    
    Parameters:
        object (dict): a dictionary list 
    """
    return dicttoxml(object)


def to_bin(object: dict()):
    """
    Converts "object" to binary and returns it
    
    Parameters:
        object (dict): a dictionary list """
    string = json.dumps(object)
    # Return the binary "str" file
    return ' '.join(format(ord(letter), 'b') for letter in string).encode("utf-8")
