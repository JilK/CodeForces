#Code:

crystal = input().split()
y_c = int(crystal[0])
b_c= int(crystal[1])

balls= input().split()
yellow=int(balls[0])
green= int(balls[1])
blue=int(balls[2])

need_yellow= 2*yellow + green
need_blue= green + 3*blue

ans_yellow=ans_blue=0
if y_c<need_yellow:
    ans_yellow= need_yellow - y_c
if b_c< need_blue:
    ans_blue= need_blue - b_c

print(ans_yellow + ans_blue)
