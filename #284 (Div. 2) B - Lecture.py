#Code:

a,b= input().split()

di={}
for i in range(int(b)):
    s= input().split()
    i= s[0]
    if len(s[0])<=len(s[1]):
        j=s[0]
    else:
        j=s[1]
    di.update({i:j})

st= input().split()
for i in st:
    print(di[i], end= " ")
