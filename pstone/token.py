#!/usr/bin/env python


class Token(object):
    EOF = self.__init__(-1)
    EOL = '\n'

    def __init__(self, line):
        self.lineNumber = line

    def getLineNumber():
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
