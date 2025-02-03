from pprint import pprint

''' табло номеронабирателя. 
    Задача - обойти конем, 
    найти маршрут с максимальным числом ходов '''

#граф -{ вершина:[связанные вершины]}
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

    for node in gr:#добавляем стартовые точки
        if gr[node]: #исключаем несвязанные вершины
            paths.append([node])

    while True:
        new_paths=[]
        for path in paths:
            last = path[-1]#последняя вершина в пути
            path_closed = True
            for node in gr[last]:
                if not node in path:#добавляем вершину если такой не было в данном пути
                    new_paths.append(path + [node])
                    path_closed = False
            if path_closed:# если ничего не добавилось, оставляем старый путь
                new_paths.append(path)
        if paths == new_paths:
            break# если ничего не меняется - выход
        else:
            paths = new_paths


    return paths

if __name__ == '__main__':
    pprint(sorted(paths(gr)))
    print('paths len =', len(paths(gr)))
    print('max path len = ',max([len(path) for path in paths(gr)]))