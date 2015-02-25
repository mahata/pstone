from parser import Parser
from listlexer import ListLexer


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
        # while self.lookahead.kind == LookaheadLexer.COMMA:
        #     self.match(LookaheadLexer.COMMA)
        #     self.element()

    # element : NAME "=" NAME | NAME | list
    def element(self):
        if self.lookahead.kind == LookaheadLexer.NAME:
            self.match(LookaheadLexer.NAME)
        elif self.lookahead.kind == LookaheadLexer.LBRACK:
            self.list()
        else:
            raise Exception("expecting name or list; found %s" % (self.lookahead))
