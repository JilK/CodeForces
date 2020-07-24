#Code:

vowel=['a','e','i','o','u']

s= str(input())
s=s+" "
i=0
k=0
if len(s[:-1])>1:
    while i<len(s):
        if s[i]=='n' or s[i]==str(" "):
            k=0
        elif s[i] not in vowel and s[i+1] not in vowel:
            k=1
            break
        i=i+1
else:
    if s[0] not in vowel and s[0]!='n':
        k=1

if k==0:
    print("YES")
else:
    print("NO")
