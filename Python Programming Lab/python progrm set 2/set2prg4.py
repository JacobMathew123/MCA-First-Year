# 4. From a list of integers, create a list after removing even numbers


nums = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
result = []
for n in nums:
    if n % 2 != 0:
       result.append(n)   # keep only odd numbers
print("Entered numbers:", nums)
print("List after removing even numbers:", result)
