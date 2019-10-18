import time

lines=9
column=int(lines*2.5)
space=15
x=y=0

one_third=int(lines*(1/3)-1)
two_third=lines*(2/3)
down_count=0
top_count=1

def sp(num):
    while num >= 0:
        print(" ",end="")
        num=num-1

def sp_up(num1):
    while (num1 >= 0):
        print("*", end="")
        sp(5 * top_count)
        num1 = num1 - 1

while x < lines:
  #  time.sleep(2)
    space1 = space
    sp(space)
    space=space1
    if(x <= one_third):

        if(x == 0):
            print("*",end="")
            sp(space1-one_third)
            print("*")
        elif(x == one_third):
            sp_up(1)
            print("*")
            top_count=top_count+1
        else:
            sp_up(2)
            print("*")
            top_count=top_count+1
        if(x == one_third):
            space=space-1
        else:
            space=space-2
    else:
        print("*",end="")
        sp(column - down_count)
        down_count=down_count+4
        print("*")
        if(x == one_third):
            space=space+1
        else:
            space=space+2
    x=x+1