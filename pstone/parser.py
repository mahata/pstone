#!/usr/bin/env python

from pstone.token import Token
from pstone.ast.ast import ASTree, ASTList, ASTLeaf

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
        def __init__(self, p):
            self.parsers = p

        def parse(self, lexer, res):
            p = choose(lexer)
            if (p is None):
                raise Exception("Parse Exception")  # ToDo - Dedicated Exception class needed
            else:
                res.add(p.parse(lexer))

        def match(self, lexer):
            return self.choose(lexer) is not None

        def choose(self, lexer):
            for p in self.parsers:
                if p.match(lexer):
                    return p

            return None

        def insert(self, p):
            self.parsers.insert(0, p)

    class Repeat(Element):
        def __init__(self, p, once):
            self.parser = p
            self.onlyOnce = once

        def parse(self, lexer, res):
            while self.parser.match(lexer):
                t = self.parser.parse(lexer)
                if t.__class__.__name__ != "ASTList" or 0 < t.numChildren():
                    res.add(t)
                if self.onlyOnce:
                    break

        def match(self, lexer):
            return self.parser.match(lexer)

    class AToken(Element):  # Abstract
        def __init__(self, t):
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

    def __init__(self, arg):
        if isinstance(arg, ASTree):
            self.reset(arg)
        elif isinstance(arg, Parser):
            self.elements = arg.elements
            self.factory = p.factory
        else:
            raise Exception("Wrong arguments for __init__ of Parser.")

    @staticmethod
    def rule(*args):
        # ToDo - Refactor
        if (len(args) == 0):
            klass = None
        else:
            klass = args[0]
        return Parser(klass)

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

        # ToDo: Fix Me
        self.program = Parser.rule()

    def parse(self, lexer):
        program.parse(lexer)


class Operators(object):
    LEFT = True
    RIGHT = False

    def __init__(self):
        self.operators = {}

    def add(self, name, prec, leftAssoc):
        self.operators[name] = (prec, leftAssoc)
