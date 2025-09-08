# Ques 7: 
# n = 5 
# * * * * * 
# * * 
# * * 
# * * 
# * * * * * 


n = 5
for i in range(n):
    if i == 0 or i == n - 1:
        print("* " * n)
    else:
        print("* " * 2)
