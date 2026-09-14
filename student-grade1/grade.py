name = input("Enter student name: ")
mark1 = float(input("Enter first subject mark: "))
mark2 = float(input("Enter second subject mark: "))

total = mark1 + mark2
average = total / 2

print(f"\nStudent Name: {name}")
print(f"Total Mark: {int(total) if total.is_integer() else total}")
print(f"Average Mark: {int(average) if average.is_integer() else average}")

if average >= 50:
    print("Result: Pass")
else:
    print("Result: Fail")
