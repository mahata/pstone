#!/usr/bin/env python


class Parser(object):
    pass


class BasicParser(Parser):
    def __init__(self):
        pass


class Operators(object):
    LEFT = True
    RIGHT = False

    def __init__(self):
        self.operators = {}

    def add(name, prec, leftAssoc):
        self.operators.append[name] = (prec, leftAssoc)
