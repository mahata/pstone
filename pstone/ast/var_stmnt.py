#!/usr/bin/env python

import pstone.ast.ast as ast


class VarStmnt(ast.ASTList):
    def __init__(self, c):
        super(VarStmnt, self).__init__(c)

    def name(self):
        return self.child(0).token().getText()

    def type(self):
        return self.child(1)

    def initializer(self):
        return self.child(2)

    def __str__(self):
        return "(var %s %s %s)" % (self.name(), self.type(), self.initializer())
