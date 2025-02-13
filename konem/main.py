import time
from pprint import pprint
from graph_path_gen import long_paths



''' табло номеронабирателя. 
    Задача - обойти конем, 
    найти маршрут с максимальным числом ходов '''


class Matr2Graph:
    def __init__(self, matr):

        self.rows = len(matr)
        self.cols = max([len(arr) for arr in matr])
        self.matr = matr

    def hody(self, node):# returns possible cords horse jump
        return (
            (node[0] - 1, node[1] + 2),
            (node[0] - 1, node[1] - 2),
            (node[0] + 1, node[1] + 2),
            (node[0] + 1, node[1] - 2),
            (node[0] - 2, node[1] + 1),
            (node[0] - 2, node[1] - 1),
            (node[0] + 2, node[1] + 1),
            (node[0] + 2, node[1] - 1),
        )

    def set_edges(self):
        gr = {}
        for r in range(self.rows):
            for c in range(self.cols):
                hody = [node for node in self.hody((r,c)) if node[0] in range(self.rows) and node[1] in range(self.cols) ]

                if (node_name:=self.matr[r][c]) is not None:
                    gr[node_name] = [self.matr[node[0]][node[1]] for node in hody if self.matr[node[0]][node[1]] is not None]
        return gr





class Matr:
    def __init__(self,cols,rows):

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

    graph = Matr2Graph(matr.matr)
    start = time.time()
    gr = graph.set_edges()
    # pprint(gr)
    paths = long_paths(gr)

    end = time.time()
    print('num of paths =', len(paths))
    print('max path len = ', max([len(path) for path in paths]))
    print('time elapsed ',end - start)
    # with open('gr.txt','w', encoding="utf-8") as f:
    #     for p in paths:
    #         f.write(str(p)+'\n')