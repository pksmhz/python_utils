import re
import sys


def format_value(input_value):
    result = input_value.rstrip()
    result = result[1:-1]
    result = result.replace("'", "\\'")
    result = "'" + result + "'"
    return result


inputFile = None
outputFile = None
lineToWrite = None

print("using arguments: {}".format(sys.argv))
if len(sys.argv) > 2:
    inputFile = sys.argv[1]
    outputFile = sys.argv[2]
else:
    exit("Not enough parameters.")

if not inputFile and not outputFile:
    exit("Bad parameters.")

inF = open(inputFile)
outF = open(outputFile, "w")

count = 0

for line in inF:
    count += 1
    match = re.search(r'(.*)(".*":).*(".*")', line)
    if match:
        beginning_of_the_line = match.group(1)
        first = match.group(2)
        second = match.group(3)
        first = format_value(first)
        second = format_value(second)
        outputLine = "{}{}: {}".format(beginning_of_the_line, first, second)
        lineToWrite = outputLine + "\n"
    else:
        lineToWrite = line
    outF.write(lineToWrite)

# Closing files
inF.close()
outF.close()
