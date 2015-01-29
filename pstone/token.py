#!/usr/bin/env python


from pstone.pstone_exception import PStoneException


class Token(object):

    def __init__(self, line):
        # EOF = self.__init__(-1)
        EOL = '\n'

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
