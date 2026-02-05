n=int(input())
a=list(map(int,input().split()))
num=set()
for x in a:
    if x in num:
        print("NO")
    else:
        print("YES")
        num.add(x)