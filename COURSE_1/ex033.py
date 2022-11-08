'''Exercise: Write a program that reads three numbers and shows them in ascending order'''

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))

if a > b and a > c:
    if b > c:
        print('Highest number: {} \nLowest number: {}'.format(a, c))
    else:
        print('Highest number: {} \nLowest number: {}'.format(a, b))
elif b > c and b > a:
    if c > a:
        print('Highest number: {} \nLowest number: {}'.format(b, a))
    else:
        print('Highest number: {} \nLowest number: {}'.format(b, c))
else:
    if a > b:
        print('Highest number: {} \nLowest number: {}'.format(c, a))
    else:
        print('Highest number: {} \nLowest number: {}'.format(c, b))