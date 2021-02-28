# Xingtong Zhou
# CSE 101
# Lab 4

# IN THIS PART OF THE FILE, IT IS VERY IMPORTANT THAT YOU *ONLY* WRITE CODE
# INSIDE THE FUNCTION DEFINITIONS BELOW! IF YOU WRITE CODE BETWEEN (AND OUTSIDE)
# THE FUNCTION DEFINITIONSS, THE GRADING SYSTEM WILL NOT BE ABLE TO READ YOUR
# CODE AND YOU WILL RECEIVE A GRADE OF ZERO FOR THIS ASSIGNMENT!

def expand(text):
    new_text=""
    i=0
    while len(text) >= (i+1) :
        g= text[i]* int(text[i+1])
        i += 2
        new_text += g
        
    return new_text


def braid(level):
    ori=[1, 1, 1]
    i=0
    while i< (level):
        i += 1
        if i == 0:
            return ori
        if i % 2==0:
            ori[1], ori[2] = ori[2], ori[1]
            ori[1]= ori[2] +ori [1]
        else:
            ori[0], ori[1] = ori[1], ori[0]
            ori[1]= ori[1] + ori[0]
    return ori

def shuffle(deck, rounds):
    new_deck=[]
    half_1=[]
    half_2=[]
    r=0
    while r<rounds:
        half_1=deck[:len(deck)//2]
        half_2=deck[len(deck)//2:]
        r += 1
        i=0
        new_deck=[]
        while i < len(deck)//2:
            new_deck.append(half_1[i])
            new_deck.append(half_2[i])
            i += 1
        deck = new_deck
        
    return new_deck


def backspace(text):
    a=text.find("^H")
    if a == -1:
        return text
    while a != -1:
        result=""
        result += text[:a-1]
        result += text[a+2:]
        text=result
        a= text.find("^H")
        
    return result

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE OR REMOVE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    ############### Part 1 Tests ###############
    print('Testing expand() with the string "d3o5z2y1": \"', expand("d3o5z2y1"), "\"", sep='')

    print('Testing expand() with the string "y2e1Z314p6o1C5": \"', expand("y2e1Z314p6o1C5"), "\"", sep='')

    print('Testing expand() with the string "E2r8A5*9e6F4": \"', expand("E2r8A5*9e6F4"), "\"", sep='')
    print('Testing expand() with the string "a5b4c3d2e1": \"', expand("a5b4c3d2e1"), "\"", sep='')
    print()  # prints a blank line

    ############### Part 2 Tests ###############
    print('Testing braid(0):', braid(0))
    print('Testing braid(2):', braid(2))
    print('Testing braid(5):', braid(5))
    print('Testing braid(8):', braid(8))
    print() # prints a blank line

    ############### Part 3 Tests ###############
    initial_deck = [5, 2, 1, 7, 2, 3]
    rounds = 1
    print('Shuffling', initial_deck, rounds, 'time(s)......')
    d = shuffle(initial_deck, rounds)
    print("Final deck ordering is:", d, "\n")

    initial_deck = [14, 3, 2, -8, 11, 5, 9, 12]
    rounds = 2
    print('Shuffling', initial_deck, rounds, 'time(s)......')
    d = shuffle(initial_deck, rounds)
    print("Final deck ordering is:", d, "\n")

    initial_deck = [14, 3, 2, -8, 11, 5, 9, 12]
    rounds = 3
    print('Shuffling', initial_deck, rounds, 'time(s)......')
    d = shuffle(initial_deck, rounds)
    print("Final deck ordering is:", d, "\n")


    initial_deck = [1, 2, 3, 4, 5, 6]
    rounds = 3
    print('Shuffling', initial_deck, rounds, 'time(s)......')
    d = shuffle(initial_deck, rounds)
    print("Final deck ordering is:", d, "\n")

    print()  # prints a blank line

    ############### Part 4 Tests ###############
    print('Testing backspace("Hello, w^horld!"): \"', backspace("Hello, w^horld!"), "\"", sep='')
    print('Testing backspace("A Horse is a Horse, of k^Hcourse"): \"', backspace("A Horse is a Horse, of k^Hcourse"), "\"", sep='')
    print('Testing backspace("I wish^H^H^Hant some ice cream^H^H^H^H^Hmilk"): \"', backspace("I wish^H^H^Hant some ice cream^H^H^H^H^Hmilk"), "\"", sep='')
    print('Testing backspace("Do whw^Hat you like!"): \"', backspace("Do whw^Hat you like!"), "\"", sep='')
    print()  # prints a blank line


