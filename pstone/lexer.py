#!/usr/bin/env python

import pstone.token as token
import re


class Lexer(object):
    def __init__(self, source):
        # self.hasMore = True
        self.queue = []
        self.source = source
        self.lines = source.split("\n")

    def read(self):
        if (0 < len(self.lines)):
            ret = self.lines[0]
            self.lines = self.lines[1:]
            return ret
        else:
            return token.Token(-1)  # EOF

    def peek(self, i):
        if (i < len(self.lines)):
            return self.lines[0:i+1]
        else:
            return token.Token(-1)  # EOF

    def _split2token(self, line):
        ignore = r"\s*(//.*)"
        string = r'"(.+)"'  # ToDo - Fix Me: it's super naive ('\"' aren't allowed)
        num = r"([0-9]+)"
        identity = r"([a-z_A-Z][a-z_A-Z0-9]*)"
        reserved = r"==|<=|>=|&&|\|\||{|}|<|>|\+|\-|\*|/|="

        reg = re.search("|".join([ignore, string, num, identity, reserved]), line)

        if reg is None:
            return True

        if reg.group(1):
            # comment - ignore it!
            pass
        elif reg.group(2):
            strToken = token.StrToken(reg.group(2))
            strToken.setText(reg.group(2))
            self.queue.append(strToken)
        elif reg.group(3):
            numToken = token.NumToken(reg.group(3))
            self.queue.append(numToken)
        elif reg.group(4):
            idToken = token.IdToken(reg.group(4))
            self.queue.append(idToken)
        else:
            self.queue.append(token.Token(reg.group(0)))

        return self._split2token(line[reg.end():])

    def tokenize(self):
        for line in self.lines:
            self._split2token(line)

        return self.queue
