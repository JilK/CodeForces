#Code:

a= input().split()
stores=int(a[0])
kgs=int(a[1])
test=[]
for i in range(stores):
    x= input().split()
    test.append( (int(x[0])/int(x[1]) )*kgs )
print(min(test))
