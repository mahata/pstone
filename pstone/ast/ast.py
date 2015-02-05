#!/usr/bin/env python

from abc import ABCMeta


class ASTree(object):
    __metaclass__ = ABCMeta

    def numChildren(self):
        raise Exception("Abstract method has been called.")

    def children(self):
        raise Exception("Abstract method has been called.")

    def location(self):
        raise Exception("Abstract method has been called.")

    def iterator(self):
        raise Exception("Abstract method has been called.")


class ASTList(ASTree):
    pass


class ASTLeaf(ASTree):

    def __init__(self, token):
        self.token = token

    def child(self):
        raise Exception("ToDo: Fix Me - something like IndexOutOfBoundsException")

    def numChildren(self):
        return 0

    def children(self):
        return []  # ToDo: ??

    def location(self):
        return "at line %d" % self.token.getLineNumber()

    def token(self):
        return self.token

    def __str__(self):
        return self.token.getText()
