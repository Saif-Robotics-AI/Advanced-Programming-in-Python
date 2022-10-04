"""

Calculate factorial of a number

User: SaifullahZadran
created: 2/10/2021

"""

a = int(input("Enter the number: "))

for i in range (1,a) [::-1]:
    a = i*a
    i -=1
print ("The factorial of the given number is: ", a)