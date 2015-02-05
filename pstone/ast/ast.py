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
    pass
