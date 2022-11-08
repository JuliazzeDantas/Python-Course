'''Exercise: Write a program that reads the name of some city and displays if its name starts with "Santo" '''

city = input("Enter city's name: ")

city_first = city.split()[0]

if(city_first == 'Santo'):
    print("Correct!")
else:
    print("Wrong!")