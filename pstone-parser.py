#!/usr/bin/env python

import pstone.token as token
from pstone.lexer import Lexer
from pstone.parser import BasicParser
from pstone.ast.ast import ASTree

if __name__ == "__main__":
    snippet = """
        foo = "Hello, world"
        // this line should be skipped
        while i < 10 {
            sum = sum + i
            i = i + 1
        }
        sum
    """

    lexer = Lexer(snippet)
    bp = BasicParser()
    while (lexer.peek(0) != token.Token.EOF):
        print("Yo")
        ast = bp.parse(l)
        print("=> ", ast)
