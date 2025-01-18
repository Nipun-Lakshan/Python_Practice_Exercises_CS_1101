# Example 02: Pass / Fail Grade Calculation for CS1101
print()
print("========================================")
print("Pass / Fail Grade Calculation for CS1101")
print("========================================")
print()
mark_1 = int(input("Enter Assignment 01 Marks: "))
mark_2 = int(input("Enter Assignment 02 Marks: "))
mark_3 = int(input("Enter Assignment 03 Marks: "))
mark_4 = int(input("Enter Assignment 04 Marks: "))
print()
total = mark_1 + mark_2 + mark_3 + mark_4
average = total / 4
print("Average Mark for Assignment : " + str(average))
if (average >= 40):
    print("")
