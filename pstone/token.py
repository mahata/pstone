#!/usr/bin/env python

from pstone.pstone_exception import PStoneException
import sys


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

    def isEOF(self):
        return self.lineNumber == -1


class NumToken(Token):
    def isNumber(self):
        return True


class StrToken(Token):
    def isString(self):
        return True

    def setText(self, literal):
        self.literal = literal

    def getText(self):
        return self.literal

    def __str__(self):
        try:
            return self.literal
        except NameError:
            sys.stderr.write("String literal must be set to StrToken object!\n")
            return ""


class IdToken(Token):
    def isIdentifier(self):
        return True
