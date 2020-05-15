'''
Input
The first and the single line contains the set of letters. The length of the line doesn't exceed 1000. It is guaranteed that the line starts from an opening curved bracket and ends with a closing curved bracket. Between them, small English letters are listed, separated by a comma. Each comma is followed by a space.

Output
Print a single number — the number of distinct letters in Anton's set.
'''

#Code

a=str(input())
a= a.replace("{",'')
a= a.replace("}",'')
a= a.replace(",",'')
a= a.replace(" ",'')
 
b=''
for i in a:
    if i not in b:
        b=b+i
 
print(len(b))
