import time
current = time.localtime()
print("Current time before sleep:", time.strftime("%Y-%m-%d %H:%M:%S", current))
time.sleep(5)
current = time.localtime()
print("Current time after sleep:", time.strftime("%Y-%m-%d %H:%M:%S", current))
