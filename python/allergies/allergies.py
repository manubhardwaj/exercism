import operator

class Allergies(object):
    ALLERGIES = {
         'eggs': 1,
         'peanuts': 2,
         'shellfish': 4,
         'strawberries': 8,
         'tomatoes': 16,
         'chocolate': 32,
         'pollen': 64,
         'cats': 128
         }

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        return (self.score >= self.ALLERGIES[item])

    @property
    def lst(self):
        lst = []
        tmp_score = self.score
        for key,value in sorted(self.ALLERGIES.items(), key=operator.itemgetter(1)):
            if(tmp_score >= value):
                lst.append(key)
                tmp_score -= value
        return lst
