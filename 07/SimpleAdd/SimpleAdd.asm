
// PUSH CONSTANT 7

@7
D=A
@SP
A=M
M=D
@SP
M=M+1

// PUSH CONSTANT 8

@8
D=A
@SP
A=M
M=D
@SP
M=M+1

// ADD

@SP
A=M
A=A-1
D=M
A=A-1
M=D+M
@SP
M=M-1
