#!/usr/bin/env python

import os
import sys

if len(sys.argv) > 2:
    arg1 = sys.argv[1]
    arg2 = sys.argv[2]
else:
    exit("Not enough parameters.")

for i in range (int(arg1), int(arg2)):
	numer = str(i)
	smallId = "p" + numer
	bigId = "P" + numer
	
	print(smallId)
	
	outputLines = []
	outputLines.append("")
	outputLines.append("#include \"stdafx.h\"")
	outputLines.append("")
	outputLines.append("class " + bigId)
	outputLines.append("")
	outputLines.append("{")
	outputLines.append("    int a;")
	outputLines.append("    int b;")
	outputLines.append("};")
	outputLines.append("")
	
	filename = smallId + ".cpp"
	
	outF = open(filename, 'w')
	for l in outputLines:
		outF.write(l + '\n')
	
	outF.close()
	
	
