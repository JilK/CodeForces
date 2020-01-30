#Input
#The first line of the input contains one integer t (1≤t≤100) — the number of test cases.

#The next n lines describe test cases. The i-th test case is given on a new line as one integer n (2≤n≤109).

#Output
#For each test case, print the answer on it. Print "NO" if it is impossible to represent n as a⋅b⋅c for some distinct integers a,b,c such that 2≤a,b,c.

#Otherwise, print "YES" and any possible such representation.


t = int(input())
for i in range(t):
	l = []
	n = int(input())
	for i in range(2,n):
		if n%i == 0:
			l.append(i)
			n /= i
		if len(l) == 2 or i*i>n:
			break
	if len(l) == 2 and n!=l[0] and n!= l[1] and n>1:
		print("YES")
		print(l[0],l[1],int(n))
	else:
		print("NO")