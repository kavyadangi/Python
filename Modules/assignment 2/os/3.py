import os
path = "C:/Users/samak/Desktop/Python/Modules/Class Activity VIII/OS"
try:
    os.mkdir(path)
    print("Directory created successfully.")
except OSError as e:
    print("Failed to create directory:", e)
