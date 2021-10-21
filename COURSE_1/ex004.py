'''Exercise: Write a program to read what user enter and print some of this variable's characteristics.'''

variable = input("Enter something: ")

print("The primitive type is ", type(variable))

print("There is only spaces? ", variable.isspace())

print("There is only numbers? ", variable.isnumeric())

print("There is only lyrics? ", variable.isalpha())

print("There is only alphanumerics? ", variable.isalpha())

print("There is only lowercase letters? ", variable.islower())

print("There is only capital letters? ", variable.isupper())

print("There is capital letters and lowercase letters? ", variable.istitle())