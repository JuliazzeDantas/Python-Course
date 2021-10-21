''''Exercise: Write a program to read how much money (BRL) the user has, then convert it to dollar (USD).'''
'''01/10/2021 - 13:02   USD 1.00 => BRL 5.37'''

money = (float)(input("How much money do you have?: "))

dollar = money/5.37

if(dollar < 0):
    print("Invalid Value!")
elif(dollar < 1):
    print("You have {} reais and can buy {} cents of dollars" .format(money, dollar))
elif(dollar == 1):
    print("You have {} reais and can buy 1 dollar" .format(money))
else:
    print("You have {} reais and can buy {} dollars" .format(money, dollar))
