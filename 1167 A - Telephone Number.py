#Code:

for i in range(int(input())):
    n= int(input())
    s= str(input())
    if '8' in s:
        x= s.index('8')
        x=s[x:]
        if len(x)>=11:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
