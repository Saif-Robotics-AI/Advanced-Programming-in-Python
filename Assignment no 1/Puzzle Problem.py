"""

Calculate factorial of a number

User: SaifullahZadran
created: 2/10/2021

"""
a = input("What is your first move?: ")
while a == "forward":
    print("going straight!")
    a = input("What is your next move?: ")
while a=="right":
    print("moving towards right")
    a = input("What is your next move?: ")
while a == "left":
    print ("moving towards left")
    a = input("What is your next move?: ")
while a == "right":
    print("moving towards right")
    break
