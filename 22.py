a = int(input("Enter your marks: "))

if a >= 90 and a <= 100:
    print("Grade A")

elif a >= 80 and a <= 89:
    print("Grade B")

elif a >= 70 and a <= 79:
    print("Grade C")

elif a >= 60 and a <= 69:
    print("Grade D")

elif a <= 59 and a >=0:
    print("Fail")

else:
    print("Invailid marks")