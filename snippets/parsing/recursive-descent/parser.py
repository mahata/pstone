from abc import ABCMeta, abstractmethod


class Parser(metaclass=ABCMeta):
    def __init__(self, input):
        self.input = input
        self.consume()  # set self.lookahead

    def match(self, x):
        if self.lookahead.kind == x:
            self.consume()
        else:
            raise Exception("exception %s; %s" % (self.input.get_token_name(x), self.lookahead))

    def consume(self):
        self.lookahead = self.input.next_token()
