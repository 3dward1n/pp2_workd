
a=int(input())
prime=True
i=2
while (i<a):
  if (a%i==0):
    prime=False
  i+=1
if (prime):
  print("Yes")
else:
  print("No")
#213