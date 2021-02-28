# Your name:Xingtong Zhou
#
# CSE 101, Fall 2018
# Assignment 3-2 (List Manipulation) starter code

# Complete the functions below for this assignment

def magicSquare(n):
    squares = []
    if n <= 0:
        return None

    elif n%2 == 0:
        return None



    if n%2 != 0:
        squares = [ [-1 for i in range(n)] for i in range(n)]
        squares[0][((n-1)//2)] = 1
        row = 0
        column = (n-1)//2
        new_row=0
        for i in range(2,(n**2+1)):
            if column > 0:
                column = column -1
                if row > 0:
                    row = row - 1
                    if squares[row][column] == -1:
                        squares[row][column]=i
                        
                
                    elif squares[row][column] != -1:
                        column = column + 1
                        row = row + 2
                        squares[row][column]=i
                else:
                    row = n-1
                    if squares[row][column] == -1:
                        squares[row][column]=i
                        
                
                    elif squares[row][column] != -1:
                        column = column + 1
                        row = row-n+2
                        squares[row][column]=i


            else:
                column = n-1
                if row > 0:
                    row = row - 1
                    if squares[row][column] == -1:
                        squares[row][column]=i
                        
                
                    elif squares[row][column] != -1:
                        column = column -n+1
                        row = row + 2

                        squares[row][column]=i
                else:
                    row = n-1
                    if squares[row][column] == -1:
                        squares[row][column]=i
                        
                
                    elif squares[row][column] != -1:
                        column = column-n+1
                        row = row -n+2
                        squares[row][column]=i
            
                    
            
                
                                 
                    
    return squares


def checkCourses(required, filename):
    dic = {}
    retake = []
    for line in open(filename):
        base = line.split(" ")
        
        dic.setdefault(base[0],int(base[1]))
    for i in required:
        
        if i in dic and int(dic[i]) < 75:
            retake.append(i)
        elif i not in dic:
            retake.append(i)
    if len(retake) == 0:
        return True
    

    
    return retake
            
              



# DO NOT modify or remove the code below! We will use it for testing.

if __name__ == "__main__":
    # Test of Part 1
    print("Creating a magic square with n = -3:")
    s = magicSquare(-3)
    if s == None:
        print("Result: None (Invalid square size)")
    else:
        print(s, "\n")
        print("Formatted square:")
        for r in s: # print row-by-row
            for c in r: # print each element in the current row
                print(c, "\t", sep='', end='')
            print()
        print()
    print()

    print("Creating a magic square with n = 5:")
    s = magicSquare(5)
    if s == None:
        print("Result: None (Invalid square size)")
    else:
        print(s, "\n")
        print("Formatted square:")
        for r in s: # print row-by-row
            for c in r: # print each element in the current row
                print(c, "\t", sep='', end='')
            print()
        print()
    print()

    print("Creating a magic square with n = 7:")
    s = magicSquare(7)
    if s == None:
        print("Result: None (Invalid square size)")
    else:
        print(s, "\n")
        print("Formatted square:")
        for r in s: # print row-by-row
            for c in r: # print each element in the current row
                print(c, "\t", sep='', end='')
            print()
        print()
    print()

    print("Creating a magic square with n = 4:")
    s = magicSquare(4)
    if s == None:
        print("Result: None (Invalid square size)")
    else:
        print(s, "\n")
        print("Formatted square:")
        for r in s: # print row-by-row
            for c in r: # print each element in the current row
                print(c, "\t", sep='', end='')
            print()
        print()
    print()

    # Add your own tests here

    # Test of Part 2
    requiredCourses = ["CSE114", "CSE214", "CSE215", "CSE216", "CSE220", "CSE300", "CSE303", "CSE310", "CSE312", "CSE316", "CSE320", "CSE373", "CSE416"]

    print("Result of calling checkCourses() with file 'transcript1.txt':", checkCourses(requiredCourses, "transcript1.txt"))
    print()

    print("Result of calling checkCourses() with file 'transcript2.txt':", checkCourses(requiredCourses, "transcript2.txt"))
    print()

    print("Result of calling checkCourses() with file 'transcript3.txt':", checkCourses(requiredCourses, "transcript3.txt"))
    print()

    # Add your own tests here

    print()
    

