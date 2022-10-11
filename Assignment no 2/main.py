""" Cube root of a number

User: SaifullahZadran
created: 10/11/2022
"""

#Taking float as an input value
cube = float(input('Type a number for cube root: '))
epsilon = 0.01
num_guesses = 0
low = 0
high = max(1, cube)
guess = (high + low)/2.0
while abs(guess**3 - cube) >= epsilon:
    if guess**3 < cube:
        low = guess
    else:
        high = guess
    guess = (high + low)/2.0
    num_guesses += 1
print('num_guesses =', num_guesses)
print(guess, 'is close to the cube root of', cube)