from abc import ABCMeta, abstractmethod


class Lexer(metaclass=ABCMeta):
    def __init__(self, input):
        """
        input: str
        """
        self.input = input
        self.c = input[0]
        self.p = 0

    def consume(self):
        self.p += 1
        if len(self.input) <= self.p:
            self.c = "\0"  # EOF
        else:
            self.c = self.input[self.p]

    @abstractmethod
    def next_token(self):
        raise NotImplementedError("next_token() is not implemented.")
