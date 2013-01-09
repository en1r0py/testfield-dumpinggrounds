import sys
import math

def printPaths():
    print sys.path


def buildConnectionString(params):
    """Build a connection string from a dictionary of parameters"""

    return ";".join([("%s=%s") % (k,v) for k,v in params.items()])

def someRandomListStuff():
    li = []
    li.append("a")
    li.extend(["a"])
    print li
    if "b" in li:
        print "b in li"
    else:
        print "no b in cli"

    li.remove("a")
    print li * 3

def someRandomTupleStuff():
    t = ('a','b','c','a')
    print t
    print t.index("a")
    print t.index('b')

def someRandomStringStuff():
    s = "%2.98f" % math.pi
    print s
    print len(s)
    li = range(1,101)
    fs = ",".join(["%s" % e for e in li])
    print fs

def someMoreRandomStringStuff():
    s = "this is a strange sentence, and that's, the, only one, I really need"
    li = s.split(",")
    print li
    print len(li)




if __name__ == '__main__':
    myParams = {"server":"mpilgrim",\
                "database":"master",\
                "uid":"sa",\
                "pwd":"secret"\
                }

    #print buildConnectionString(myParams)
    #printPaths()
    someMoreRandomStringStuff()
