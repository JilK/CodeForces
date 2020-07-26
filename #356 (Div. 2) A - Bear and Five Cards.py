#Code;

cards = list(map(int, input().split()))

cards.sort()
test=[]
for i in cards:
    if cards.count(i)>1 and i not in test:
        test.append(i)
compare=0
check=0
number=0
if test==[]:
    print(sum(cards))
else:
    for i in test:
        compare= cards.count(i)*i
        check=max(check, compare)
        if check==compare:
            number=i
    x= cards.count(number)
    x=min(x,3)
    for j in range(int(x)):
        cards.remove(number)
    print(sum(cards))
