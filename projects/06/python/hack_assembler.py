from asm_parser import ASMParser


def main():
    path = r'C:\Users\cemil\OneDrive\nand2tetris\projects\06\add\Add.asm'
    # path = r'C:\Users\cemil\OneDrive\nand2tetris\projects\06\max\Max.asm'
    # path = r'C:\Users\cemil\OneDrive\nand2tetris\projects\06\rect\Rect.asm'
    # path = r'C:\Users\cemil\OneDrive\nand2tetris\projects\06\pong\Pong.asm'
    prs = ASMParser(path)
    out = path.replace('.asm', '.hack')

    with open(out, 'w') as out_file:
        prs.prepare_labels()
        # print prs.code.symbol_table.symbols
        while prs.has_more_commands():
            line = prs.translate()
            if line != '(LABEL)':
                # print line
                out_file.write(line.zfill(16) + '\n')
            prs.advance()


if __name__ == '__main__':
    main()
