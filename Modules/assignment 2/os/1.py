import os
f = "file.txt"
if os.path.exists(f):
    print("File exists.")
else:
    print("File does not exist.")
