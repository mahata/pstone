#!/usr/bin/env python

import pstone.token as token
from pstone.lexer import Lexer
from pstone.parser import BasicParser
from pstone.ast.ast import ASTree

if __name__ == "__main__":
    # snippet = """
    #     foo = "Hello, world"
    #     // this line should be skipped
    #     while i < 10 {
    #         sum = sum + i
    #         i = i + 1
    #     }
    #     sum
    # """

    # Parser paren = rule().sep("(").ast(expr).sep(")");

    snippet = """
    3 + 5
    """

    lexer = Lexer(snippet)
    bp = BasicParser()
    while (not lexer.peek(0).isEOF()):
        ast = bp.parse(lexer)
        # print("=> ", ast)
        break
