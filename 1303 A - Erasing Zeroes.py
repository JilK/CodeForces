#Code;

for i in range(int(input())):

    s= str(input())
    try:
        x= s.index('1')

        y= s[::-1].index('1')
        y= len(s)-y
        new= s[x:y]
        print(new.count('0'))
    except:
        print(0)
