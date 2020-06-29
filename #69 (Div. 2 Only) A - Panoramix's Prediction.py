#Code:

prime= [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53]

x= input().split()
a=int(x[0])
b=int(x[1])
if a not in prime or b not in prime:
    print("NO")
else:
    pos1= prime.index(a)
    pos2= prime.index(b)
    if pos2-pos1==1:
        print("YES")
    else:
        print("NO")
