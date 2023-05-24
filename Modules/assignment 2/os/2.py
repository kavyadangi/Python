import os
f="file.txt"
try:
    size=os.path.getsize(f)
    sizekb=size/1024
    print("File size:", sizekb, "KB")
except OSError as e:
    print("Failed to get file size:", e)
