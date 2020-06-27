#Code:

s= str(input())

plus= s.find('+')
equal=s.find("=")
first= (s[:plus]).count('|')
second= (s[plus+1:equal]).count('|')
third= (s[equal+1:]).count('|')
if int(first)+int(second)==int(third):
    print( int(first)*"|" + "+" + int(second)*"|" + "=" + int(third)*"|"   )
elif int(first)+1+int(second)==int(third)-1:
    first= int(first)+1
    third= int(third)-1
    print( int(first)*"|" + "+" + int(second)*"|" + "=" + int(third)*"|"   )

elif int(first)+int(second)-1==int(third)+1:
    if int(first)!=1:
        first= int(first)-1
    else:
        second= int(second)-1
    third= int(third)+1
    print( int(first)*"|" + "+" + int(second)*"|" + "=" + int(third)*"|"   )

else:
    print("Impossible")
