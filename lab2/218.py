n=int(input())
doramas={}
for i in range(n):
    dorama, amount=input().split()
    amount=int(amount)
    if dorama not in doramas:
        doramas[dorama]=amount
    else:
        doramas[dorama]+=amount
        
for key in sorted(doramas):
    print(f"{key} {doramas[key]}")     