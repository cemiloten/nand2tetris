import os
from command import Command


class VMParser:
    def __init__(self, filepath):
        self._commands = []
        self._current_index = 0

        if not os.path.isfile(filepath):
            print '<VMParser>: File "{}": does not exist\n'.format(filepath)
            exit()
        if not filepath.lower().endswith('.vm'):
            print '<VMParser>: File "{}": extension is not ".vm"\n'.format(filepath)
            exit()

        with open(filepath, 'r') as file:
            self._prepare_text(file)

    @property
    def command(self):
        return Command(self._commands[self._current_index])

    def _prepare_text(self, file):
        '''Make a clean list of individual instructions from input text'''
        text = file.read()
        # Create an array of lines
        for line in text.split('\n'):
            # Remove comments
            line = line.split('//')[0]
            # Ignore empty lines
            if line != '':
                self._commands.append(line)

    def has_more_commands(self):
        '''Determine if the index of the current command is valid'''
        return self._current_index < len(self._commands)

    def advance(self):
        '''Increment current command index, called after operations on line'''
        if self.has_more_commands():
            self._current_index += 1
        else:
            print 'Last command reached.'
