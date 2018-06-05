
import sys, re
import git
from time import gmtime, strftime

def findHighestTag(component):
    print 'findHighestTag'
    repo = git.Repo(component)
    tags = sorted(repo.tags, key=lambda t: t.commit.committed_datetime)
    latest_tag = tags[-1]
    return str(latest_tag)

def getNewerTag(component):
    tag = findHighestTag(component)

    print 'Old Tag was: ' + tag
    p = re.compile('v(\d*).(\d*).(\d*)')
    erg = p.findall(tag)
    if erg[0][0] == '0':
        return 'v1.0.0'
    #increase patch
    patch = int(erg[0][2]) + 1
    return 'v' + erg[0][0] + '.' + erg[0][1] + '.' + str(patch)

def checkout(component):
    print 'checkout'

def changeAndCommit(component):
    file = open(component + '/text.txt', 'w')
    file.write(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
    file.close()
    obj = git.Repo(component)
    obj.index.commit("Automatic Commit")

    print 'changeAndCommit' 

def tag(component):
    newTag = getNewerTag(component)
    obj = git.Repo(component)
    obj.create_tag(newTag)
    print 'New Tag is: ' + newTag
    return newTag

def push(component, tag):
    obj = git.Repo(component)
    obj.remotes.origin.push()

    #obj.origin.push("origin", "HEAD:refs/for/master")

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
            changeAndCommit(component)
            tagstr = tag(component)
            push(component, tagstr)

        raw_input("Press Enter to continue...")

if __name__ == "__main__":
    main()