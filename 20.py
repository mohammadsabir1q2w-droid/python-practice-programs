a = int(input("Enter a number: "))

if a % 5 == 0 and a % 11 == 0:
    print(a,"is Divisible by 5 and 11")

elif a % 5 == 0:
    print(a,"is Divisible by 5")

elif a % 11 == 0:
    print(a,"is Divisible by 11")

else:
    print(a,"is not Divisible by 5 and 11")