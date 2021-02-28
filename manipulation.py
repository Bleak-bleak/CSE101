# Your name:Xingtong Zhou
#
# CSE 101, Fall 2018
# Assignment 3-3 (Sequence Manipulation) starter code

# Complete the functions below for this assignment

def enhancedSplit(source, delimiters, includeDelimiters):
    result=[]
    current1=""
    current2=""
    for i in source:
        if i in delimiters:
            if len(current1)>0:
                result.append(current1)
            current1=""
            current2= current2 + i
        else:
            if includeDelimiters is True and len(current2)>0:
                result.append(current2)
            current2=""
            current1= current1 + i
    if len(current1) >0:
        result.append(current1)
        
                
    return result

def flatten(myList):
    if len(myList) == 0:
        return []
    else:
        if isinstance(myList[0],list) is True:
            return flatten(myList[0]) + flatten(myList[1:])
        else:
            return [myList[0]] + flatten(myList[1:])
 
    


# DO NOT modify or remove the code below! We will use it for testing.

if __name__ == "__main__":
    # Test of Part 1
    print('Testing enhancedSplit("repetition", [], False):', enhancedSplit("repetition", [], False)) # no delims
    print()

    print('Testing enhancedSplit("repetition", ["e"], False):', enhancedSplit("repetition", ["e"], False)) # 1 delim, present
    print()

    print('Testing enhancedSplit("i am the very model of a modern major-general", ["p"], False):', enhancedSplit("i am the very model of a modern major-general", ["p"], False)) # 1 delim, not present
    print()

    print('Testing enhancedSplit("why is the sun yellow and not blue", ["m", "x", "z"], False):', enhancedSplit("why is the sun yellow and not blue", ["m", "x", "z"], False)) # multiple delims, none present
    print()

    print('Testing enhancedSplit("vampires and werewolves are mainly nocturnal creatures", ["a", "m", "n", "x", "z"], False):', enhancedSplit("vampires and werewolves are mainly nocturnal creatures", ["a", "m", "n", "x", "z"], False)) # multiple delims, some present
    print()

    print('Testing enhancedSplit("repetition", [], True):', enhancedSplit("repetition", [], True)) # no delims
    print()

    print('Testing enhancedSplit("repetition", ["e"], True):', enhancedSplit("repetition", ["e"], True)) # 1 delim, present
    print()

    print('Testing enhancedSplit("i am the very model of a modern major-general", ["p"], True):', enhancedSplit("i am the very model of a modern major-general", ["p"], True)) # 1 delim, not present
    print()

    print('Testing enhancedSplit("why is the sun yellow and not blue", ["m", "x", "z"], True):', enhancedSplit("why is the sun yellow and not blue", ["m", "x", "z"], True)) # multiple delims, none present
    print()

    print('Testing enhancedSplit("vampires and werewolves are mainly nocturnal creatures", ["a", "m", "n", "x", "z"], True):', enhancedSplit("vampires and werewolves are mainly nocturnal creatures", ["a", "m", "n", "x", "z"], True)) # multiple delims, some present
    print()

    # Add your own tests here
    print()

    # Test of Part 2
    print("Testing flatten([]):", flatten([])) # empty list
    print()

    print("Testing flatten([2]):", flatten([2])) # 1-element flat list
    print()

    print("Testing flatten([3, 6, 1, 0]):", flatten([3, 6, 1, 0])) # multi-element flat list
    print()

    print("Testing flatten([[5]]):", flatten([[5]])) # 1-element nested list
    print()

    print("Testing flatten([1, 3, 5, [7], 9, 11]):", flatten([1, 3, 5, [7], 9, 11])) # multi-element, 1 nested list
    print()

    print("Testing flatten([[6], 32, 36, 59, [93, 54], 98, [88]]):", flatten([[6], 32, 36, 59, [93, 54], 98, [88]])) # multi-element, multiple nested lists
    print()

    print("Testing flatten([[[[3]]]]):", flatten([[[[3]]]])) # 1-element, multiply-nested list
    print()

    print("Testing flatten([65, [52, 41], [7, [14, 35], 93], 73, 33, 94, 44, [63, 24, [[27, 88], [78, 75, 13], 31], 84]]):", flatten([65, [52, 41], [7, [14, 35], 93], 73, 33, 94, 44, [63, 24, [[27, 88], [78, 75, 13], 31], 84]])) # multi-elelent, elements of vsarying nesting level
    print()

    # Add your own tests here
    print()
    

