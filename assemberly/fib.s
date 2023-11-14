        LDA b
start   ADD a
        sta b
        LDA b
        sub a
        sta a
        BRA start
a       DAT 0
b       DAT 1
