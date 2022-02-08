import sys

def see_if_works(same_lvl, corn, hunger_lvl):
    hunger_lvl[0] -= corn[0]
    hunger_lvl[-1] -= corn[-1]
    for i in range(1, len(hunger_lvl)-1):
        sum_of_corn = corn[i-1] + corn[i]
        hunger_lvl[i]-= sum_of_corn
    if len(set(hunger_lvl)) == 1 and same_lvl >= 0 and min(corn) >= 0:
        return True
    else:
        return False

def both_cows(n_cows, hunger_lvl, corn):
    find_min_level = []
    for i in range(1, n_cows - 1, 2):
        if i-2 >= 0:
            pos_lvl = hunger_lvl[i-1] - corn[i-2]
        else: 
            pos_lvl = hunger_lvl[i-1]
        corn[i] = hunger_lvl[i] - pos_lvl
    if n_cows%2==0:
        same_lvl = min(min(find_min_level), min(hunger_lvl))
    else:
        same_lvl = hunger_lvl[-1] - corn[-1]
    corn[0] = hunger_lvl[0] - same_lvl
    if n_cows%2==0:
        n_cows_sub = n_cows-2
        corn[-1] = hunger_lvl[-1] - same_lvl
    else: n_cows_sub = n_cows-1

    for i in range(2, n_cows_sub, 2):
        corn[i] = (hunger_lvl[i] - corn[i-1] - same_lvl)
    works = see_if_works(same_lvl, corn, hunger_lvl)
    if works:
        return sum(corn)*2
    else:
        return -1

def draught():
    n_cows = int(sys.stdin.readline())
    lvl = list(map(int, sys.stdin.readline().split()))
    corns = [0]*(n_cows - 1)
    if n_cows == 1 or len(set(lvl)) == 1:
        return 0
    if n_cows == 2:
        if len(set(lvl)) == 1:
            return 0
        else:
            return -1
    if n_cows == 3:
        corns[1] = lvl[1] - lvl[0]
        same_level = lvl[-1] - corns[1]
        corns[0] = lvl[0] - same_level
        if same_level >= 0 and min(corns) >= 0:
            return sum(corns)*2
        else:
            return -1
    return both_cows(n_cows, lvl, corns)

cnt = int(sys.stdin.readline())
for _ in range(cnt):
    print(draught())