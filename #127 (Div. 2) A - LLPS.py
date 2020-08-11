#Code:

s= str(input())
ans= ''
for i in s:
    ans= max(ans,i)
print(s.count(ans) *ans)
