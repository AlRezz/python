power = int(input("Enter number: "))
result = 0
for n in range(1, power + 1):
    result += 1 / 2 ** n
print(result)