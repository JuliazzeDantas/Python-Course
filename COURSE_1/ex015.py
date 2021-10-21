'''Exercise: Write a program to read how many kilometers a rental car has traveled and how many days
it has been rented. Calculate the price to pay.'''

'''Information: 
* car costs R$60 per day 
* US$0.15 per km driven.'''

kilometers = float(input("Hoe many kilometers the car has traveled: "))
days = int(input("How many days the car has been rented: "))

days = days * 60
kilometers = kilometers * 0.15

print("The costumer must to pay {} dollars!".format(days + kilometers))