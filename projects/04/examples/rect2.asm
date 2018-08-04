// Program: rectangle.asm
// Draw a filled rectangle at the screen's to left corner.
// The rectangle's width is 16 pixels, and its height is RAM[0].
// Usage: put a non-negative number (rectangle's height) in RAM[0].

    // Put number of iterations @n
    @R0
    D=M
    @n
    M=D
    // Initialize @i to 0
    @i
    M=0

    // RAM[16384+j] = 1
    @SCREEN
    D=A
    @addr  // Store starting address of SCREEN
    M=D

(LOOP)
    // if i > n goto END, also expressed as if (i - n > 0)
    @i
    D=M
    @n
    D=D-M
    @END
    D;JGT

    // Set pixel value
    @addr
    A=M
    M=-1

    @i
    M=M+1  // increment i
    @32
    D=A
    @addr
    M=M+D // addr = addr + 32
    @LOOP
    0;JMP

(END)
    @END
    0;JMP
