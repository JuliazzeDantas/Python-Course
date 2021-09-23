int1 = int(input("Digit the first number: "))
int2 = int(input("Digit the second number: "))

print("The sum is equal to ", int1 + int2)

float1 = float(input("Digit the first number: "))
float2 = float(input("Digit the first number: "))

print("The multiplication is equal to ", float1 * float2)
print("The multiplication of {} and {} is equal to {}" .format(float1, float2, float1 * float2))

boolean = bool(input("Empty variable? "))
if(not boolean):
    print("TURE!")
else:
    print("FALSE!")

string = str(input("Digit your phrase: "))
print("This is your phrase: ", string)