Code :

s= str(input())

pearl= s.count("o")
link= s.count("-")
if link*pearl==0 or link%pearl==0:
    print("YES")
else:
    print("NO")
