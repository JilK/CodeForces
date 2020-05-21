#Code:

def function(s):
    if s.endswith('o'):
        print("FILIPINO")
    elif s.endswith('u'):
        print("JAPANESE")
    else:
        print("KOREAN")
 
 
m= int(input())
i=0
while i<m:
    s= str(input())
    function(s)
    i=i+1
