a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

#also shorter
b=input()
if b=="ibm": print("it")

a="company"
b="kompany"
print ("K") if b=="kompany" else print("not k") if a==b else print ("AB") #chain

age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")  #nested if statements

  