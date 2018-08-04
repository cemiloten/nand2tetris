class Command:
    class Type:
        PUSH = 'push'
        POP  = 'pop'
        ADD  = 'add'
        SUB  = 'sub'
        NEG  = 'neg'
        EQ   = 'eq'
        GT   = 'gt'
        LT   = 'lt'
        AND  = 'and'
        NOT  = 'not'
        OR   = 'or'

    def __init__(self, text):
        self._text = text
        self._parts = []

        if (self.type == Command.Type.PUSH or self.type == Command.Type.POP):
            self.split_memory_access_command()

    @property
    def text(self):
        return self._text

    @property
    def type(self):
        return self.text.split(' ')[0]

    @property
    def segment(self):
        if (self.type == Command.Type.PUSH or self.type == Command.Type.POP):
            return self._parts[1]
        else:
            return None

    @property
    def index(self):
        if (self.type == Command.Type.PUSH or self.type == Command.Type.POP):
            return self._parts[2]
        else:
            return None

    def split_memory_access_command(self):
        # example: 'push local 2'
        self._parts = self._text.split(' ')

    def __str__(self):
        return self.text
