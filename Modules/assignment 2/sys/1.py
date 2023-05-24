import sys
name=sys.argv[0]
arguments=sys.argv[1:]
print("Script name:", name)
print("Arguments:", arguments)
if len(arguments) > 0:
    print("Arguments:")
    for arg in arguments:
        print(arg)
else:
    print("No arguments provided.")
