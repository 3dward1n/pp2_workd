a, b, c=map(int,input().split())
num=list(map(int, input().split()))
num[b-1:c]=num[b-1:c][::-1]
print (*num)