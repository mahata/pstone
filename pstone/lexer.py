#!/usr/bin/env python

from pstone.token import Token
import re


class Lexer(object):
    def __init__(self, source):
        # self.hasMore = True
        self.queue = []
        self.source = source
        self.lines = source.split("\n")

    def read(self):
        if (0 < len(self.line)):
            ret = self.line[0]
            self.line = self.line[1:]
            return ret
        else:
            return Token(-1)  # EOF

    def peek(self):
        pass
        if (0 < len(self.line)):
            return self.line[0]
        else:
            return Token(-1)  # EOF

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
            # print("*ignore*", reg.group(1))
            pass
        elif reg.group(2):
            # print('string', reg.group(2))
            self.queue.append(reg.group(2))
        elif reg.group(3):
            # print('integer', reg.group(3))
            self.queue.append(reg.group(3))
        elif reg.group(4):
            # print('id', reg.group(4))
            self.queue.append(reg.group(4))
        else:
            # print('others', reg.group(0))
            self.queue.append(reg.group(0))

        # line = self.source[line.end():]
        return self._split2token(line[reg.end():])

    def tokenize(self):  # Which is like `readLine()`
        for line in self.lines:
            self._split2token(line)

        return self.queue
