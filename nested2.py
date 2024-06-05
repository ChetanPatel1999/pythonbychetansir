#wap to find greatest number btween three number.
num1=int(input("enter num1 : "))
num2=int(input("enter num2 : "))
num3=int(input("enter num3 : "))
if num1>num2 :
    if num1>num3:
        print(f"greatest num = {num1}")
    else:
        print(f"greatest num = {num3}")    
else:
   if num2>num3:
        print(f"greatest num = {num2}") 
   else:
        print(f"greatest num = {num3}")            
    