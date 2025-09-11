def exchange_first_last(s):
    if len(s)<=1:
        return s
    return s[-1]+s[1:-1]+s[0]
text=input("Enter a word:\n");
print("Original:",text);
print("Modified:",exchange_first_last(text));
