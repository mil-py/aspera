from pprint import pprint



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
def long_paths(gr):
    paths=[]
    ii=0

    for node in gr:#добавляем стартовые точки
        if gr[node]: #исключаем несвязанные вершины
            paths.append([node])
    count = 0
    # with open("gr.txt", 'w', encoding='UTF-8') as f:
    while True:
        old_count = count
        # new_paths = []
        for i,path in enumerate(paths):
            if not path:
                continue
            last = path[-1]  # последняя вершина в пути
            path_closed = True
            for node in gr[last]:
                if not node in path:  # добавляем вершину если такой не было в данном пути
                    paths.append(path + [node])
                    path_closed = False
                    count += 1
            if not path_closed:  # если что-то добавилось, удаляем старый путь
                paths[i] = ''
                #f.write(str(path) + '\n')
                ii = i
        if old_count == count:
            break  # если ничего не меняется - выход
        # else:
        #     paths = new_paths
        paths = paths[ii:]

    return paths

if __name__ == '__main__':
    pprint(sorted(long_paths(gr)))
    print('paths len =', len(long_paths(gr)))
    print('max path len = ',max([len(path) for path in long_paths(gr)]))