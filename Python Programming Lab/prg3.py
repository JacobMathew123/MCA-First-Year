def replace_occurrences(s):
   first_char=s[0];
   result=first_char + s[1:].replace(first_char,'$');
   return result
text=input("Enter a word:\n");
print("Original:",text);
print("Modified:",replace_occurrences(text));