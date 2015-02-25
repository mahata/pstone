from abc import ABCMeta, abstractmethod


class Parser(metaclass=ABCMeta):
    def __init__(self, input, k):
        self.input = input  # input should be a Lexer object
        self.k = k  # number of lookahead symbols
        self.p = 0  # circular index of next token position to fill

        self.lookahead = [None] * k
        for i in range(k):
            self.consume()

    def consume(self):
        self.lookahead[self.p] = self.input.next_token()
        self.p = (p + 1) % self.k

    def match(self, x):
        if self.lookahead.kind == x:
            self.consume()
        else:
            raise Exception("exception %s; %s" % (self.input.get_token_name(x), self.lookahead))
