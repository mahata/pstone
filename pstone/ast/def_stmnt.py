#!/usr/bin/env python

import pstone.ast.ast as ast


class DefStmnt(ast.ASTList):
    def __init__(self, c):
        super(DefStmnt, self).__init__(c)

    def name(self):
        return self.child(0).token().getText()

    def parameters(self):
        return self.child(1)

    def body(self):
        return self.child(2)

    def __str__(self):
        return "(def %s %s %s)" % (self.name(), self.parameters(), self.body())
