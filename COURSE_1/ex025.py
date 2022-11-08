'''Exercise: Write a program that reads the names and displays if the name have "Silva" '''

name = input("Enter the name: ")

name_split = name.split()
print(len(name_split))

answer = 0

for word in name_split:
    if(word == 'Silva'):
        answer = 1

if(answer == 1):
    print("Correct!")
else:
    print("Wrong!")