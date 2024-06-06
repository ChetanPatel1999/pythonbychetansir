# match case 
# wap to print state name according to state short name.
state=input("enter a state short name :")
match state:
    case "mp" :print("madhya pradesh")
    case "up" :print("uttar pradesh")
    case "rj" :print("rajsthan")
    case _ :print("invalid short state name")
