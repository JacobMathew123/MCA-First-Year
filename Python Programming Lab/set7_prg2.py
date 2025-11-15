def check(n):
    if n%2==0:
        return"Even"
    else:
        return"Odd"
num=int(input("Enter a number:"))
print("The given number",num,"is",check(num))