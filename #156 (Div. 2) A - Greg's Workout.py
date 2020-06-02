#Code:

ab = input()

array= list(map(int,input().split()))
c=bi=back=i=0
while i<len(array):
    if i<len(array):
        c=c+array[i]
        i=i+1
    if i<len(array):
        bi=bi+array[i]
        i=i+1
    if i<len(array):
        back=back+array[i]
        i=i+1

ans= max(c,bi,back)
if ans==c:
    print("chest")
if ans==bi:
    print("biceps")
if ans==back:
    print("back")

