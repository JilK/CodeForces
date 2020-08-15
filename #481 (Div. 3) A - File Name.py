#Code:

n= int(input())
s= str(input())

i=0
c=0
while 'xxx' in s:
    c= c+ s.count('xxx')
    s= s.replace('xxx','xx')
print(c)
