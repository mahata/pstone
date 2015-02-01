#!/usr/bin/env python

from pstone.pstone_exception import PStoneException


class Token(object):
    EOL = "\n"

    def __init__(self, line):
        self.lineNumber = line

    def getLineNumber(self):
        return self.lineNumber

    def isIdentifier(self):
        return False

    def isNumber(self):
        return False

    def isString(self):
        return False

    def getNumber(self):
        raise PStoneException("not number token")

    def getText(self):
        return ""
