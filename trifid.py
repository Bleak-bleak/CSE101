# Your name:Xingtong Zhou
#
# Trifid Cipher (Homework 1-2) starter code
# CSE 101, Fall 2018

import string

# DO NOT MODIFY THIS HELPER FUNCTION!!!
def invert(source):
    t = {}
    for k in source:
        t[source[k]] = k
    return t


# COMPLETE THE FUNCTIONS BELOW FOR THIS ASSIGNMENT

def buildEncipheringTable(key):
    new_key=key.upper()
    new_key=new_key.replace(" ","")
    available=list(string.ascii_uppercase)+["!"]
    lookup=[1,[],[],[]]
    track=1
    for i in new_key:
        if i in available:
            available.remove(i)
            lookup[track].append(i)
            if len(lookup[track]) == 9:
                track += 1
    for y in available:
        lookup[track].append(y)
        if len(lookup[track]) == 9:
            track += 1
    empt_dic={}
    for x in range(1,4):
        for z in lookup[x]:
            firstDigit= x
            letterIndex= lookup[x].index(z)
            secondDigit=(letterIndex//3)+1
            thirdDigit=(letterIndex%3)+1
            empt_dic[z]=firstDigit*100+secondDigit*10+thirdDigit
            
            
    return empt_dic
            
        
        
        
    


def encipher(message, key):
    trig = buildEncipheringTable(key)
    row_1=""
    row_2=""
    row_3=""
    new_message= message.replace(" ","").upper()
    for a in new_message:
        letter = str(trig[a])
        row_1 = row_1 + letter[0]
        row_2 = row_2 + letter[1]
        row_3 = row_3 + letter[2]
    reverse = invert(trig)
    combi = ""
    final = ""
    b=0
    for n in range(len(row_1)):
        combi += row_1[b:b+5] + row_2[b:b+5] + row_3[b:b+5]
        row_1 = row_1[b+5:]
        row_2 = row_2[b+5:]
        row_3 = row_3[b+5:]
    message=""
    left=0
    while b < len(combi)/3:
        chunks = int(combi[left:left+3])
        left += 3
        b += 1
        message += reverse[chunks]
    while len(message)%5 != 0:
        message += "X"
    add=[]
    d=0
    for e in range(int(len(message)/5)):
        add.append(message[d:d+5])
        d += 5
    result=" ".join(add)
        
        
    
    return result


# DO NOT modify or remove the code below! We will use it for testing.

if __name__ == "__main__":
    # Testing Part 1
    print('Testing buildEncipheringTable() with key "DRAGON"...')
    table1 = buildEncipheringTable("DRAGON")
    print('The trigram for "R" is:', table1["R"])
    print('The trigram for "I" is:', table1["I"])
    print('The trigram for "Z" is:', table1["Z"])
    print()

    print('Testing buildEncipheringTable() with key "NEPTUNE"...')
    table2 = buildEncipheringTable("NEPTUNE")
    print('The trigram for "B" is:', table2["B"])
    print('The trigram for "J" is:', table2["J"])
    print('The trigram for "V" is:', table2["V"])
    print()

    print('Testing buildEncipheringTable() with key "CHALLENGER"...')
    table3 = buildEncipheringTable("CHALLENGER")
    print('The trigram for "E" is:', table3["E"])
    print('The trigram for "Q" is:', table3["Q"])
    print('The trigram for "T" is:', table3["T"])
    print()

    # Testing Part 2
    print('Calling encipher() with message "TOBEORNOTTOBE" and key "HAMLET":', encipher("TOBEORNOTTOBE", "HAMLET"))
    print()

    print('Calling encipher() with message "SPACETHEFINALFRONTIER" and key "KIRK":', encipher("SPACETHEFINALFRONTIER", "KIRK"))
    print()

    print('Calling encipher() with message "FOUR SCORE AND SEVEN YEARS AGO" and key "LINCOLN":', encipher("FOUR SCORE AND SEVEN YEARS AGO", "LINCOLN"))
    print()

    print('Calling encipher() with message "The Helvetii compelled by the want of everything sent ambassadors to him about a surrender" and key "caesar":', encipher("The Helvetii compelled by the want of everything sent ambassadors to him about a surrender", "caesar"))
    print()

    print('Calling encipher() with message "Alan Turing was a leading participant in the breaking of German ciphers at Bletchley Park" and key "ENIGMA":', encipher("Alan Turing was a leading participant in the breaking of German ciphers at Bletchley Park", "ENIGMA"))
    print()

    print()

