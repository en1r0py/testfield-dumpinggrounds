import os
import sys
from UserDict import UserDict

def stripnulls(data):
    return data.replace("\00","").strip()

class FileInfo(UserDict):
    def __init__(self, filename=None):
        UserDict.__init__(self)
        self["name"] = filename


class MP3FileInfo(FileInfo):
    tagDataMap = {  "title"     : (3, 33, stripnulls),
                  "artist"  : (33, 63, stripnulls),
                  "album"   : (63, 93, stripnulls),
                  "year"    : (93, 97, stripnulls),
                  "comment" : (97, 126, stripnulls),
                  "genre"   : (127, 128, ord)}

    def __parse(self, filename):
        self.clear()
        try:
            fsock = open(filename, "rb", 0)
            try:
                fsock.seek(-128, 2)
                tagdata = fsock.read(128)
            finally:
                fsock.close()

            if tagdata[:3] == "TAG":
                for tag, (start, end, parseFunc) in self.tagDataMap.items():
                    self[tag] = parseFunc(tagdata[start:end])
        except IOError:
            pass

    def __setitem__(self, key, item):
        if key == "name" and item:
            self.__parse(item)
            FileInfo.__setitem__(self, key, item)

def listDirectory(directory, fileExtList):
    fileList = [os.path.normcase(x) for x in os.listdir(directory)]
    fileList = [os.path.join(directory, x) for x in fileList if os.path.splitext(x)[1] in fileExtList]

def getFileInfoClass(filename, module=sys.modules[FileInfo.__module__]):
    subclass = "%sFileInfo" % os.path.splitext(filename)[1][1:].upper()
    return hasattr(module, subclass) and getattr(module, subclass) or FileInfo



if __name__ == "__main__":

    getFileInfoClass(



#
#    bloke = MP3FileInfo()
#    print "Here"
#    bloke["name"] = "Fuzzbug"
#
#    print repr(bloke)
#
#    mylist = hmm_listDirectory("/home/spacecrafty",".vim")
#    print mylist
#



















