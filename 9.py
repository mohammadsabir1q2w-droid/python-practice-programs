while True:
    year = int(input("Enter a year: "))

    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
       print(year, "is a Leap Year")
    else: 
       print(year, "ia Not a Leap Year") 

    ch = input("Do you want to check another year? (yes/no): ")

    if ch.lower() != "yes":
       print("Program Ended.")
       break