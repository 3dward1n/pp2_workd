import os
import shutil
from functools import reduce

all_files=[f for f in os.listdir("sales") if f.endswith(".txt")]
prod=[]



for file_name in all_files:
    file_path=os.path.join("sales",file_name)
    with open(file_path,"r",encoding="utf-8") as f:
        for line in f:
            if "," in line: 
                name,qty=line.strip().split(",")
                prod.append((name,int(qty)))


if prod:
    qant=[p[1] for p in prod]
    total_records=len(prod)
    total_qty=sum(qant)
    max_sale=max(qant)
    min_sale=min(qant)
    popular_products=list(filter(lambda p:p[1]>5,prod))
    product_of_all=reduce(lambda x,y:x*y,qant)


    avg_qty=total_qty/total_records
    
    with open("sales_report.txt","w",encoding="utf-8") as report:
        report.write(f"Total records:{total_records}\n")
        report.write(f"Average:{avg_qty:.1f}\n")
        report.write(f"Highest:{max_sale}\n")
        report.write(f"Lowest:{min_sale}\n")
        report.write("\nPopular prod:\n")
        for name,qty in popular_products:
            report.write(f"{name} {qty}")