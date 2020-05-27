#Code -

p= input()
test=''
for i in range(int(p)):
    t=str(input())
    if str(t) in test:
        print("YES")
    else:
        print("NO") 
    test=test+t
