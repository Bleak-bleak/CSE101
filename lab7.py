# Xingtong Zhou
# CSE 101
# Lab 7

import string

# IN THIS PART OF THE FILE, IT IS VERY IMPORTANT THAT YOU *ONLY* WRITE CODE
# INSIDE THE FUNCTION DEFINITIONS BELOW! IF YOU WRITE CODE BETWEEN (AND OUTSIDE)
# THE FUNCTION DEFINITIONSS, THE GRADING SYSTEM WILL NOT BE ABLE TO READ YOUR
# CODE AND YOU WILL RECEIVE A GRADE OF ZERO FOR THIS ASSIGNMENT!

def shopping(products, shopping_list):
    result = 0
    for i in range(len(shopping_list)):
        if shopping_list[i] in products:
            result += products[shopping_list[i]]
            
    return result


def recoverMessage(samples):
    dic = {}
    result = ""
    for i in range(len(samples[0])):
        for num in samples:
            dic.setdefault(num[i],0)
            dic[num[i]] += 1
        most_common = list(dic.keys())[0]
        for n in dic:
            if dic[most_common] < dic[n]:
                most_common = n
        result += most_common
        dic = {}
    
            
    
    return result

def buildIndex(filename):
    idx = {}
    text = ""
    for line in open(filename):
        text += line.lower()
    text = text.split()
    for i in range(len(text)):
        idx.setdefault(text[i],[])
        idx[text[i]].append(i)
        
    return idx



# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE OR REMOVE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    ############### Part 1 Tests ###############
    products = {'shampoo': 10, 'soap': 5, 'comb': 3, 'brush': 7, 'toothbrush': 2}
    print('For the following Part 1 tests, products is defined as:')
    print('\t' + str(products))
    shopping_list = ['shampoo', 'brush', 'shampoo', 'soap', 'soap', 'dog food', 'soap']
    print('Testing shopping() for shopping_list = \n\t' + str(shopping_list) + '\n' +
          '\tResult: ' + str(shopping(products, shopping_list)))
    shopping_list = ['candy', 'brush', 'brush', 'soap', 'fruit', 'soap']
    print('Testing shopping() for shopping_list = \n\t' + str(shopping_list) + '\n' +
          '\tResult: ' + str(shopping(products, shopping_list)))
    shopping_list = ['wood', 'paint', 'shovel', 'mop']
    print('Testing shopping() for shopping_list = \n\t' + str(shopping_list) + '\n' +
          '\tResult: ' + str(shopping(products, shopping_list)))

    # Write your own tests for Part 1 here!
    print()  # prints a blank line

    ############### Part 2 Tests ###############
    print('Testing recoverMessage(["edferfthm", "aqvorithm", "algbridnn", "glgoxirhm", "iogleielb", "alwxuithj", "wlaobifhm"]):', recoverMessage(["edferfthm", "aqvorithm", "algbridnn", "glgoxirhm", "iogleielb", "alwxuithj", "wlaobifhm"]))

    print('Testing recoverMessage(["citputejncienje", "cebautersmjynzt", "comcntewsciunwb", "foxuuterscienfe", "jomvuzerociiavn", "tojeotesstfdiqe", "computezsciryce"]):', recoverMessage(["citputejncienje", "cebautersmjynzt", "comcntewsciunwb", "foxuuterscienfe", "jomvuzerociiavn", "tojeotesstfdiqe", "computezsciryce"]))

    print('Testing recoverMessage(["ouanycrokk", "stwnyaraok", "rtraybrauk", "stinyfuslk", "stknlbrxzk", "hrirybraek", "sjofyborjd"]):', recoverMessage(["ouanycrokk", "stwnyaraok", "rtraybrauk", "stinyfuslk", "stknlbrxzk", "hrirybraek", "sjofyborjd"]))

    # Write your own tests for Part 2 here!
    print() # prints a blank line

    ############### Part 3 Tests ###############
    print('Testing buildIndex("sample1.txt"):', buildIndex("sample1.txt"))
    print()

    print('Testing buildIndex("sample2.txt"):', buildIndex("sample2.txt"))
    print()

    print('Testing buildIndex("sample3.txt"):', buildIndex("sample3.txt"))
    print()


    # Write your own tests for Part 3 here!
    print()  # prints a blank line


