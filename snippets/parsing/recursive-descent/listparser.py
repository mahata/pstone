from parser import Parser
from listlexer import ListLexer


class ListParser(Parser):
    def __init__(self, input):
        super(ListParser, self).__init__(input)

    def list(self):
        self.match(ListLexer.LBRACK)
        self.elements()
        self.match(ListLexer.RBRACK)

    def elements(self):
        self.element()
        while self.lookahead.kind == ListLexer.COMMA:
            self.match(ListLexer.COMMA)
            self.element()

    def element(self):
        if self.lookahead.kind == ListLexer.NAME:
            self.match(ListLexer.NAME)
        elif self.lookahead.kind == ListLexer.LBRACK:
            self.list()
        else:
            raise Exception("expecting name or list; found %s" % (self.lookahead))
