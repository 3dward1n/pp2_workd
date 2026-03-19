import shutil
import os

with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Line 1: Sample Data\nLine 2: Python Practice")

with open("sample.txt", "r") as f:
    print(f.read())

with open("sample.txt", "a") as f:
    f.write("\nLine 3: Appended Content")

with open("sample.txt", "r") as f:
    print(f.read())

shutil.copy("sample.txt", "backup_sample.txt")

if os.path.exists("sample.txt"):
    os.remove("sample.txt")