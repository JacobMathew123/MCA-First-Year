def string_copies(s,n):
    if n<0:
        return "n must be a none negative integer"
    return s*n
text=input("Enter a string:\n")
num=int(input("Enter number of copies:\n"))
print("String:",text)
print("Copies:",string_copies(text,num))