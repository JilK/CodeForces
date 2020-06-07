#Code:

i= int(input())
l= (i+1)//2

j=0

k=i//2
while j<l:
    print( k *'*'+ (2*j + 1)  *'D'+  k *'*'   )
    k=k-1
    j=j+1
k=k+2
j=j-2
while j>=0:
   print( k *'*'+ (2*j + 1)  *'D'+  k *'*'   ) 
   k=k+1
   j=j-1
