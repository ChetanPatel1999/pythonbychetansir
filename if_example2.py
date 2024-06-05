#if user press 1 so display "good morning"
#if press 2 disply "good afternoon"
#if press 3 display "good evning"
#if press 4 display "good night"
#if press any other number display "please press 1,2,3or4"
num=int(input("press any number :"))
if num==1:
   print("good morning")
if num==2:   
   print("good afternoon")
if num==3:   
   print("good evening")
if num==4:   
   print("good night")
if num>4 or num==0 or num<0:
   print("please press 1,2,3or4")
