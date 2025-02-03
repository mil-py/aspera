from pprint import pprint
from graf import paths

class PhoneTablo():
    def __init__(self):
        self.tablo = {
            (0, 0): "1",
            (0, 1): "2",
            (0, 2): "3",
            (1, 0): "4",
            (1, 1): "5",
            (1, 2): "6",
            (2, 0): "7",
            (2, 1): "8",
            (2, 2): "9",
            (3, 1): "0"
        }
        self.rows = 4
        self.cols = 3

    def hody(self, pin):
        return [
            (pin[0]  - 1, pin[1]+2),
            (pin[0] - 1, pin[1] - 2),
            (pin[0] + 1, pin[1] + 2),
            (pin[0] + 1, pin[1] - 2),
            (pin[0] - 2, pin[1] + 1),
            (pin[0] - 2, pin[1] - 1),
            (pin[0] + 2, pin[1] + 1),
            (pin[0] + 2, pin[1] - 1),
                ]




class Matr:
    def __init__(self,cols,rows):
        i = 1
        self.cols = cols
        self.rows = rows
        self.matr =[]
        i =1
        for r in range(rows):
            row = []
            for c in range(cols):
                row.append(str(i))
                i+=1
            self.matr.append(row)

    def set_cell(self,c,r,val):
        self.matr[r][c] = val

    def is_in_matr(self, col, row):
        return row in range(self.rows) and col in range(self.cols)

    def get_all_paths(self):
        paths = set()
        return paths

if __name__ == "__main__":
    matr = Matr(3,4)
    matr.set_cell(0,3, None)
    matr.set_cell(2,3, None)
    matr.set_cell(1,3, '0')
    pprint(matr.matr)