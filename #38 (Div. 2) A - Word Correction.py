#Code - 

vowel= ['a','e','i','o','u','y']
n= int(input())
s= str(input())
ans=s[0]
i=1
while i <len(s):
    if s[i] not in vowel:
        ans= ans+s[i]
    elif s[i] in vowel and ans[-1] not in vowel:
        ans= ans+s[i]
    i=i+1

print(ans)
