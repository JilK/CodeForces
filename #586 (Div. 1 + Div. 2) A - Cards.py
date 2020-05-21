#Code:

m= int(input())
s= str(input())
 
ones= s.count('n')
zeros= s.count('z')
ans= ones*' 1' + zeros*' 0'
print(ans.lstrip())
