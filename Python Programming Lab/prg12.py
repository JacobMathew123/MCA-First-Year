age=int(input("Enter age:"))
print("age",age)
if age<10:
    print("Ticket rate is 7")
elif age>=10 and age<60:
    print("Ticket rate is 10")
elif age>=60:
    print("Ticket rate is 5")
else:
    print("Invalid")