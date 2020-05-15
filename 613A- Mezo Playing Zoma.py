'''
Input
The first line contains n (1≤n≤105) — the number of commands Mezo sends.

The second line contains a string s of n commands, each either 'L' (Left) or 'R' (Right).

Output
Print one integer — the number of different positions Zoma may end up at.
'''

#Code


m=int(input())
 
s= str(input())
 
print((s.count('L')+s.count('R'))+1)
