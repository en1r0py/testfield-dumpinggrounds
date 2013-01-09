import os
import sys
from UserDict import UserDict

class MyScum(UserDict):
    def __init__(self, NameOfTheScum):
        UserDict.__init__(self)
        self["NameOfTheScum"] = NameOfTheScum


if __name__ == "__main__":
    myscum = MyScum("Blah")

    for k,v in myscum.items():
        print k,v



