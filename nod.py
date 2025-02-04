def factors(n):
    arr = [1]
    while True:

        for i in range(2, n + 1):
            if n % i == 0:
                n = n // i
                arr += [i]
                break
        if n == 1:
            break

    return arr


def intersection(arr1, arr2):
    res = []
    arr22 = arr2.copy()
    for it1 in arr1:
        for it2 in arr22:
            if it1 == it2:
                res.append(it1)
                arr22.remove(it2)
                break
    return res


def mutual_simple(n, m):
    fn = factors(n)
    fm = factors(m)
    intersect = intersection(fn, fm)
    if len(intersect) <= 1:
        return True
    else:
        return False


inp = input()
arr = inp.split(';')
set_ = set([int(arr[i].strip()) for i in range(len(arr))])
arr = sorted(list(set_))
for num in arr:

    res = []
    for i, num2 in enumerate(arr):
        if mutual_simple(num, num2):
            res += [num2]
            # zpt = ',' if i!=len(arr)-1 else ''
            # print(f" {num2}{zpt}",end='')
    out = str(res)
    if len(res) > 0:
        print(f"{num} - {out[1:-1]}")
