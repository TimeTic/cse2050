def find_factors(L):
    dict_return = dict()

    for item in L:
        dict_return[item] = []
        for item2 in L:
            if item % item2 == 0:
                dict_return[item].append((item2))
    return dict_return

if __name__ == '__main__':
    print(find_factors([6, 7, 18, 1, 3]))