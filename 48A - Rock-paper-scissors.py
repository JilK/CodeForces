#Code:

l=[]
for i in range(3):
    l.append(str(input( )))

x=l[:]
x= set(x)

if len(x)!=2:
    print("?")
else:
    if l[1]==l[2] and l[0]!=l[1]:
        if l[1]== 'rock' and l[0]=='paper' or l[1]=='paper' and l[0]=='scissors' or l[1]=='scissors' and l[0]=='rock':
            print("F")
        else:
            print("?")
    elif l[1]==l[0] and l[0]!=l[2]:
        if l[1]== 'rock' and l[2]=='paper' or l[1]=='paper' and l[2]=='scissors' or l[1]=='scissors' and l[2]=='rock':

            print("S")
        else:
            print("?")
    elif l[2]==l[0] and l[0]!=l[1]:
        if l[0]== 'rock' and l[1]=='paper' or l[0]=='paper' and l[1]=='scissors' or l[0]=='scissors' and l[1]=='rock':

            print("M")
        else:
            print("?")
