#Code:

a= input().split()
limit= int(a[1])

skills= list(map(int, input().split()))
length= len(skills)


i=0

while skills[0]<=limit and len(skills)>1:
    skills.remove(skills[0])
    i=i+1

skills.reverse()

while skills[0]<=limit and len(skills)>1:
    skills.remove(skills[0])
    i=i+1
if skills[0]<=limit:
    i=i+1
print(i)
