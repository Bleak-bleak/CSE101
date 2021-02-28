#Xingtong Zhou
# CSE 101
# Lab 5

# IN THIS PART OF THE FILE, IT IS VERY IMPORTANT THAT YOU *ONLY* WRITE CODE
# INSIDE THE FUNCTION DEFINITIONS BELOW! IF YOU WRITE CODE BETWEEN (AND OUTSIDE)
# THE FUNCTION DEFINITIONSS, THE GRADING SYSTEM WILL NOT BE ABLE TO READ YOUR
# CODE AND YOU WILL RECEIVE A GRADE OF ZERO FOR THIS ASSIGNMENT!

def removeLast(first, second):
    editing=first
    delete=second
    new_string=""
    for g in delete:
        a=editing.rfind(g)
        if a !=-1:
            editing = editing[:a] + editing[a+1:]
    return editing


def statement(init_balance, transactions):
    for i in transactions:
        if i[0] == "credit":
            init_balance -= i[1]
        elif i[0] == "debit":
            init_balance += i[1]
        elif i[0] =="interest":
            init_balance += ( init_balance*(i[1]))
           
    return init_balance


def limboScore(scores, contestant):
    sunl=0
    for i in range(len(scores)):
        if scores[i][0] == contestant:
            sunl += scores[i][1] + 5
        else:
            sunl += scores[i][1] * 2
            
            
    return sunl/14


def getHost(url):
    a=url.find("://")
    if a != -1:
        url = url[a+3:]
        b=url.find("/")
        if b != -1:
            url = url[:b]
            c=url.rfind(".")
            if c != -1:
                url = url[:c]
                d=url.rfind(".")
                if d != -1:
                    url = url[d+1:]
    return url


# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE OR REMOVE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    ############### Part 1 Tests ###############
    print('Testing removeLast("starlord", "thor"):', removeLast("starlord", "thor")) # only some characters appear in first string

    print('Testing removeLast("graymalkin", "rag"):', removeLast("graymalkin", "rag")) # all characters appear in first string

    print('Testing removeLast("Booster Gold", "Aquaman"):', removeLast("Booster Gold", "Aquaman")) # no characters appear in first string

    print('Testing removeLast("Super Linsefvdan", "sefv"):', removeLast("Super Linsefvdan", "sefv")) # no characters appear in first string
    print()  # prints a blank line

    ############### Part 2 Tests ###############
    print('Testing statement(219.73, [["credit", 102.88], ["credit", 468.64], ["interest", 0.23], ["debit", 128.48]]):')
    print("Final balance:", statement(219.73, [["credit", 102.88], ["credit", 468.64], ["interest", 0.23], ["debit", 128.48]]))
    print()

    print('Testing statement(40.22, [["debit", 474.23], ["interest", 0.32], ["debit", 452.68], ["debit", 158.95], ["interest", 0.34], ["credit", 34.47]]):')
    print("Final balance:", statement(40.22, [["debit", 474.23], ["interest", 0.32], ["debit", 452.68], ["debit", 158.95], ["interest", 0.34], ["credit", 34.47]]))
    print()

    print('Testing statement(1220.61, [["credit", 393.09], ["credit", 62.42], ["credit", 284.84], ["payment", 88.19], ["debit", 153.12], ["payment", 122.98], ["credit", 69.1], ["interest", 0.06]]):')
    print("Final balance:", statement(1220.61, [["credit", 393.09], ["credit", 62.42], ["credit", 284.84], ["payment", 88.19], ["debit", 153.12], ["payment", 122.98], ["credit", 69.1], ["interest", 0.06]]))
    print()

    print('Testing statement(220.00, [["credit", 50.00], ["credit", 20.00], ["interest", 0.23], ["debit", 200.00]]):')
    print("Final balance:", statement(220, [["credit", 50.00], ["credit", 20.00], ["interest", 0.23], ["debit", 200.00]]))
    print()

    ############### Part 3 Tests ###############
    print('Testing limboScore([["Kenya", 1.8], ["France", 7.8], ["Ethiopia", 1.4], ["India", 5.7], ["South Korea", 8.9], ["Norway", 3.4], ["Morocco", 4.1]], "Thailand"):')
    print("Final score:", limboScore([["Kenya", 1.8], ["France", 7.8], ["Ethiopia", 1.4], ["India", 5.7], ["South Korea", 8.9], ["Norway", 3.4], ["Morocco", 4.1]], "Thailand"))
    print()

    print('Testing limboScore([["USA", 8.4], ["Finland", 2.5], ["Germany", 7.5], ["Jamaica", 1.5], ["Russia", 3.6], ["Poland", 7.9], ["South Africa", 3.7]], "Egypt"):')
    print("Final score:", limboScore([["USA", 8.4], ["Finland", 2.5], ["Germany", 7.5], ["Jamaica", 1.5], ["Russia", 3.6], ["Poland", 7.9], ["South Africa", 3.7]], "Egypt"))
    print()

    print('Testing limboScore([["Norway", 1.4], ["Aruba", 1.3], ["Russia", 8.4], ["Jamaica", 5.5], ["Spain", 2.6], ["USA", 3.3], ["Morocco", 3.0]], "Spain"):')
    print("Final score:", limboScore([["Norway", 1.4], ["Aruba", 1.3], ["Russia", 8.4], ["Jamaica", 5.5], ["Spain", 2.6], ["USA", 3.3], ["Morocco", 3.0]], "Spain"))
    print()

    print('Testing limboScore([["USA", 7.0], ["Finland", 4.5], ["Germany", 6.0], ["Jamaica", 3.3], ["Russia", 6.1], ["Poland", 5.4], ["South Africa", 7.9]], "Poland"):')
    print("Final score:", limboScore([["USA", 7.0], ["Finland", 4.5], ["Germany", 6.0], ["Jamaica", 3.3], ["Russia", 6.1], ["Poland", 5.4], ["South Africa", 7.9]], "Poland"))
    print()

    ############### Part 4 Tests ###############
    print('getHost("irc://foo.com/") returns:', getHost("irc://foo.com/"))
    print('getHost("http://i.am.a.hostname.edu/blah/blah/") returns:', getHost("http://i.am.a.hostname.edu/blah/blah/"))
    print('getHost("ftp://some-like.it-hot.net/something/filename.pdf") returns:', getHost("ftp://some-like.it-hot.net/something/filename.pdf"))
    print('getHost("irc://hpwudi666.com/") returns:', getHost("irc://hpwudi666.com/"))

    # Write your own tests for Part 4 here!
    print()  # prints a blank line


