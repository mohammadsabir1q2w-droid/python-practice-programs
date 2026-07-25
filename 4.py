a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

largest = a if a > b else b

print("Largest number=", largest)
print("Condition=", a > b)