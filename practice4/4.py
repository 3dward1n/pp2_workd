import json
import math as m
with open("41.json", "r", encoding="utf-8") as f:
    use = json.load(f)
a=use["a"]
b=use["b"]
prmtr=(a+b)*2
p1=prmtr/3
print(f"perimeter={prmtr}")
print(p1)
print(m.ceil(p1))
res={"perimeter": prmtr,"p1_raw": p1,"p1": m.ceil(p1)}
with open("result.json", "w", encoding="utf-8") as fout:
    json.dump(res, fout)
