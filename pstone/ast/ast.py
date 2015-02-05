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

    def __init__(self, children):
        self.children = children

    def child(self, i):
        self.children[i]

    def numChildren(self):
        return len(self.children)

    def children(self):
        return self.children

    def location():
        for astobj in self.children:
            loc = asbobj.location()
            if loc is None:
                return loc

        return None

    def __str__(self):
        return "Something S-exp like stuff"  # ToDo - Fix Me


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
