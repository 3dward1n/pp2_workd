
a=int(input())
n=list(map(int, input().split()))
count=0
mx=n[0]
for i in range (a):
    if (n[i]>mx):
        mx=n[i]
print(mx)
#206