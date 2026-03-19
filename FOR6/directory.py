import os
import shutil

os.makedirs("parent/child/grandchild", exist_ok=True)

items=os.listdir(".")
print(items)

txt_files=[f for f in os.listdir(".") if f.endswith(".txt")]
print(txt_files)

if os.path.exists("backup_sample.txt"):
    shutil.move("backup_sample.txt", "parent/backup_sample.txt")