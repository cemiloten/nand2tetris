// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
D=M
@EQ_1
D;JEQ
@SP
A=M
M=0
@NEXT.1
0;JMP
(EQ_1)
@SP
A=M
M=-1
(NEXT.1)
@SP
M=M+1

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
D=M
@EQ_2
D;JEQ
@SP
A=M
M=0
@NEXT.2
0;JMP
(EQ_2)
@SP
A=M
M=-1
(NEXT.2)
@SP
M=M+1

// push constant 16
@16
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 17
@17
D=A
@SP
A=M
M=D
@SP
M=M+1

// eq
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
D=M
@EQ_3
D;JEQ
@SP
A=M
M=0
@NEXT.3
0;JMP
(EQ_3)
@SP
A=M
M=-1
(NEXT.3)
@SP
M=M+1

// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
D=M
@LT.1
D;JLT
@SP
A=M
M=0
@NEXT.4
0;JMP
(LT.1)
@SP
A=M
M=-1
(NEXT.4)
@SP
M=M+1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 892
@892
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
D=M
@LT.2
D;JLT
@SP
A=M
M=0
@NEXT.5
0;JMP
(LT.2)
@SP
A=M
M=-1
(NEXT.5)
@SP
M=M+1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 891
@891
D=A
@SP
A=M
M=D
@SP
M=M+1

// lt
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
D=M
@LT.3
D;JLT
@SP
A=M
M=0
@NEXT.6
0;JMP
(LT.3)
@SP
A=M
M=-1
(NEXT.6)
@SP
M=M+1

// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
D=M
@GT.1
D;JGT
@SP
A=M
M=0
@NEXT.7
0;JMP
(GT.1)
@SP
A=M
M=-1
(NEXT.7)
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32767
@32767
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
D=M
@GT.2
D;JGT
@SP
A=M
M=0
@NEXT.8
0;JMP
(GT.2)
@SP
A=M
M=-1
(NEXT.8)
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 32766
@32766
D=A
@SP
A=M
M=D
@SP
M=M+1

// gt
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
D=M
@GT.3
D;JGT
@SP
A=M
M=0
@NEXT.9
0;JMP
(GT.3)
@SP
A=M
M=-1
(NEXT.9)
@SP
M=M+1

// push constant 57
@57
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 31
@31
D=A
@SP
A=M
M=D
@SP
M=M+1

// push constant 53
@53
D=A
@SP
A=M
M=D
@SP
M=M+1

// add
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=D+M
@SP
M=M+1

// push constant 112
@112
D=A
@SP
A=M
M=D
@SP
M=M+1

// sub
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=M-D
@SP
M=M+1

// neg
@SP
M=M-1
@SP
A=M
M=-M
@SP
M=M+1

// and
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=D&M
@SP
M=M+1

// push constant 82
@82
D=A
@SP
A=M
M=D
@SP
M=M+1

// or
@SP
M=M-1
@SP
A=M
D=M
@SP
M=M-1
@SP
A=M
M=D|M
@SP
M=M+1

// not
@SP
M=M-1
@SP
A=M
M=!M
@SP
M=M+1

(ENDPROGRAM)
@ENDPROGRAM
0;JMP
