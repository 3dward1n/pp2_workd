# 1 Generator kvadratov chisel do N
def sqкgen(n):
    for i in range(n+1):
        yield i**2

n_val=5
for sq in sqкgen(n_val):
    print(sq)

# 2 Programma dlya vyvoda chetnykh chisel cherez zapyatuyu
def evgen(n):
    for i in range(n+1):
        if i%2==0:
            yield str(i)

n_input=int(input("Vvedite n: "))
print(",".join(evgen(n_input)))

# 3 Funktsiya s generatorom dlya chisel, kratnykh 3 i 4
def div34(n):
    for i in range(n+1):
        if i%3==0 and i%4==0:
            yield i

for num in div34(50):
    print(num)

# 4 Generator squares ot (a) do (b) s tsiklom for
def squares(a,b):
    for i in range(a,b+1):
        yield i**2

a=3
b=7
for val in squares(a,b):
    print(val)

# 5 Generator dlya otscheta ot N vniz do 0
def countdown(n):
    while n>=0:
        yield n
        n-=1

for x in countdown(5):
    print(x)