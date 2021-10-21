'''Exercise: Write a program to check if user enter something (use if and boolean variable).'''

boolean = bool(input("Empty variable? "))
if(not boolean):
    print("TURE!")
else:
    print("FALSE!")