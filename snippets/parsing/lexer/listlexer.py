from lexer import Lexer
from token import Token


class ListLexer(Lexer):
    def __init__(self, input):
        super(ListLexer, self).__init__(input)

    def next_token(self):
        while self.c != "\0":
            if self.c == " " or self.c == "\t" or self.c == "\n" or self.c == "\r":
                self._ws()
                continue
            elif self.c == ",":
                self.consume()
                return Token(Token.COMMA, ",")
            elif self.c == "[":
                self.consume()
                return Token(Token.LBRACK, "[")
            elif self.c == "]":
                self.consume()
                return Token(Token.RBRACK, "]")
            else:
                if self.c.isalpha():
                    return self._name()
                raise Exception("invalid character: %s" % (self.c))

        return Token(Token.EOF, "<EOF>")

    def _name(self):
        buf = []
        while True:
            buf.append(self.c)
            self.consume()
            if not self.c.isalpha():
                break

        return Token(Token.NAME, "".join(buf))

    def _ws(self):
        while self.c == " " or self.c == "\t" or self.c == "\n" or self.c == "\r":
            self.consume()
