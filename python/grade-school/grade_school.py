class School(object):
    def __init__(self, name):

        self.school = name
        self.roster = dict()

    def add(self, student, grade):
        self.roster.setdefault(grade, []).append(student)

    def grade(self, grade):
        return self.roster.get(grade, [])

    def sort(self):
        return [(k, tuple(sorted(self.roster[k]))) for k in sorted(self.roster.keys())]
