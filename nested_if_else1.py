#wap to check given number is even-positive or even-nagaitive 
#or odd-positive or odd-nagative.
num=int(input("enter a num :"))#9
if num==0:
    print("num is zero")
elif num%2==0:
    if num<0:
        print("even-nagative")
    else: 
        print("even-positive")  
else:
    if num<0:
        print("odd-nagative")
    else:
        print("odd-positive")    
