'''Exercise: Write a program to read a number and to print its table.'''

number = int(input("Digit any integer number: "))

print("--------------")
for counter in range(11):
    print("{} x {} = {}".format(number, counter, (number * counter)))
print("--------------")
