#multiple object ,formate method,fstring,formate specifire
name='chetan'
rno=1001
per=90.67
ch='c'
print('name of student : ',name,"\nrno of student : ",rno,"\npercent of student :",per)
print("name of std :{} \nrno of std :{}\npercent of std :{}".format(name,rno,per))
print("name of std :{a} \nrno of std :{b}\npercent of std :{c}".format(a=name,b=rno,c=per))
print(f"name of std :{name} \nrno of std :{rno}\npercent of std :{per}")
#formate specifire
print("name of std :%s \nrno of std :%d\npercent of std :%.2f"%("aman",rno,per))
print("name= %s"%name)
print('vale of ch = %c'%ch)
print('65 is ascci code of %c'%65)
print('name of student : ',name)
print('rno of student : ',rno)
print('per of student : ',per)
