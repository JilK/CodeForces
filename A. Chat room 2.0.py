str_main=input()

arr=list(str_main)

# print(arr)

hello=list("hello")
store=[]
for i in hello:
    if i in arr:
        save=arr.index(i)
        store.append(i)
        # print(save)
        arr=arr[save+1:]
        # print(arr)

save1="".join(store)
if save1=="hello":
    print("YES")
else:
    print("NO")
