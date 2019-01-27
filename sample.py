""" a class to be tested """

class Grid:
    def __init__(self, valuelist=None, validlist=None):
        if valuelist:
            self.value = valuelist
        else:
            self.value = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        if valuelist:
            self.valid = validlist
        else:
            self.valid = [False, False, False, False, False, False, False, False, False]

    def __repr__(self) -> str:
        i = 0
        rslt = ''
        for value, isvalid in zip(self.value, self.value):
            if i % 3 == 0:
                rslt += '\n'
            if isvalid:
                rslt += '%d ' % value
            else:
                rslt += '* '
            i += 1
        return rslt

    def is_valid(self) -> bool:
        checklist = [0]*10
        sums = 0
        for item in self.value:
            checklist[item] += 1
            sums += item
        if sums != 45:
            return False
        for item in checklist[1:]:
            if item != 1:
                return False
        return True

# end of file
