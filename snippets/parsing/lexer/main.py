#!/usr/bin/env python

from token import Token
from lexer import Lexer
from listlexer import ListLexer
from sys import argv

if __name__ == "__main__":
    lexer = ListLexer(argv[1])
    token = lexer.next_token()
    while token.kind is not Token.EOF:
        print(token)
        token = lexer.next_token()
    print(token)  # EOF
