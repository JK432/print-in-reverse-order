# Write a program to print the content of a file in the reverse order
f=open("file1.txt","r")
s=f.read()
print(s[::-1])
