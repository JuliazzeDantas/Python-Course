'''Exercise: Write a program to read the disance of a trip and displays the price of the travel.
    0.25 until 200 Km
    045 after 200 Km'''

km = float(input("Enter the distance: "))
price = 0

if(km <= 200):
    price = km * 0.5
else:
    price = 200 * 0.45

print("The price is {}". format(price))