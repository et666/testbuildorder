
import sys

args = sys.argv
print args

file1 = open(args[1])
lines1 = [line.rstrip('\n') for line in file1]

file2 = open(args[2])
lines2 = [line.rstrip('\n') for line in file2]

for line in lines1:
    if line.startswith('-'):
        print line
        continue

    if line not in lines2:
        print line        