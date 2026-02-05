
a=int(input())
n=list(map(int, input().split()))
count=0
for i in range (a):
    if (n[i]>0):
        count+=1
print(count)
#204