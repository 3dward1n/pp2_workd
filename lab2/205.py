n=int(input())
def ist(n):
    return n>0 and n&(n-1)==0
if (ist(n)):
    print("YES")
else:
    print("NO")
#205