#Code:

i= int(input())
j= str(input())

total=0
test=[]
for i in j:
    if i=='+':
        total= total+1
        test.append(total)
    else:
        total= total-1
        test.append(total)

number_of_stones=min(test)
number_of_stones=abs(min(number_of_stones,0))


minus= j.count('-')
plus= j.count("+")
 
total= (number_of_stones+ plus*1) - minus*1
 
print(total)
