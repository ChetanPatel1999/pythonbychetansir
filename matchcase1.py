# match case 
# wap to print day name according to number.
num=int(input("enter a num :"))
match num:
    case 1 :print("One")
    case 2 :print("Two")
    case 3 :print("Three")
    case 4 :print("thursday")
    case 5 :print("Friday")
    case 6 :print("saturday")
    case 7 :print("sunday")
    case _ :print("please enter one to seven")
