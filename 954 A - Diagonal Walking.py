#Code:

import re
n= int(input())
x= str(input())
ans = n-len(re.findall('RU|UR',x))
print(ans)
