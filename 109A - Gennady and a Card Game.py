#Code:

card= str(input())
hand= str(input())
 
rank=card[0]
suit= card[1]
if rank in hand or suit in hand:
    print("YES")
else:
    print("NO")
