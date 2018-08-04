import sys
from vm_parser import VMParser
from code_writer import CodeWriter


def main():
    if len(sys.argv) != 2:
        print('<VMTranslator>: Execute script with '
              'one argument only (The path of an existing "vm" file)\n')
        exit()

    vm_file = sys.argv[1]
    parser = VMParser(vm_file)

    asm_file = vm_file.replace('.vm', '.asm')
    code_writer = CodeWriter(asm_file)

    while parser.has_more_commands():
        code_writer.write_command(parser.command)
        parser.advance()
    code_writer.write_end()

    print '<VMTranslator>: Successfully created "{}"\n'.format(asm_file)


if __name__ == '__main__':
    main()
