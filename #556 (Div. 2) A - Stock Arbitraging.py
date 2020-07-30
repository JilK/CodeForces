Code:

a,b,c= input().split()
buy= list(map(int,input().split()))
sell= list(map(int,input().split()))

buyat = min(buy)
buy.remove(buyat)
sellat= max(sell)

number= int(c)//buyat
money= int(c)- number*buyat

if buyat<sellat:
    ans= number*sellat + money
else:
    ans= c
print(ans)
