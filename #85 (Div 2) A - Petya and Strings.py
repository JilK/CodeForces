# Code:

s1= str(input())
s2= str(input())
s1= s1.lower()
s2= s2.lower()
i=0
j=0
while s1[i]==s2[i] and i<len(s1)-1:
        i=i+1
if s1[i]>s2[i]:
    print('1')
elif s1[i]<s2[i]:
    print("-1")
else:
    print("0")
