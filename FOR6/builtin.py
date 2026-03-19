from functools import reduce

data=[10, 20, 30, 40, 50]
names=["Apple", "Banana", "Cherry"]

res_map=list(map(lambda x: x * 10, data))
print(res_map)

res_filter=list(filter(lambda x: x > 25, data))
print(res_filter)

res_reduce=reduce(lambda x, y: x + y, data)
print(res_reduce)

for index, name in enumerate(names):
    print(index, name)

for name, val in zip(names, data):
    print(name, val)

val="100"
if isinstance(val, str):
    num = int(val)
    print(type(num), num)