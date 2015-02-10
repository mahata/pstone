#!/usr/bin/env python

from pstone.token import Token


class Parser(object):
    class Element(object):  # Abstract
        def parse(self, lexer, res):
            raise Exception("Abstract method has been called.")

        def match(self, lexer):
            raise Exception("Abstract method has been called.")

    class Tree(Element):
        def __init__(self, p):
            self.parser = p

        def parse(self, lexer, res):
            res.add(self.parser(lexer))

        def match(self, lexer):
            self.parser.match(lexer)

    class OrTree(Element):
        pass

    class Repeat(Element):
        pass

    class AToken(Element):  # Abstract
        pass

    class IdToken(AToken):
        pass

    class NumToken(AToken):
        pass

    class StrToken(AToken):
        pass

    class Leaf(Element):
        pass

    class Skip(Leaf):
        pass

    class Precedence(object):
        pass

    class Expr(Element):
        pass

    class Factory(object):  # Abstract
        pass

    def __init__(self):
        pass

    def rule(self):
        pass

    def match(self):
        pass

    def reset(self):
        pass

    def number(self):
        pass

    def identifier(self):
        pass

    def string(self):
        pass

    def token(self):
        pass

    def sep(self):
        pass

    def ast(self):
        pass

    def otherwise(self):  # Originally, it's "or" function
        pass

    def maybe(self):
        pass

    def option(self):
        pass

    def repeat(self):
        pass

    def expression(self):
        pass

    def insertChoice(self):
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

        # self.expr0 = rule()
        parser = Parser()

    def parse(self, lexer):
        program.parse(lexer)


class Operators(object):
    LEFT = True
    RIGHT = False

    def __init__(self):
        self.operators = {}

    def add(self, name, prec, leftAssoc):
        self.operators[name] = (prec, leftAssoc)
