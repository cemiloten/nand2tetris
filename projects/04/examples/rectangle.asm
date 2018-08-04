// Program: rectangle.asm
// Draw a filled rectangle at the screen's to left corner.
// The rectangle's width is 16 pixels, and its height is RAM[0].
// Usage: put a non-negative number (rectangle's height) in RAM[0].

@R0
D=M
@j
M=D

@R16
D=M
@n
M=D

(COLLOOP)
    // if (j == n) goto END
    @j
    D=M
    @n
    D=D-M
    @END
    D;JEQ

    // RAM[16384+j] = 1
    @SCREEN
    D=A
    @arr  // Store starting address of array
    M=D
    @j    // Get value @j
    A=D+M // Set address to starting address + value @j
    M=1   // Set value

    // increment j
    @j
    M=M+1

    @COLLOOP
    0;JMP

(END)
    @END
    0;JMP
