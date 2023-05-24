import os
new = "C:/Users/kavya/Desktop/Python/Modules/Class Activity VIII/OS/New"
try:
    os.chdir(new)
    print("Current working directory changed to:", new)
except OSError as e:
    print("Failed to change current working directory:", e)
