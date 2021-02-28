# Xingtong Zhou
# CSE 101
# Lab 1

# In this part of the file it is very important that you write code inside
# the functions only! If you write code in between the functions, then the
# grading system will not be able to read your code and grade your work!

def net_pay(hours, pay_rate, fed_rate, state_rate):
    net_pay= hours*pay_rate*(1-fed_rate-state_rate)
    return net_pay

def displacement(velocity, acceleration, time_init, time_final):
    Vi = velocity
    a = acceleration
    ti = time_init
    tf = time_final
    S=Vi*(tf-ti)+(a/2)*(tf-ti)**2
    return S

def stardate(month, day, year):
    month_number=month
    d=day
    y=year
    m=0
    if month_number==1:
        m=0
    elif month_number==2:
        m=31
    elif month_number==3:
        m=59
    elif month_number==4:
        m=90
    elif month_number==5:
        m=120
    elif month_number==6:
        m=151
    elif month_number==7:
        m=181
    elif month_number==8:
        m=212
    elif month_number==9:
        m=243
    elif month_number==10:
        m=273
    elif month_number==11:
        m=304
    elif month_number==12:
        m=334
    stardate=(1000*(y-2323))+((1000/365)*(m+d-1))
    return stardate

# Below you will see an if-statement and a few tests. It is REALLY important
# that you not delete this if-statement or the tests inside. You may, however,
# add more tests to the code below. You can format them however you like.

if __name__ == "__main__": # This line is needed for the auto-grader. DO NOT CHANGE IT!
    # Check the assignment itself to find what the correct outputs should be
    # for these tests.

    ############### Part I Tests ###############
    print('net_pay(25, 10, .15, .10) returns', net_pay(25, 10, .15, .10))
    print('net_pay(40, 8, .25, .25) returns', net_pay(40, 8, .25, .25))
    print('net_pay(35, 20, .2, .09) returns', net_pay(35, 20, .2, .09))
    print('net_pay(40, 20, .3, .10) returns', net_pay(40, 20, .3, .10))
    print()# prints a blank line

    ############### Part II Tests ###############
    print('displacement(5,2,1,7) returns', displacement(5,2,1,7))
    print('displacement(3,1,4,20) returns', displacement(3,1,4,20))
    print('displacement(18,-3,2,6) returns', displacement(18,-3,2,6))
    print('displacement(15,4,1,9) returns', displacement(15,4,1,9))
    print() # prints a blank line

    ############### Part III Tests ###############
    print('stardate(2,21,2365) returns', stardate(2,21,2365))
    print('stardate(11,29,2401) returns', stardate(11,29,2401))
    print('stardate(5,4,2390) returns', stardate(5,4,2390))
    print('stardate(9,17,2548) returns', stardate(5,4,2548))
    print() # prints a blank line

