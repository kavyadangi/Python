import sys
module = 'math'
if module in sys.modules:
    print("Module", module, "has been imported.")
else:
    print("Module", module, "has not been imported.")
