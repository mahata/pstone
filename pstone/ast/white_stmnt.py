#!/usr/bin/env python

import pstone.ast.ast as ast


class WhileStmnt(ast.ASTList):
    def __init__(self, c):
        super(WhileStmnt, self).__init__(c)

    def condition(self):
        return self.child(0)

    def body(self):
        return self.body(1)

    def __str__(self):
        return "(while %s %s)" % (self.condition(), self.body())
