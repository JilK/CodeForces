#Code:

x= input()
test= list(map(int, input().split()))
count=sp=0
trial=[]
for i in test:
    while abs(i)!=1:
        if i<-1:
            count= count+ abs(i+1)
            i= -1
        elif i>1:
            count= count+ abs(i-1)
            i=1
        elif i==0:
            count= count+1
            i=1
            sp=sp+1
    trial.append(i)

x= trial.count(-1)
y= sp

if x%2==0 or (x+y)%2==0 or y>=2 and (x+y-1)%2==0 :
    print(count)
else:
    print(count+2)
