#Code:

a = (input()).split()
two= int(a[0])
three= int(a[1])
five = int(a[2])
six = int(a[3])
total=0
d= min(two, five,six)
total = d*256
two= two-d
e= min(two,three)
total= total + e*32
print(total)
