from pprint import pprint

from numpy.ma.core import count

''' табло номеронабирателя. 
    Задача - обойти конем, 
    найти маршрут с максимальным числом ходов '''

gr = {
    '1': ['6', '8'],
    '2': ['7', '9'],
    '3': ['4', '8'],
    '4': ['0', '3', '9'],
    '5': [],
    '6': ['0', '1', '7'],
    '7': ['2', '6'],
    '8': ['1', '3'],
    '9': ['2', '4'],
    '0': ['4', '6'],
}

#найти все пути
def paths(gr):
    paths=[]
    for node in gr:
        paths.append([node])
    lens = [len(val) for val in gr.values()]
    count = max(list(lens))+3
    print('count=',count)
    while count >=0:
        new_paths=[]
        for path in paths:
            last = path[-1]
            for node in gr[last]:
                if not node in path:
                    new_paths.append(path + [node])
        paths = new_paths.copy()
        print(count)
        count-=1
    return paths

pprint(paths(gr))