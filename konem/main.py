import time
from pprint import pprint
from turtledemo.penrose import start

from graf import paths

class Matr2Graph:
    def __init__(self, matr):
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
        self.rows = len(matr)
        self.cols = max([len(arr) for arr in matr])
        self.matr = matr

    def hody(self, node):# returns possible cords horse jump
        return [
            (node[0] - 1, node[1] + 2),
            (node[0] - 1, node[1] - 2),
            (node[0] + 1, node[1] + 2),
            (node[0] + 1, node[1] - 2),
            (node[0] - 2, node[1] + 1),
            (node[0] - 2, node[1] - 1),
            (node[0] + 2, node[1] + 1),
            (node[0] + 2, node[1] - 1),
                ]

    def create_graph(self):
        gr = {}
        for r in range(self.rows):
            for c in range(self.cols):
                hody = [node for node in self.hody((r,c)) if node[0] in range(self.rows) and node[1] in range(self.cols) ]

                if (node_name:=self.matr[r][c]) is not None:
                    gr[node_name] = [self.matr[node[0]][node[1]] for node in hody if self.matr[node[0]][node[1]] is not None]
        return gr





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



if __name__ == "__main__":
    matr = Matr(5,5)
    # matr.set_cell(3,0, None)
    # matr.set_cell(3,2, None)
    # matr.set_cell(3,1, '0')
    graph = Matr2Graph(matr.matr)
    start = time.time()
    paths = paths(graph.create_graph())
    # pprint(paths)
    end = time.time()
    print('num of paths =', len(paths))
    print('max path len = ', max([len(path) for path in paths]))
    print('time elapsed ',end - start)