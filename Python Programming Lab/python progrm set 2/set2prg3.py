#3. Write a program to prompt the user for a list of integers. For all values greater than 100,
#store ‘over’ instead.


nums = input("Enter a list of integers separated by spaces: ").split()
result = []
for n in nums:
    n = int(n)    # convert each input to integer
    if n > 100:
        result.append("over")
    else:
        result.append(n)

print(result)