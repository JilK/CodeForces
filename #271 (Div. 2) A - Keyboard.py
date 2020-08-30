#Code:

st= 'qwertyuiopasdfghjkl;zxcvbnm,./'
d= str(input())
s= str(input())
ans=''
if d=='R':
    for i in s:
        x= st.find(i)
        ans= ans+st[x-1]
    print(ans)
else:
    for i in s:
        x= st.find(i)
        ans=ans+st[x+1]
    print(ans)
