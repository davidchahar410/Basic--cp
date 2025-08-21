n=int(input("Enter the First number"))
m=int(input("Enter the Second number"))
for i in range(1,n+1):
    for j in range(n+1-i):
        print("*", end="")
    print()