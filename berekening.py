import random

addition = int.__add__
subtraction = int.__sub__
multiplication = int.__mul__
division = int.__truediv__
increment = lambda a: a + 1
decrement = lambda a: a - 1

a, b = (random.randrange(1, 100), random.randrange(1, 101))

print(f'{a} \t+ \t{b} \t= {addition(a, b)}')
print(f'{a} \t- \t{b} \t= {subtraction(a, b)}')
print(f'{a} \t* \t{b} \t= {multiplication(a, b)}')
print(f'{a} \t/ \t{b} \t= {division(a, b)}')
print(f'{a} \t++ \t\t= {increment(a)}')
print(f'{a} \t-- \t\t= {decrement(a)}')
