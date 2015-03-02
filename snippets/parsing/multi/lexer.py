from abc import ABCMeta, abstractmethod


class Lexer(metaclass=ABCMeta):
    EOF = "\0"
    EOF_KIND = 1

    def __init__(self, input):
        """
        input: str
        """
        self.input = input
        self.c = input[0]
        self.i = 0

    # Move to next non-whitespace character
    def consume(self):
        self.advance()
        self._ws()

    # Move one character
    def advance(self):
        self.i += 1
        if len(self.input) <= self.i:
            self.c = self.EOF
        else:
            self.c = self.input[self.i]

    # Ensure x is next character on the input stream
    def match(x):
        if self.c == x:
            self.consume()
        else:
            raise Error("expecting %s; found %s" % (x, self.c))

    @abstractmethod
    def next_token(self):
        raise NotImplementedError("next_token() is not implemented.")

    @abstractmethod
    def get_token_name(self, token_kind):
        raise NotImplementedError("get_token_name() is not implemented.")

    @abstractmethod
    def _ws():
        raise NotImplementedError("ws() is not implemented.")
