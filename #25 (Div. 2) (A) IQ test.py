'''

A word or a sentence in some language is called a pangram if all the characters of the alphabet of this language appear in it at least once. Pangrams are often used to demonstrate fonts in printing or test the output devices.

You are given a string consisting of lowercase and uppercase Latin letters. Check whether this string is a pangram. We say that the string contains a letter of the Latin alphabet if this letter occurs in the string in uppercase or lowercase.

Input
The first line contains a single integer n (1 ≤ n ≤ 100) — the number of characters in the string.

The second line contains the string. The string consists only of uppercase and lowercase Latin letters.

Output
Output "YES", if the string is a pangram and "NO" otherwise.
'''

# Complete the code below.
 
total=0
n= int(input())
a= [int(1) if int(x)%2==0 else int(2) for x in input().split()]
 
p= a.count(1)
q = a.count(2)
if q<p:
    print(a.index(2)+1)
else:
    print(a.index(1)+1)
