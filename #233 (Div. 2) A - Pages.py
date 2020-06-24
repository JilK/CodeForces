#Code:

x= input().split()
n= int(x[0])
p= int(x[1])
k= int(x[2])
 
max_limit=min(n, p+k)
min_limit= max(1, p-k)
ans=''
for i in range(min_limit, max_limit+1):
    ans= ans+ ' '+str(i)
if ans.count(str(p))==1:
    ans= ans.replace(str(p), "("+str(p)+")")

else:
    temp= ans[:98]
    temp2= ans[98:]
    temp= temp.replace(str(p), "("+str(p)+")")
    ans = temp +temp2

 
if int(min_limit)!=1:
    ans= '<<'+ans
if int(max_limit)!=n:
    ans= ans+" "+'>>'
 
print(ans.lstrip())
