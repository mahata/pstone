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

    def LT(self, i):  # Return Token object
        return self.lookahead[(self.p + i - 1) % self.k]

    def LA(self, i):  # Is it needed actually?
        return self.LT(i).type

    def match(self, x):
        if self.LA(1) == x:
            consume()
        else:
            raise Exception("expecting %s; found %s" % (self.input.get_token_name(x), self.LT(1)))
