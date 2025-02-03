from pprint import pprint
from graf import paths





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

    def set_cell(self,r,c,val):
        self.matr[r][c] = val

    def is_in_matr(self, row,col ):
        return row in range(self.rows) and col in range(self.cols)

    def get_all_paths(self):
        paths = set()
        return paths

if __name__ == "__main__":
    matr = Matr(3,4)
    matr.set_cell(3,0, None)
    matr.set_cell(3,2, None)
    matr.set_cell(3,1, '0')
    pprint(matr.matr)