'''Exercise: Write a program to read a salary and the desired increase in the wage, then print the new value.'''

salary = float(input("Enter a salary: "))
increase = float(input("Enter the increase wage (in percent): "))

newSalary = salary + salary*increase/100

print("Your new salary is {}".format(newSalary))


