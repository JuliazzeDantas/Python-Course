'''Exercise: Write a program that reads a complete name and displays the first and the last name'''

name = input("Enter the complete name: ").strip().split()

print('The first name is "{}" and the last name is "{}"'.format(name[0], name[len(name) - 1]))