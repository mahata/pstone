#!/usr/bin/env python

import pstone.ast.ast as ast


class BlockStmt(ast.ASTList):
    def __init__(self, c):
        super(BlockStmt, self).__init__(c)
