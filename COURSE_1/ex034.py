'''Exercise: Write a program that reads a salary and displays the new one. If salary is bigger than 1250.00, then the encresead is 10% and if it is less or equal 1250, the the encreased is 15%'''

salary = float(input("Enter your salary: "))


if(salary > 1250):
    print("Your new salary is {}".format(salary + (salary * 0.1)))
else:
    print("Your new salary is {}".format(salary + (salary * 0.15)))