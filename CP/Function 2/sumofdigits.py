n=int(input("Enter your digit : "))
sum=0
while(n!=0):
    rem=n%10
    sum+=rem
    n=n//10
print("The sum of the digit ",n," is : ",sum)