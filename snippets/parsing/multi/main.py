#!/usr/bin/env python

from listlexer import ListLexer
from listparser import ListParser
from sys import argv

if __name__ == "__main__":
    lexer = ListLexer(argv[1])
    # parser = ListParser(lexer)
    parser = LookaheadParser(lexer, 2)
    parser.list()
