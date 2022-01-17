# 22 September 2021
l = [90,5,8,3,41,25,96,75,120,130,121,12,1]

ans = l[0]
maxnum = l[0]
for i in l:
    if i >= maxnum:
        ans = maxnum
        maxnum = i
    elif i > ans:
        ans = i

print(ans)
