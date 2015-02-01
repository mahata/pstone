#!/usr/bin/env python

from pstone.token import Token
import re


class Lexer(object):
    def __init__(self):
        # self.hasMore = True
        self.queue = []
        self.lines = open("/etc/resolv.conf").read().split("\n")  # ToDo: Fix Me

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

    def tokenize(self):  # Which is like `readLine()`
        ignore = r"\s*(//.*)"
        string = r'"(.+)"'  # ToDo - Fix Me: it's super naive ('\"' aren't allowed)
        num = r"([0-9]+)"
        identity = r"([a-z_A-Z][a-z_A-Z0-9]*)"
        reserved = r"==|<=|>=|&&|\|\||{|}|<|>|\+|\-|\*|/|="

        reg = re.search("|".join([ignore, string, num, identity, reserved]), source)

        if reg is None:
            return self.queue

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
            self.queue.qppend(reg.group(0))

        source = source[reg.end():]
