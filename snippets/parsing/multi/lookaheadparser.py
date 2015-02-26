from parser import Parser
from lookaheadlexer import LookaheadLexer


class LookaheadParser(Parser):
    def __init__(self, input, k):
        super(LookaheadParser, self).__init__(input, k)

    # list : "[" elements "]"
    def list(self):
        self.match(LookaheadLexer.LBRACK)
        self.elements()
        self.match(LookaheadLexer.RBRACK)

    # elements : element ("," element)*
    def elements(self):
        self.element()
        while self.LA(1) == LookaheadLexer.COMMA:
            self.match(LookaheadLexer.COMMA)
            self.element()

    # element : NAME "=" NAME | NAME | list
    def element(self):
        if self.LA(1) == LookaheadLexer.NAME and self.LA(2) == LookaheadLexer.EQUALS:
            self.match(LookaheadLexer.NAME)
            self.match(LookaheadLexer.EQUALS)
            self.match(LookaheadLexer.NAME)
        elif self.LA(1) == LookaheadLexer.NAME:
            self.match(LookaheadLexer.NAME)
        elif self.LA(1) == LookaheadLexer.LBrack:
            self.list()
        else:
            raise Exception("expecting name or list; found " + self.LT(1))
