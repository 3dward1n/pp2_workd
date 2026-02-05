
a=int(input())
n=list(map(int, input().split()))
n.sort()
n.reverse()
for i in range (a):
    print(n[i])