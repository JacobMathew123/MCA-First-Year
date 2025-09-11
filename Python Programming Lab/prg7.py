a=int(input("Enter first number:\n"))
b=int(input("Enter Second number:\n"))
print("Arithmetic Operations:")

print(f"{a} + {b} = {a+b}")
print(f"{a} - {b} = {a-b}")
print(f"{a} * {b} = {a*b}")

if b!=0:

    print(f"{a} / {b} = {a/b}")
    print(f"{a} % {b} = {a%b}")
    print(f"{a} // {b} = {a//b}")

else:

    print("Division, Floor division and modulus are not possible(Division by zero).")

print(f"{a} ** {b} = {a**b}")