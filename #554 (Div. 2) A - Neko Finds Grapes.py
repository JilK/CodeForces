#Code:

i= input().split()

a= int(i[0])

b= int(i[1])

chest=[1 for i in input().split() if int(i)%2==0]

key= [1 for i in input().split() if int(i)%2==0]

even_chest = len(chest)
even_key= len(key)

odd_chest= a-even_chest
odd_key= b-even_key

possible= min(even_chest, odd_key) + min(even_key,odd_chest)

print(possible)
