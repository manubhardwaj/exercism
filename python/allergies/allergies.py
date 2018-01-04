import operator

class Allergies(object):
    ALLERGIES = [
         'eggs', # 1,
         'peanuts', # 2,
         'shellfish', # 4,
         'strawberries', # 8,
         'tomatoes', # 16,
         'chocolate', # 32,
         'pollen', # 64,
         'cats' # 128
        ]

    def __init__(self, score):
        self.score = score

    def is_allergic_to(self, item):
        try:
            index = self.ALLERGIES.index(item)
        except ValueError:
            return True

        allergy_list = str("{0:b}".format(self.score))
        if(len(allergy_list) <= index):
            return False

        return (int(allergy_list[index]) != 0)


    @property
    def lst(self):
        lst = []
        for i in self.ALLERGIES:
            if(self.is_allergic_to(i)):
                    lst.append(i)
        return lst
