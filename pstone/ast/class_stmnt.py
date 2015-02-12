#!/usr/bin/env python

import pstone.ast.ast as ast


class ClassStmt(ast.ASTList):
    def __init__(self, c):
        super(ClassStmt, self).__init__(c)

    def name(self):
        return self.child(0).token().getText()

    def superClass(self):
        if (self.numChildren() < 3):
            return None
        else:
            return self.child(1).token().getText()

    def body(self):
        return self.child(self.numChildren() - 1)

    def __str__(self):
        parent = self.superClass()
        if parent is None:
            parent = "*"
        return "(class + %s %s %s)" % (self.name(), parent, self.body())
