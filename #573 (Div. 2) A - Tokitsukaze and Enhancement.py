#Code:

p= int(input())
q= str(p%4)
r= str((p+1) %4)
s= str((p+2) % 4)
array=''
array= q+r+s
if str(1) in array:
    e= array.find('1')
    print(e,'A')
elif str(3) in array:
    e= array.find('3')
    print(e,'B')
elif str(2) in array:
    e= array.find('2')
    print(e,"C")
else:
    print(0,'D')
