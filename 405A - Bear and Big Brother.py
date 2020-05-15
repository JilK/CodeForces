'''
Input
The only line of the input contains two integers a and b (1 ≤ a ≤ b ≤ 10) — the weight of Limak and the weight of Bob respectively.

Output
Print one integer, denoting the integer number of years after which Limak will become strictly larger than Bob.
'''

#Code

a= input().split()
Limak = int(a[0])
Bob = int(a[1])
year=0
while Limak<=Bob:
    Limak=3*Limak
    Bob=2*Bob
    year=year+1
print(year)
