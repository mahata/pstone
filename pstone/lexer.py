#!/usr/bin/env python

from pstone.token import Token


class Lexer(object):
    def __init__(self):
        self.hasMore = True
        self.lines = open("/etc/resolv.conf").read().split("\n")  # ToDo: Fix Me

    def read(self):
        if (0 < len(self.line)):
            ret = self.line[0]
            self.line = self.line[1:]
            return ret
        else:
            return Token.EOF
