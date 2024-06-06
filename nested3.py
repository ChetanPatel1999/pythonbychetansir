#nested 
age=int(input("enter your age : "))
if age>=18:
    print("please come in my clube ")
    print("clube menu : ")
    print("pasta : 140")
    print("momos : 100")
    print("moctal : 200")
    order=input("please order :") 
    if order=="pasta":
        print("pasta order is done plese pay 140")
    elif order=="momos":
         print("momos order is done plese pay 100")
    elif order=="moctal":
        print("moctal order is done plese pay 200")
    else:
        print("plese meme order somthing")            
    
else:
    print("sorry to say you age belove 18")
      