#Code:

for i in range(int(input())):
 
    st= str(input())
    test=[]
    for i in range(ord(min(st)),ord(max(st))+1):
        test.append(i)
    string=[]
    for j in st:
            string.append(ord(j))

    final=[]
    for i in string:
        if i not in final:
            final.append(i)

    if sum(test)==sum(final) and len(string)==len(test):
        print("YES")
    else:
        print("NO")
