import re

with open('raw.txt', 'r', encoding='utf-8') as f:
    text=f.read()

date=re.search(r'\d{2}\.\d{2}\.\d{4}', text)
time=re.search(r'\d{2}:\d{2}', text)

date=date.group(0) 
time=time.group(0) 

lines=text.split('\n')
products=[]
prices=[]

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

total_sum = sum(item["price"] for item in items)

result = {
    "data": {
        "date": date.group(0) ,
        "time": time.group(0) ,
        "payment_method": payment
    },
    "items": items,
    "total_amount": round(total_sum, 2)
}

with open('receipt.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, indent=4)
