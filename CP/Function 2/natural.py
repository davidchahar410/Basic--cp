n=int(input("Enter your limits of natural numbers : "))
if(n>0):
    print("Your natural numbers are : ")
    i=1
    while(i<=n):
        print(i,end=" ")
        i=i+1
else:
    print("Enter positive number!!")