// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

    @sum
    M=0

    // a = @R0
    @R0
    D=M
    // stop if @R0 == 0
    @RETURN
    D;JEQ
    // place @R0 in @a
    @a
    M=D

    // b = @R1
    @R1
    D=M
    // stop if @R1 == 0
    @RETURN
    D;JEQ
    // place @R1 in @b
    @b
    M=D

    // i = 0
    @i
    M=0

// if i == b goto END
(LOOP)
    @i
    D=M
    @b
    D=D-M
    @RETURN
    D;JEQ  // JEQ -> if D == 0

    @a
    D=M
    @sum
    M=M+D
    @i
    M=M+1
    @LOOP
    0;JMP

(RETURN)
    @sum
    D=M
    @R2
    M=D

(END)
    @END
    0;JMP
