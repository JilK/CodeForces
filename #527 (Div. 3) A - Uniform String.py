#Code-

for i in range(int(input())):
    ab= input().split()
    a= int(ab[0])
    b= int(ab[1])
    letter=''
    ans=''
    for j in range(97, 97+b):
        letter= letter+chr(j)

    c= a//b
    d= a%b
    ans= c*letter + letter[0:d]
    print(ans)
