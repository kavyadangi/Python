import sys
limit=sys.getrecursionlimit()
print("Current recursion limit:", limit)
limit1=3000
sys.setrecursionlimit(limit1)
limit2=sys.getrecursionlimit()
print("Updated recursion limit:", limit2)
