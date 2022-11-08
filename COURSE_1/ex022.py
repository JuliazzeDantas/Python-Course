'''Exercise: Write a program that reads a name and displays:
    * The name in all uppercase and lowercase letters
    * How many letters in total
    * How many letters are in the first name
'''

name = input("Enter the name: ")

print(f"Uppercase: {name.upper()}")
print(f"Lowercase: {name.lower()}")

print(f"The name has {len(name.replace(' ','A'))} letters")
#print(f"The name has {len(name) - name.count(' ')} letters")

print(f"The first name has {len(name.split(' ')[0])} letters")