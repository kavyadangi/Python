import sys
sys.stdout = open("output.txt", "w")
sys.stderr = open("error.txt", "w")
sys.stdin = open("input.txt", "r")
print("Hello, redirected stdout!")
print("Hello, redirected stderr!", file=sys.stderr)
input_data = sys.stdin.readline().strip()
print("Input from redirected stdin:", input_data)
sys.stdout = sys.__stdout__
sys.stderr = sys.__stderr__
sys.stdin = sys.__stdin__
print("Hello, original stdout!")
print("Hello, original stderr!", file=sys.stderr)
input_data = input("Enter input from original stdin: ")
print("Input from original stdin:", input_data)
