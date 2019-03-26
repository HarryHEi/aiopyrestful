# -*- coding: utf-8 -*-


def _convert_from_bytes(value, type_):
    if issubclass(type_, bytes):
        return value
    else:
        if issubclass(type_, bool):
            return False if value.upper() == b'FALSE' else True
        elif issubclass(type_, str):
            return value.decode('utf-8')
        else:
            return type_(value)


def convert(value, type_):
    """ Convert / Cast function """
    if type(value) is str:
        if issubclass(type_, str):
            return value
        value_bytes = value.encode('utf-8')
        return _convert_from_bytes(value_bytes, type_)
    elif type(value) is bytes:
        return _convert_from_bytes(value, type_)
    else:
        return type_(value)
