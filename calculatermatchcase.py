#make a calculater
print("""welcome to my calculater...
press 1 for convert weight kg into gram
press 2 for sub
press 3 for mul
press 4 for div
press 5 for exit...""")
num=int(input("please press num :"))
match num:
    case 1:
        kg=eval(input("enter weight in kg :"))
        gram=kg*1000
        print("weight in gram :",gram)
        if gram>5000:
            print("wow you gained above 5000 gram weight")
        else:
            print("sorry yoyre weight is less than 5000")

    case 2:
        a=int(input("enter frist num :"))
        b=int(input("enter second num :"))
        sub=a-b
        print(f"{a} - {b} = {sub}")
    case 3:
        a=int(input("enter frist num :"))
        b=int(input("enter second num :"))
        mul=a*b
        print(f"{a} * {b} = {mul}")
    case 4:
        a=int(input("enter frist num :"))
        b=int(input("enter second num :"))
        div=a/b
        print(f"{a} / {b} = {div}")
    case 5:pass   
    case _ :print("please enter 1 to 5")    
        


