'''Exercise: Write a program to read thre lines and displays if they can form a triangle'''

r1 = float(input("Enter the first line: "))
r2 = float(input("Enter the first line: "))
r3 = float(input("Enter the first line: "))

if (r1 + r2 > r3) and (r2 + r3 > r1) and (r3 + r1 > r2):
    print("They can form a triangule")
else:
    print("They \033[0;31mcan't\033[m form a triangule")