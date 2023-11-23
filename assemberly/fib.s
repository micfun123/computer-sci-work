# little man computer finarch

# LMC code for Fibonacci sequence generator

INP
STA FIRST    # Store the first input number at memory address FIRST

LDA FIRST    # Load the first input number into the accumulator
OUT          # Output the first number

LDA #0       # Load 0 into the accumulator
STA PREVIOUS # Store 0 as the previous number in the sequence

LDA #1       # Load 1 into the accumulator
STA CURRENT  # Store 1 as the current number in the sequence
OUT          # Output the second number

LOOP, LDA PREVIOUS   # Load the previous number
ADD CURRENT          # Add it to the current number
OUT                  # Output the result (next number in the sequence)
STA TEMP            # Store the result temporarily

LDA CURRENT         # Load the current number
STA PREVIOUS        # Set the current number as the previous number

LDA TEMP            # Load the temporary result
STA CURRENT         # Set the temporary result as the current number

BR LOOP             # Repeat the loop
