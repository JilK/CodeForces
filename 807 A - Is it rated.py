#Code:

k=0
test=[]
for i in range(int(input())):
    rating= input().split()
    if int(rating[0])!=int(rating[1]):
        k=1
    test.append(int(rating[0]))

lala=test[:]
lala.sort(reverse= True)

if k==1:
    print("rated")
elif test==lala:
    print("maybe")
else:
    print("unrated")
