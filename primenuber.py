num=3
if num==0 or num==1:
    print("not prime")
else:    
  for i in range(2,num):
    if num%i==0:
        print("not prime number")
        break
  else:
    print("prime number")    