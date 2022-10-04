"""

Swapping two numbers Assignment

User: SaifullahZadran
created: 2/10/2021

"""

a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))

c = a  #Assigning value of a to c, which is a temporary variable
a = b  #Assigning value of b to c
b = c  #Assigning value of c to a

print ("1st number after swapped: ", a)
print ("2nd number after swapped: ", b)

