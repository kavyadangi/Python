import sys
sys.tracebacklimit=5
try:
    raise ValueError("This is a custom exception")
except ValueError as e:
    print("Caught an exception:", e)
    exc_type, exc_value, exc_traceback=sys.exc_info()
    traceback.print_tb(exc_traceback, limit=sys.tracebacklimit)
