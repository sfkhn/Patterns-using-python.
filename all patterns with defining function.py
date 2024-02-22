#Defining each function.
def prnt():
    print("Press 1 to print equal row and column.")
    print("Press 2 to print pattern eqaul to line.")
    print("Press 3 to reverse of option 2.")
    print("Press 4 to print a Triangle.")
    print("Press 5 to print mirror of option 2.")
    print("Press 6 to print reverse triangle.")
    print("Press 7 to print mirror of option 3.")
    print("Press 8 to exit")

def equal():
    for row in range(a,b+1):
        for col in range(a,b+1):
            print("*",end=" ")
        print()

def line():
    for row in range(a,b+1):
        for col in range(row):
            print("*",end=" ")
        print()

def reverse():
    for row in range(b,a-1,-1):
        for col in range(row):
            print("*",end=" ")
        print()

def triangle():
    for row in range(1,x+1):
        for sp in range(x-row):
            print("", end=" ")
        for col in range(row):
            print("*",end=" ")
        print("")

def mirror():
    for row in range(1,x+1):
            for sp in range(x-row):
                print(" ", end=" ")#for equilateral time just remove space.
            for col in range(row):
                print("*",end=" ")
            print("")

def rtriangle():
    for row in range(x,0,-1):
        for sp in range(x-row):
                print("", end=" ")
        for col in range(row):
            print("*",end=" ")
        print()

def rmirror():
    for row in range(x,0,-1):
        for sp in range(x-row):
                print(" ", end=" ")
        for col in range(row):
            print("*",end=" ")
        print()

while True:
    prnt()
    n = int(input("Enter a number: "))

    if n==1:
        a=int(input("Enter the number of rows: "))
        b=int(input("Enter the number of column: "))
        equal()
    
    elif n==2:
        a=int(input("Enter the number of rows: "))
        b=int(input("Enter the number of column: "))
        line()

    elif n==3:
        print("Note: Always a<b")
        a=int(input("Enter the number of rows: "))
        b=int(input("Enter the number of column: "))
        reverse()

    elif n==4:
        x=int(input("Enter the no. of rows: "))
        triangle()

    elif n==5:
        x=int(input("Enter the no. of rows: "))
        mirror()

    elif n==6:
        x=int(input("Enter the number of rows: "))
        rtriangle()

    elif n==7:
        x=int(input("Enter the number of rows: "))
        rmirror()

    elif n==8:
        break

    else:
        print("Enter a valid number.")

