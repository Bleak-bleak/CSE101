# Your name:Xingtong Zhou
#
# Counting Problems (Homework 1-3) starter code
# CSE 101, Fall 2018

import string

# DO NOT DELETE the following helper function!

def sieve(n): # return list of primes from 2-n
    primes = [] # all prime numbers that we find
    # create a list of (n+1) True values
    candidates = [True] * (n+1)

    for value in range(2, n + 1):
        if candidates[value] == True: # value is prime
            # Mark the multiples of value as non-prime
            for i in range(value * 2, n+1, value):
                candidates[i] = False # mark index i as composite
            primes.append(value) # record value as a prime #
    return primes


# Complete the functions that follow for this assignment

def annoyanceFactor(text):
    result=0
    letter = list(string.ascii_lowercase+string.digits)
    start_row=letter.index(text[0])// 7
    for i in text[1:]:
        row = letter.index(i)//7
        current=abs(row-start_row)
        result += current
        start_row=row
        
    

    return result


def primeContainer(n):
    prime=list(sieve(50000))
    for a in prime:
        count=0
        for x in sieve(a):
            if x== a:
                continue
            if str(x) in str(a):
                count += 1
            if count == n:
                 return a


# DO NOT remove the code below! You can use it to test your work.

if __name__ == "__main__":
    print('Computing annoyanceFactor("avalon31"):', annoyanceFactor("avalon31"))
    print()

    print('Computing annoyanceFactor("23fish"):', annoyanceFactor("23fish"))
    print()

    print('Computing annoyanceFactor("waterbed"):', annoyanceFactor("waterbed"))
    print()

    print('Computing annoyanceFactor("ncc1701a"):', annoyanceFactor("ncc1701a"))
    print()

    print('Computing annoyanceFactor("excelsior"):', annoyanceFactor("excelsior"))
    print()

    print('Testing primeContainer(3):', primeContainer(3))
    print()

    print('Testing primeContainer(5):', primeContainer(5))
    print()

    print('Testing primeContainer(6):', primeContainer(6))
    print()

    print('Testing primeContainer(8):', primeContainer(8))
    print()

    print()
    
