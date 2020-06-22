#Code:

from statistics import mean
import math

for i in range(int(input())):
    n= int(input())
    numbers= list(map(int, input().split()))
    print(math.ceil(mean(numbers)))
