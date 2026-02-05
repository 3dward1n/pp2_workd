num={}
n=int(input())
arr=list(map(int, input().split()))
for x in arr:
    if x not in num:
        num[x]=1
    else:
        num[x]+=1
        
maxfreq=max(num.values())
arr=[]
for key in num:
    if maxfreq==num[key]:
        arr.append(key)
print(min(arr))

#214