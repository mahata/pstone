#!/usr/bin/env python

from lookaheadlexer import LookaheadLexer
from lookaheadparser import LookaheadParser
from sys import argv

if __name__ == "__main__":
    # lexer = ListLexer(argv[1])
    lexer = LookaheadLexer(argv[1])
    # parser = ListParser(lexer)
    parser = LookaheadParser(lexer, 2)
    parser.list()
