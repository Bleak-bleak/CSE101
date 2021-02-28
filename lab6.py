# Xingtong Zhou
# CSE 101
# Lab 6

import string

# IN THIS PART OF THE FILE, IT IS VERY IMPORTANT THAT YOU *ONLY* WRITE CODE
# INSIDE THE FUNCTION DEFINITIONS BELOW! IF YOU WRITE CODE BETWEEN (AND OUTSIDE)
# THE FUNCTION DEFINITIONSS, THE GRADING SYSTEM WILL NOT BE ABLE TO READ YOUR
# CODE AND YOU WILL RECEIVE A GRADE OF ZERO FOR THIS ASSIGNMENT!

def signature(name):
    for i in name:
        if i == "a":
            name = name.replace(i,"b")
        if i == "e":
            name = name.replace(i,"f")
        if i == "i":
            name = name.replace(i,"k")
        if i == "o":
            name = name.replace(i,"p")
        if i == "u":
            name = name.replace(i,"v")
    for i in name:
        if i not in string.ascii_lowercase:
            name="ERROR"
                
    return name


def oddRuns(sequence):
    count = 0
    countP=[]
    result=0
    for i in sequence:
        if i == "0":
            count += 1
        if i == "1":
            countP.append(count)
            count = 0
    countP.append(count)
    for i in range(len(countP)):
        if countP[i]%2==1:
            result += 1
    return result

def lol(level):
    result=""
    if level == 0:
        result = "LOL"
    else:
        result += level * "One more "
        result = result + "LOL "
        result += level * "and I'm out "
            
    return result


def pattern(n):
    result=""
    outcome=""
    x=1
    a="1"
    while x <= n:
        if x == 1:
            result = a
            outcome = result
        else:
            outcome = outcome + str(x)
            outcome = outcome + result
            result = outcome
        x+=1
    outcome=" ".join(outcome)
    return outcome


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE OR REMOVE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    ############### Part 1 Tests ###############
    print('Testing signature("uther"):', signature("uther"))

    print('Testing signature("essaul"):', signature("essaul"))

    print('Testing signature("maerl4n"):', signature("maerl4n"))

    print('Testing signature("asdnsoni"):', signature("asdnsoni"))

    # Write your own tests for Part 1 here!
    print()  # prints a blank line

    ############### Part 2 Tests ###############
    print('Testing oddRuns("0101110000"):', oddRuns("0101110000"))

    print('Testing oddRuns("001001110010000"):', oddRuns("001001110010000"))

    print('Testing oddRuns("10001011011011100011"):', oddRuns("10001011011011100011"))

    print('Testing oddRuns("0001000100010001000100010001"):', oddRuns("0001000100010001000100010001"))
    # Write your own tests for Part 2 here!
    print() # prints a blank line

    ############### Part 3 Tests ###############
    print('Testing lol(0):', lol(0))

    print('Testing lol(2):', lol(2))

    print('Testing lol(5):', lol(5))

    print('Testing lol(4):', lol(4))
    # Write your own tests for Part 3 here!
    print()  # prints a blank line

    ############### Part 4 Tests ###############
    print('pattern(1) prints', pattern(1))

    print('pattern(3) prints', pattern(3))

    print('pattern(5) prints', pattern(5))

    print('pattern(4) prints', pattern(4))
    # Write your own tests for Part 4 here!
    print()  # prints a blank line


