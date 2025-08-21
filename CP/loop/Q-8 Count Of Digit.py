n = int(input("Enter an integer"))
count = 0
temp = abs(n)

if temp == 0:
    count = 1
else:
    while temp > 0:
        temp //= 10
        count += 1

print("Number of digits:", count)
