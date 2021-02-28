#Xingtong Zhou
#
# CSE 101, Fall 2018
# Assignment 3-1 (Playlists) starter code

# Complete the functions below for this assignment

import string, random

def buildLibrary(filename):
    my_dic = {}
    new_time = []
    for line in open(filename):
        base = line.split(",")
        edi_time = base[3].split(":")
        new_time=int(edi_time[0])*60 + int(edi_time[1])
        new_list =[base[1],base[2],new_time]
        my_dic.setdefault(base[0],[]).append(new_list)
        
    return my_dic


def buildPlayList(library, genres, length):
    emptlist= []
    for n in genres:
        if n not in library:
            emptlist = emptlist
        else:
            emptlist = emptlist + library[n]
    for n in range(len(emptlist)):
        emptlist[n] = tuple(emptlist[n][:2])
            
    if len(emptlist) >= length:
        return random.sample(emptlist,length)
    elif len(emptlist) == 0:
        return []
    else:
        return random.sample(emptlist,len(emptlist))
    
    



# DO NOT modify or remove the code below! We will use it for testing.

if __name__ == "__main__":
    # Test of Part 1
    print("Testing buildLibrary() with file 'library1.txt':")
    lib1 = buildLibrary("library1.txt")
    print("Library contents are:\n", lib1)
    print("\n\n")

    print("Testing buildLibrary() with file 'library2.txt':")
    lib2 = buildLibrary("library2.txt")
    print("Library contents are:\n", lib2)
    print("\n\n")

    print("Testing buildLibrary() with file 'library3.txt':")
    lib3 = buildLibrary("library3.txt")
    print("Library contents are:\n", lib3)
    print("\n\n")

    print("Testing buildLibrary() with file 'library4.txt':")
    lib4 = buildLibrary("library4.txt")
    print("Library contents are:\n", lib4)
    print("\n\n")

    # Test of Part 2
    # normal operation
    print("Testing buildPlayList() on the contents of library1.txt: 6 songs drawn from the blues, childrens, and dance genres:", buildPlayList(lib1, ["blues", "childrens", "dance"], 6))
    print()

    # Too few songs
    print("Testing buildPlayList() on the contents of library1.txt: 12 songs drawn from the blues and kpop genres:", buildPlayList(lib1, ["blues", "kpop"], 12))
    print()
    
    # Nonexistent genre
    print("Testing buildPlayList() on the contents of library2.txt: 4 songs drawn from the classical, country, and opera genres:", buildPlayList(lib2, ["classical", "country", "opera"], 4))
    print()
    
    # No valid genres
    print("Testing buildPlayList() on the contents of library3.txt: 8 songs drawn from the classical, childrens, and dance genres:", buildPlayList(lib3, ["classical", "childrens", "dance"], 8))
    print()
    

