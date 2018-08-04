import os


class CodeWriter:
    segment_to_memory_address = {
        'local'    : 'LCL',
        'argument' : 'ARG',
        'this'     : 'THIS',
        'that'     : 'THAT',
    }
    pointer_index_to_address = {
        '0' : 'THIS',
        '1' : 'THAT'
    }

    def __init__(self, filepath):
        if not filepath.lower().endswith('.asm'):
            print '<CodeWriter>: File "{}": extension is not ".asm"\n'.format(filepath)
            exit()

        # Clear existing file contents
        open(filepath, 'w').close()

        self.filepath = filepath
        self.filename = os.path.basename(filepath).split('.')[0]
        self.counters = {
            'next' : 0,
            'eq'   : 0,
            'lt'   : 0,
            'gt'   : 0
        }

    def write_command(self, command):
        push_pop_funcs = {
            'push' : self.push,
            'pop'  : self.pop,
        }
        arithmetic_funcs = {
            'add'  : self.add,
            'sub'  : self.sub,
            'neg'  : self.neg,
            'gt'   : self.gt,
            'lt'   : self.lt,
            'and'  : self.and_,
            'not'  : self.not_,
            'or'   : self.or_
        }
        if command.type in push_pop_funcs.keys():
            asm_code = push_pop_funcs[command.type](command.segment, command.index)
        elif command.type in arithmetic_funcs.keys():
            asm_code = arithmetic_funcs[command.type]()
        else:
            print '<write_command>: Command "{}" not valid'.format(command.text)
            exit()

        with open(self.filepath, 'a') as file:
            file.write('// ' + command.text + '\n')
            file.write(asm_code + '\n')

    def write_end(self):
        end = ('(ENDPROGRAM)' + '\n'
               '@ENDPROGRAM'  + '\n'
               '0;JMP'        + '\n')
        with open(self.filepath, 'a') as file:
            file.write(end)

    # Main commands
    # ============================================================================
    def push(self, segment, index):
        commands = ''

        if segment == 'temp':
            new_index = str(int(index) + 5)
            commands += ('@' + new_index + '\n' +
                         'D=M' + '\n')

        elif segment == 'static':
            commands += ('@{}.{}'.format(self.filename, index) + '\n' +
                         'D=M' + '\n')

        elif segment == 'pointer':
            address = self.pointer_index_to_address.get(index, None)
            commands += ('@' + address + '\n' +
                         'D=M' + '\n')

        else:
            if segment == 'constant':
                address = None
            else:
                address = self.segment_to_memory_address.get(segment, None)
            commands += self.get_value_at(address, index)

        commands += (self.put_D_to_SP() +
                     self.increment_SP())
        return commands

    def pop(self, segment, index):
        commands = (self.decrement_SP() +
                    self.get_SP_value())

        if segment == 'temp':
            new_index = str(int(index) + 5)
            commands += ('@' + new_index + '\n' +
                         'M=D'           + '\n')

        elif segment == 'static':
            commands += ('@{}.{}'.format(self.filename, index) + '\n' +
                         'M=D' + '\n')

        elif segment == 'pointer':
            address = self.pointer_index_to_address.get(index, None)
            commands += ('@' + address + '\n' +
                         'M=D' + '\n')

        else:
            address = self.segment_to_memory_address.get(segment, None)
            commands += (
                '@stackTopValue' + '\n' +
                'M=D'            + '\n' +
                '@' + index      + '\n' +
                'D=A'            + '\n' +
                '@' + address    + '\n' +
                'A=M'            + '\n' +
                'A=D+A'          + '\n' +
                'D=A'            + '\n' +
                '@addressPtr'    + '\n' +
                'M=D'            + '\n' +
                '@stackTopValue' + '\n' +
                'D=M'            + '\n' +
                '@addressPtr'    + '\n' +
                'A=M'            + '\n' +
                'M=D'            + '\n'
            )
        return commands

    def add(self):
        return (
            self.decrement_SP() +
            self.get_SP_value() +
            self.decrement_SP() +
            self.set_A_to_SP()  +
            'M=D+M' + '\n' +
            self.increment_SP()
        )

    def sub(self):
        return (
            self.decrement_SP() +
            self.get_SP_value() +
            self.decrement_SP() +
            self.set_A_to_SP()  +
            'M=M-D' + '\n' +
            self.increment_SP()
        )

    def neg(self):
        return (
            self.decrement_SP() +
            self.set_A_to_SP()  +
            'M=-M' + '\n'  +
            self.increment_SP()
        )

    def eq(self):
        self.counters['next'] += 1
        self.counters['eq'] += 1
        return (
            self.decrement_SP() +
            self.get_SP_value() +
            self.decrement_SP() +
            self.set_A_to_SP()  +
            (
                'M=M-D'      + '\n'
                'D=M'        + '\n'
                '@EQ.{0}'    + '\n'
                'D;JEQ'      + '\n'
                '@SP'        + '\n'
                'A=M'        + '\n'
                'M=0'        + '\n'
                '@NEXT.{1}'  + '\n'
                '0;JMP'      + '\n'
                '(EQ.{0})'   + '\n'
                '@SP'        + '\n'
                'A=M'        + '\n'
                'M=-1'       + '\n'
                '(NEXT.{1})' + '\n'
            ).format(self.counters['eq'], self.counters['next']) +
            self.increment_SP()
        )

    def gt(self):
        self.counters['next'] += 1
        self.counters['gt'] += 1
        return (
            self.decrement_SP() +
            self.get_SP_value() +
            self.decrement_SP() +
            self.set_A_to_SP()  +
            (
                'M=M-D'      + '\n'
                'D=M'        + '\n'
                '@GT.{0}'    + '\n'
                'D;JGT'      + '\n'
                '@SP'        + '\n'
                'A=M'        + '\n'
                'M=0'        + '\n'
                '@NEXT.{1}'  + '\n'
                '0;JMP'      + '\n'
                '(GT.{0})'   + '\n'
                '@SP'        + '\n'
                'A=M'        + '\n'
                'M=-1'       + '\n'
                '(NEXT.{1})' + '\n'
            ).format(self.counters['gt'], self.counters['next']) +
            self.increment_SP()
        )

    def lt(self):
        self.counters['next'] += 1
        self.counters['lt'] += 1
        return (
            self.decrement_SP() +
            self.get_SP_value() +
            self.decrement_SP() +
            self.set_A_to_SP()  +
            (
                'M=M-D'      + '\n'
                'D=M'        + '\n'
                '@LT.{0}'    + '\n'
                'D;JLT'      + '\n'
                '@SP'        + '\n'
                'A=M'        + '\n'
                'M=0'        + '\n'
                '@NEXT.{1}'  + '\n'
                '0;JMP'      + '\n'
                '(LT.{0})'   + '\n'
                '@SP'        + '\n'
                'A=M'        + '\n'
                'M=-1'       + '\n'
                '(NEXT.{1})' + '\n'
            ).format(self.counters['lt'], self.counters['next']) +
            self.increment_SP()
        )

    def and_(self):
        return (
            self.decrement_SP() +
            self.get_SP_value() +
            self.decrement_SP() +
            self.set_A_to_SP()  +
            'M=D&M' + '\n' +
            self.increment_SP()
        )

    def not_(self):
        return (
            self.decrement_SP() +
            self.set_A_to_SP()  +
            'M=!M' + '\n'  +
            self.increment_SP()
        )

    def or_(self):
        return (
            self.decrement_SP() +
            self.get_SP_value() +
            self.decrement_SP() +
            self.set_A_to_SP()  +
            'M=D|M' + '\n' +
            self.increment_SP()
        )

    # ============================================================================

    # Helper functions
    # ============================================================================
    def decrement_SP(self):
        return (
            '@SP'   + '\n'
            'M=M-1' + '\n'
        )

    def get_address_with_offset(self, segment, index):
        return (
            '@' + index   + '\n'
            'D=A'         + '\n'
            '@' + segment + '\n'
            'A=D+A'       + '\n'
        )

    def get_SP_value(self):
        '''Access stack's top value and store it in D register'''
        return (
            '@SP' + '\n'
            'A=M' + '\n'
            'D=M' + '\n'
        )

    def get_value_at(self, address, index):
        '''Access passed memory segment with index and store its value in D register

        If the command was a constant we don't need to access any memory address
        '''
        commands = (
            '@' + index + '\n'
            'D=A'       + '\n'
        )

        # Address is None if the memory segment was "constant"
        if address is None:
            return commands
        else:
            commands += (
                '@' + address + '\n'
                'A=M'         + '\n'
                'A=D+A'       + '\n'
                'D=M'         + '\n'
            )
            return commands

    def increment_SP(self):
        '''Make the stack pointer point at the next address in memory'''
        return (
            '@SP'   + '\n'
            'M=M+1' + '\n'
        )

    def put_D_to_SP(self):
        '''Access stack's top value and put D register in this address'''
        return (
            '@SP' + '\n'
            'A=M' + '\n'
            'M=D' + '\n'
        )

    def set_A_to_SP(self):
        '''Set current address to the top of the stack pointer'''
        return (
            '@SP' + '\n'
            'A=M' + '\n'
        )
    # ============================================================================
