class Token(object):
    EOF = 0
    NAME = 1
    COMMA = 2
    LBRACK = 3
    RBRACK = 4
    TOKEN_NAMES = ["<EOF>", "NAME", "COMMA", "LBRACK", "RBRACK"]

    def __init__(self, kind, text):
        self.kind = kind
        self.text = text

    def __str__(self):
        return '<"%s", %s>' % (self.text, self.TOKEN_NAMES[self.kind])
