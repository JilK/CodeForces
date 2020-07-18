#Code:

s= str(input())
l= len(s)
test=[]
final=[]
new=''
for i in range(l):
    new= s[1:]+s[0]
    s=new
    test.append(new)
for i in test:
    if i not in final:
        final.append(i)

print(len(final))
