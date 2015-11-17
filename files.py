#!/usr/bin/python

fo = open("testfile.txt","w");

def byebyefunction():
	print("Closing now...bye bye!\n");
	return;

print("Hello, I am blah");
str = raw_input("What's your name?");
print("Hello" + str + ", I will write a file for you");
fo.write("This is a message for " + str + "\n");
fo.write("Here are some numbers...\n");
for i in 'python' :
	fo.write(i);
	fo.write("\n");
byebyefunction();
fo.close();
