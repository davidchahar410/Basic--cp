# 10. WAP to accept a number from 1 to 7 and display the name of the day, like 1 for 
# Sunday, 2 for Monday, etc. 


day = int(input("Enter a number from 1 to 7: "))

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday") 
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    case 8:
        print("Invalid input")
