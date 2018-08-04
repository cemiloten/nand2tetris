(LOOP)
    // if (i == n) goto END
    @i
    D=M
    @n
    D=D-M
    @END
    D;JEQ

    // RAM[arr+i] = -1
    @arr  // Store starting address of array
    D=M
    @i    // Get value @i
    A=D+M // Set address to starting address + value @i
    M=-1  // Set value

    // increment i
    @i
    M=M+1

    @LOOP
    0;JMP

(END)
    @END
    0;JMP
