age=int(input("Enter your age: "))

if age < 13: 
    print("child")
elif age >= 13 and age < 18:
    print("teenager")
elif age >= 18 and age < 65:
    print("adult")
elif age > 65:
    print("elder")
else:
    print("Provide correct age")