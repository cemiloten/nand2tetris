// Computes RAM[1] = 1 + 2 + ... + RAM[0]

//     n = R0
//     i = 1
//     sum = 0
// LOOP:
//     if i > n goto STOP
//     sum = sum + i
//     i = i + 1
//     goto LOOP
// STOP:
//     R1 = sum

    // Put 0 in D
    @R0
    D=M
    // Set value @n to D
    @n
    M=D
    // Set value @i to 1
    @i
    M=1
    // Set value @sum to 0
    @sum
    M=0

// goto STOP if i > n
(LOOP)
    // Store value @i
    @i
    D=M
    // Store i - n
    @n
    D=D-M
    // if i - n > 0 then it means that i > n,
    // in which case we now that it is time to stop
    @STOP
    D;JGT  // JGT means if value > 0

    // Store in D the value @sum
    @sum
    D=M
    // Add value @i to stored value
    @i
    D=D+M
    // Put stored value @sum
    @sum
    M=D
    // Increment value @i
    @i
    M=M+1
    // Check if next iteration or stop
    @LOOP
    0;JMP

// Go here when done
(STOP)
    // Store value @sum
    @sum
    D=M
    // Put D in R1
    @R1
    M=D

// Infinite loop for ending
(END)
    @END
    0;JMP
