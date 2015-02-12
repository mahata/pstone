#!/usr/bin/env python

import pstone.ast.ast as ast


class BlockStmnt(ast.ASTList):
    def __init__(self, c):
        super(BlockStmnt, self).__init__(c)
