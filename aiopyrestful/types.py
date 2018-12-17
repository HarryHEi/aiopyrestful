# -*- coding: utf-8 -*-


def convert(value, type_):
    """ Convert / Cast function """
    if issubclass(type_, bytes):
        return value
    else:
        data = value.decode('utf-8')
        if issubclass(type_, bool):
            return False if data.upper() == 'FALSE' else False
        else:
            return type_(data)
