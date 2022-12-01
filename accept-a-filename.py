"""write a Python program to accept a filename from the user and print the extension of that"""
fn= input("Input the Filename: ")
f = fn.split(".")
print("The extension of the file is : " + f[-1])
