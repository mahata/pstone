#!/usr/bin/env python

# from token import Token
# from lexer import Lexer
from listlexer import ListLexer
from listparser import ListParser
from sys import argv

if __name__ == "__main__":
    lexer = ListLexer(argv[1])
    # token = lexer.next_token()
    parser = ListParser(lexer)
    parser.list()
