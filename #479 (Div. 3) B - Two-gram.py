#Code:

l= int(input())

n= str(input())
i=j=0
maximum=0
ans=''
new_string=''
test=[]
while i<len(n)-1:
    string=''
    string= n[i]+n[i+1]
    new_string= new_string+ " "+string
    i=i+1
new_string= (new_string.lstrip())
while j<len(new_string)-1:
    final=''
    final= new_string[j]+new_string[j+1]
    y= new_string.count(final)
    maximum= max(maximum,y)
    if y==maximum:
        ans=final
    j=j+3

print(ans)
