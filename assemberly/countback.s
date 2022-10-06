        LDA back
        out
        LDA back
        sub ONE
        STA back
        LDA ONE
        STA COUNT
LOOPTOP LDA COUNT
        ADD ONE
        STA COUNT
        SUB TEN
        BRP ENDLOOP
        LDA back
        sub ONE
        STA back
        OUT
        BRA LOOPTOP
ENDLOOP HLT
ONE     DAT 001
TEN     DAT 010
COUNT   DAT
back    DAT 010
