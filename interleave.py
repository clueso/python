#!/usr/bin/python

Option2File = open("Option2.txt", "r");
DirFile = open("dir.txt","r");
CodeFile = open("Code.txt","r");
OutputFile = open("Output.txt","w");

for Optline in Option2File:
	DirLine = DirFile.readline();
	CodeLine = CodeFile.readline();
	OutputFile.write(Optline);
	OutputFile.write("\t"+DirLine);
	OutputFile.write("\t"+CodeLine);
	OutputFile.write("</Option2>\n");
	


Option2File.close();
DirFile.close();
CodeFile.close();
OutputFile.close();
