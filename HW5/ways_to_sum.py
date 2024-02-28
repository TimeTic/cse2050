def ways_to_sum_memo(n, total, memo={}):
    if total == 0:
        return 1
    if total < 0:
        return 0
    if (n, total) in memo:
        return memo[(n, total)]

    count = 0
    for i in range(1, n+1):
        count += ways_to_sum_memo(n, total - i, memo)
    memo[(n, total)] = count
    return count


def ways_to_sum_tab(n, total):
    die_table = [0] * (total + 1)
    die_table[0] = 1
    
    for i in range(1, n+1):
        for j in range(i, total+1):
            # die_table[i] += die_table[j-1]
            die_table[j] += die_table[j-i]
    return die_table[total]


print(ways_to_sum_memo(n=4, total=3))
print(ways_to_sum_tab(n=4, total=3))
