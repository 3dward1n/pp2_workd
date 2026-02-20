i = 1
while i < 6:
  print(i)
  i += 1


  ####

i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

  ####

i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6") # +else

  #####

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue #skips "banana"
  print(x) 

#####

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)