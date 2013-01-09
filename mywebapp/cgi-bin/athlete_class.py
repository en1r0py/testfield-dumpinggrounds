class Athlete(list):
    def __init__(self, a_name, a_dob, a_times):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set(self))[:3]

    def test(self):
        print self.name
        print self.dob
        print self

