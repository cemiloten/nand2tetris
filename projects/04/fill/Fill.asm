// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed.
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Initialize values
    // initialize screen pointer
    @SCREEN
    D=A
    @screenAddress
    M=D
    // initialize keyboard pointer
    @KBD
    D=A
    @keyAddress
    M=D
    // initialize value @color
    @color
    M=0
    // initialize value @n
    // 8192 = (pixel count / size of a register, (512x256) / 16)
    @8192
    D=A
    @n
    M=D

// Set all screen pixels to @color (0 or -1)
(FILL)
    // if i == n, go back to regular loop, else continue incrementing
    @i
    D=M
    @n
    D=D-M // (i == n can be expressed as i - n == 0)
    @LOOP
    D;JEQ

    // get current color
    @color
    D=M

    // set color @screenAddress
    @screenAddress
    A=M
    M=D

    // increment i
    @i
    M=M+1

    // increment screenAddress
    @screenAddress
    M=M+1

    // next iteration
    @FILL
    0;JMP

// Set color value to white (0000.. or 0)
(WHITE)
    @color
    M=0
    @FILL
    0;JMP

// Set color value to black (1111.. or -1)
(BLACK)
    @color
    M=-1
    @FILL
    0;JMP

// Main loop
(LOOP)
    // reset i
    @i
    M=0
    // set screenAddress to first screen register
    @SCREEN
    D=A
    @screenAddress
    M=D
    // Lookup value at keyboard memory address
    @keyAddress
    A=M
    D=M
    // set color to white if no key pressed
    @WHITE
    D;JEQ
    // set color to black if key pressed
    @BLACK
    0;JMP

// Start program
    @LOOP
    0;JMP
