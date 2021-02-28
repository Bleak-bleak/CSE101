# Xingtong Zhou
# CSE 101
# Lab 8


# IN THIS PART OF THE FILE, IT IS VERY IMPORTANT THAT YOU *ONLY* WRITE CODE
# INSIDE THE FUNCTION DEFINITIONS BELOW! IF YOU WRITE CODE BETWEEN (AND OUTSIDE)
# THE FUNCTION DEFINITIONSS, THE GRADING SYSTEM WILL NOT BE ABLE TO READ YOUR
# CODE AND YOU WILL RECEIVE A GRADE OF ZERO FOR THIS ASSIGNMENT!

class Fish:
    def __init__(self, name, species, color, weight):
        self._name = name
        self._species = species
        self._color = color
        self._weight = weight
        
    
    def __repr__(self):
        current_fish = "<><" +" "+ "("+self._name+", "+self._color+" "+ self._species+")"
        return current_fish
    
    def __lt__(self, other):
        if self._weight < other._weight:
            return True
        else:
            return False
    
    def kind(self):
        
        return self._species


def createFish(data):
    base = data.split(" ")
    create = Fish(base[1],base[0],base[2],float(base[3]))
    return create

class Aquarium:
    def __init__(self, capacity):
        self._emptlist=[]
        self._capacity = capacity
        
    
    def __repr__(self):
        number = 0
        output = ""
        for x in range(len(self._emptlist)):
            if number%2 == 0:
                output += self._emptlist[x].__repr__() + "\t"
                number += 1 
            else:
                output += self._emptlist[x].__repr__() + "\n"
                number += 1
        return output
    
    def add(self, newFish):
        if len(self._emptlist) < self._capacity:
            self._emptlist.append(newFish)
            return True
        else:
            return False
            
        
    
    def population(self):

        return len(self._emptlist)
        
    
    def countType(self, type):
        amount = 0
        for i in self._emptlist:
            if i._species == type:
                amount += 1
                
        return amount

def fillAquarium(filename, gallons):
        NEW_Aquarium = Aquarium(gallons)
        for line in open(filename):
            addf=createFish(line)
            NEW_Aquarium.add(addf)
            
            
        return NEW_Aquarium



# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE OR REMOVE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    # Test the Fish class
    print("Creating three new fish...")
    fish_1 = Fish("Homer", "Guppy", "red", 3.4)
    fish_2 = Fish("Marge", "Cichlid", "blue", 2.8)

    # Test the createFish() function
    fish_3 = createFish("Tetra Bart yellow 1.3")

    # Test the __repr()__ and kind() methods
    print("Fish 1:", fish_1)
    print("Fish 1 is a", fish_1.kind())
    print("Fish 2:", fish_2)
    print("Fish 2 is a", fish_2.kind())

    if fish_3 != None:
        print("Fish 3:", fish_3)
        print("Fish 3 is a", fish_3.kind())

    # Test the __lt()__ method
    if fish_1 < fish_2:
        print("Fish 1 is smaller than Fish 2")
    else:
        print("Fish 1 is larger than Fish 2")
    
    if fish_3 != None and fish_1 < fish_3:
        print("Fish 1 is smaller than Fish 3")
    else:
        print("Fish 1 is larger than Fish 3")
    
    # Test the Aquarium class
    test_tank = Aquarium(20)
    print("The test tank's current population is:", test_tank.population())
    print("Adding fish now...")
    test_tank.add(fish_1)
    test_tank.add(fish_2)
    if fish_3 != None:
        test_tank.add(fish_3)
    print("The test tank's new population is:", test_tank.population())
    
    print()
    print(test_tank)
    print()

    print("The test tank contains", test_tank.countType("Cichlid"), "Cichlid(s).")
    print("The test tank contains", test_tank.countType("Guppy"), "Guppy (or Guppies).")
    print("The test tank contains", test_tank.countType("Tetra"), "Tetra(s).")
    print("The test tank contains", test_tank.countType("Mollie"), "Mollie(s).")
    print()

    # Test the fillAquarium() function
    print("Creating a new 15-gallon aquarium from tank1.txt...")
    tank1 = fillAquarium("tank1.txt", 15)
    if tank1 != None:
        print("tank1 contains", tank1.population(), "fish:")
        print()
        print(tank1)

    print("Creating a new 30-gallon aquarium from tank2.txt...")
    tank2 = fillAquarium("tank2.txt", 30)
    if tank2 != None:
        print("tank2 contains", tank2.population(), "fish:")
        print()
        print(tank2)

    print("Creating a new 10-gallon aquarium from tank3.txt...")
    tank3 = fillAquarium("tank3.txt", 10)
    if tank3 != None:
        print("tank3 contains", tank3.population(), "fish:")
        print()
        print(tank3)

