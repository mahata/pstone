#!/usr/bin/env python

import pstone.ast.ast as ast


class NullStmnt(ast.ASTList):
    def __init__(self, c):
        super(NullStmnt, self).__init__(c)
