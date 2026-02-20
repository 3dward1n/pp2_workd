print(bool("Hello"))
print(bool(18))
#true both

name=input()
if name:
    print("Hi!")
#checks if there are some information

bool(False)
bool(None)
bool(0)
bool("")
bool(())
bool([])
bool({})
#this all false

x = 200
print(isinstance(x, int))
#true because x is integer

x = "ацфвцф"
print(isinstance(x, int))