import sys
print("Original sys.path:")
for path in sys.path:
    print(path)
sys.path.append("C:/Users/kavya/Desktop/Python/Modules/Class Activity VIII/Sys/New")
print("\nsys.path after appending a directory:")
for path in sys.path:
    print(path)
sys.path.remove("C:/Users/kavya/Desktop/Python/Modules/Class Activity VIII/Sys/New")
print("\nsys.path after removing a directory:")
for path in sys.path:
    print(path)
sys.path.insert(0, "C:/Users/kavya/Desktop/Python/Modules/Class Activity VIII/Sys/New")
print("\nsys.path after inserting a directory:")
for path in sys.path:
    print(path)
