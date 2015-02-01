#!/usr/bin/env python

from pstone.lexer import Lexer


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
    tokens = lexer.tokenize()
    # print(tokens)
