#Write a Python program to reverse a string. 
#Sample String : "1234abcd"
string1="1234abcd"
print(reverse.string1())
for i in range(0, len(string1)/2, 1):
    t=string1[i]
    string1[i]=string1[len(string1)-i-1]
    string1[len(string1)-i-1]=t
print(string1)
