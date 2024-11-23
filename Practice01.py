# Find the Largest Number between Two Numbers
print()
print("Find the Largest Number between Two Numbers")
print("===========================================")
print()
num1 = int(input("Enter number 01: "))
num2 = int(input("Enter number 02: "))
print()
x = num1 - num2
if (x == 0):
    print("Two numbers are equal!")
elif (x < 0):
    print("Largest Number :- " + str(num2))
else:
    print("Largest Number :- " + str(num1))
print("===========================================")
