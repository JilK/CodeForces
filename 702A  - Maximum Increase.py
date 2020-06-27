#Code:

n= int(input())

test= list(map(int, input().split()))
i=count=0
option=[0]
while i<n-1:
    try:
        while (test[i]<test[i+1])  and i<n-1:
            count=count+1
            i=i+1
            option.append(count)
    except:
        break

    count=0

    i=i+1
print(max(option)+1)
