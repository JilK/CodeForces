'''
Input
First line of the input contains a single integer n (1 ≤ n ≤ 2·105), the length of the string that Andreid has.

The second line contains the string of length n consisting only from zeros and ones.

Output
Output the minimum length of the string that may remain after applying the described operations several times.
'''

#The completed code

m=int(input())
 
s= str(input())
 
print(abs(s.count('1')- s.count('0')))
