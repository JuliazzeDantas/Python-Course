'''Exercise: Write a program receive the speed of car and displays the value os traffic ticket'''

speed = float(input("Enter the speed: "))

if(speed > 80):
    print("The value of traffic ticket is {}".format((speed - 80) * 7.00))