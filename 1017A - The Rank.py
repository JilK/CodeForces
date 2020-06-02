#Code:

score=[]
for i in range(int(input())):
    a = sum(list(map(int , input().split())))
    score.append(a)

thomas= score[0]
score.sort(reverse=True)
rank= score.index(thomas)
print(rank+1)
