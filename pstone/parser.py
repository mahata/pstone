#!/usr/bin/env python

from pstone.token import Token


class Parser(object):
    pass


class BasicParser(Parser):
    def __init__(self):
        self.reserved = set()
        self.operators = Operators()

        self.reserved.add(";")
        self.reserved.add("}")
        self.reserved.add(Token.EOL)


class Operators(object):
    LEFT = True
    RIGHT = False

    def __init__(self):
        self.operators = {}

    def add(name, prec, leftAssoc):
        self.operators.append[name] = (prec, leftAssoc)
