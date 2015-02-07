#!/usr/bin/env python

from pstone.token import Token


class Parser(object):
    pass


class BasicParser(object):
    def __init__(self):
        self.reserved = set()
        self.operators = Operators()

        self.reserved.add(";")
        self.reserved.add("}")
        self.reserved.add(Token.EOL)

        self.operators.add("=", 1, Operators.RIGHT)
        self.operators.add("==", 2, Operators.LEFT)
        self.operators.add(">", 2, Operators.LEFT)
        self.operators.add("<", 2, Operators.LEFT)
        self.operators.add("+", 3, Operators.LEFT)
        self.operators.add("-", 3, Operators.LEFT)
        self.operators.add("*", 4, Operators.LEFT)
        self.operators.add("/", 4, Operators.LEFT)
        self.operators.add("%", 4, Operators.LEFT)


class Operators(object):
    LEFT = True
    RIGHT = False

    def __init__(self):
        self.operators = {}

    def add(self, name, prec, leftAssoc):
        self.operators[name] = (prec, leftAssoc)
