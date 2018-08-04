import os
import re
from code import Code


class ASMParser:
    def __init__(self, filepath):
        self.code = Code()
        self._lines = []
        self._current_cmd_index = 0

        if os.path.isfile(filepath) and filepath.endswith('.asm'):
            with open(filepath, 'r') as file:
                self._prepare_text(file)
        else:
            raise IOError('Failed to initialize Parser, file invalid.')

    @property
    def current_command(self):
        return self._lines[self._current_cmd_index]

    def _prepare_text(self, file):
        '''Make a clean list of instructions from input text'''
        text = file.read()
        for line in text.split('\n'):
            # Remove whitespace
            line = line.replace(' ', '')
            # Remove comments
            line = line.split('//')[0]
            # Ignore empty lines
            if line != '':
                self._lines.append(line)

    def has_more_commands(self):
        '''Determine if the index of the current command is valid'''
        return self._current_cmd_index < len(self._lines)

    def advance(self):
        '''Increment current command index, called after operations on line'''
        if self.has_more_commands():
            self._current_cmd_index += 1

    def restart(self):
        self._current_cmd_index = 0

    def is_A_command(self, command):
        return command.startswith('@')

    def is_L_command(self, command):
        return (command.startswith('(') and command.endswith(')'))

    def prepare_labels(self):
        occurences = 0
        while self.has_more_commands():
            cmd = self.current_command
            if self.is_L_command(cmd):
                label = self.current_command[1:-1]
                self.code.add_label(label, self._current_cmd_index - occurences)
                occurences += 1
            self.advance()
        self.restart()

    def translate(self):
        command = self.current_command
        if self.is_A_command(command):
            return self._translate_A_command(command)
        elif self.is_L_command(command):
            return '(LABEL)'
        else:
            return self._translate_C_command(command)

    def _translate_A_command(self, command):
        '''Return binary address from number or from symbol table'''
        # Slice string because we want to ignore the first character '@'
        address = command[1::]
        if address.isdigit():
            result = self.code.dec_to_bin(int(address))
        else:
            result = self.code.get_address_value(address)
        return result

    def _translate_C_command(self, command):
        '''Split command and translate sub components individually'''
        if '=' in command and ';' in command:
            # ex: D=D+M;JLT
            components = re.split('=|;', command)
            dest = self.code.dest(components[0])
            comp = self.code.comp(components[1])
            jump = self.code.jump(components[2])
        elif '=' in command:
            # ex: D=D-M
            components = re.split('=', command)
            dest = self.code.dest(components[0])
            comp = self.code.comp(components[1])
            jump = self.code.jump('null')
        elif ';' in command:
            # ex: D;JGT
            components = re.split(';', command)
            dest = self.code.dest('null')
            comp = self.code.comp(components[0])
            jump = self.code.jump(components[1])
        else:
            raise AttributeError(
                '{} is not a valid C command.'.format(command))

        result = '111{0}{1}{2}'.format(comp, dest, jump)
        return result
