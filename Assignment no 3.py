"""

Submitted by Saifullah Zadran
Registration Number: 399546


"""

def move(firstcylinder,num):
    print("Move disc", num, "to the", firstcylinder, "cylinder\n")
 
def tower(n):
    for i in range(1,n**2):
        h = 1
        s = i
        while (s%2==0):
            s += 1
            s = s/2
        if ((s + 1)/2%3==0):
            move("A", n+1-h)
        elif ((n+1-h)%2==1 and (s+1)/2%3==1 or (n+1-h)%2==0 and (s+1)/2%3==2):
            move("C", n+1-h)
        elif (n+1-h)!=0:
            move("B", n+1-h)
tower(int(input("Enter the number of discs:")))