from symbol_table import SymbolTable


class Code:
    def __init__(self):
        self.symbol_table = SymbolTable()
        self.next_register_addr = 16

    def dec_to_bin(self, num):
        if num == 0:
            return ''
        else:
            return self.dec_to_bin(num / 2) + str(num % 2)

    def get_address_value(self, address):
        if address not in self.symbol_table.symbols:
            self.symbol_table.symbols[address] = self.next_register_addr
            self.next_register_addr += 1
        return self.dec_to_bin(self.symbol_table.symbols[address])

    def add_label(self, label, number):
        if label not in self.symbol_table.symbols:
            self.symbol_table.symbols[label] = number

    def dest(self, string):
        return self.symbol_table.dest[string]

    def comp(self, word):
        op_code = '0'
        if 'M' in word:
            word = word.replace('M', 'A')
            op_code = '1'
        return op_code + self.symbol_table.comp[word]

    def jump(self, string):
        return self.symbol_table.jump[string]
