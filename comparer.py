
import sys

def checkout(component):
    print 'checkout'

def change(component):
    print 'change' 

def tag(component):
    print 'tag' 

def push(component):
    print 'push' 

def cleanFolder():
    print 'clean Folder'

def main():
    args = sys.argv

    file1 = open(args[1])
    lines1 = [line.rstrip('\n') for line in file1]

    file2 = open(args[2])
    lines2 = [line.rstrip('\n') for line in file2]

    count = 0
    buildOrder = []
    for line in lines1:
        if line.startswith('-'):
            print line
            count+= 1
            buildOrder.append([])
            continue

        if line not in lines2:
            print line
            buildOrder[count-1].append(line)

    buildOrder = filter(None, buildOrder)

    for buildStage in buildOrder:
        cleanFolder()
        print buildOrder.index(buildStage)
        for component in buildStage:
            checkout(component)
            change(component)
            tag(component)
            push(component)

        raw_input("Press Enter to continue...")

if __name__ == "__main__":
    main()