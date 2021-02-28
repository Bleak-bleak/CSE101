# Xingtong Zhou
# CSE101
# Assignment #1

# Complete the function that follows for this assignment

import string

def alfg(sequence, rounds):
    list=sequence
    next_number=0
    t=0
    i=0
    while t<rounds:
        next_number=(list[i]+list[i+1])%10
        list.append(next_number)
        i += 1
        t += 1
    return list[-5:]
    
        
    
    return Result # CHANGE OR REPLACE THIS STATEMENT


# DO NOT modify or remove the code below! We will use it for testing.

if __name__ == "__main__":
    # Problem 1: Lagged Fibonacci Digits
    init_sequence = []
    next_value = 10 # we need a multi-digit value other than -1 to force the loop to begin
    while next_value != -1 and next_value > 9:
        next_value = int(input("Enter the next digit in the initial sequence, or -1 to end: "))
        if next_value != -1 and next_value < 10:
            init_sequence.append(next_value)
            next_value = 10 # force the loop to continue after a single digit is entered
    rds = int(input("Enter the number of rounds to perform: "))

    print("Calling alfg() with the starting sequence", init_sequence, "and", rds, "rounds, for a final result of", alfg(init_sequence,rds))
    print()

