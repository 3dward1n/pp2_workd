import re
import json

with open('raw.txt', 'r', encoding='utf-8') as f:
    text=f.read()

date_match=re.search(r'\d{2}\.\d{2}\.\d{4}', text)
time_match=re.search(r'\d{2}:\d{2}', text)

date=date_match.group(0) 
time=time_match.group(0) 

lines=text.split('\n')
products=[]
prices=[]
items=[]

for i in range(len(lines)):
    if ' x ' in lines[i]:
        name=lines[i-1].strip()
        if re.match(r'^\d+\.$', name):
            name=lines[i-2].strip()
        
        price_match=re.search(r'(\d+,\d{2})$', lines[i])
        if price_match:
            price_str=price_match.group(1).replace(',', '.')
            price_num=float(price_str)
            
            products.append(name)
            prices.append(price_num)
            items.append({"product_name": name, "price": price_num})
total_sum = sum(item["price"] for item in items)

result = {
    "data": {
        "date": date,
        "time": time
    },
    "items": items,
    "total_amount": round(total_sum, 2)
}

with open('receipt.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4)

