import sys

def see_if_works(same_lvl, corn, hunger_lvl):
    # check if proposed leveling, corn amount works in regards to given hunger levels of the cows
    hunger_lvl[0] -= corn[0]
    hunger_lvl[-1] -= corn[-1]
    for i in range(1, len(hunger_lvl)-1):
        sum_of_corn = corn[i-1] + corn[i]
        hunger_lvl[i]-= sum_of_corn
    if len(set(hunger_lvl)) == 1 and same_lvl >= 0 and min(corn) >= 0:
        return True
    else:
        return False

def odd_cows(n_cows, hunger_lvl, corn):
    # skip two to find the corn amount difference
    for i in range(1, n_cows - 1, 2):
        if i-2 >= 0:
            pos_lvl = hunger_lvl[i-1] - corn[i-2]
        else: 
            pos_lvl = hunger_lvl[i-1]
        corn[i] = hunger_lvl[i] - pos_lvl
    # find leveling, in which all the hunger level is the same
    same_lvl = hunger_lvl[-1] - corn[-1]
    corn[0] = hunger_lvl[0] - same_lvl
    # fill in rest corn amount
    for i in range(2, n_cows - 1, 2):
        corn[i] = (hunger_lvl[i] - corn[i-1] - same_lvl)
    works = see_if_works(same_lvl, corn, hunger_lvl)
    if works:
        return sum(corn)*2
    else:
        return -1

def even_cows(n_cows, hunger_lvl, corn):
    find_min_level = []
    # skip two to find the corn amount difference
    for i in range(1, n_cows - 1, 2):
        if i-2 >= 0:
            pos_lvl = hunger_lvl[i-1] - corn[i-2]
        else: 
            pos_lvl = hunger_lvl[i-1]
        find_min_level.append(pos_lvl)
        corn[i] = hunger_lvl[i] - pos_lvl
    # find leveling, in which all the hunger level is the same
    same_lvl = min(min(find_min_level), min(hunger_lvl))
    corn[0] = hunger_lvl[0] - same_lvl
    corn[-1] = hunger_lvl[-1] - same_lvl
    # fill in rest corn amount
    for i in range(2, n_cows - 2, 2):
        corn[i] = hunger_lvl[i] - corn[i-1] - same_lvl
    works = see_if_works(same_lvl, corn, hunger_lvl)
    if works:
        return sum(corn)*2
    else:
        return -1

def draught():

    # number of cows
    n_cows = int(sys.stdin.readline())
    # hunger levels
    lvl = list(map(int, sys.stdin.readline().split()))
    # corn
    corns = [0]*(n_cows - 1)
    # when n == 1
    if n_cows == 1 or len(set(lvl)) == 1:
        return 0
    # when n == 2
    if n_cows == 2:
        if len(set(lvl)) == 1:
            return 0
        else:
            return -1
    # when n == 3
    if n_cows == 3:
        corns[1] = lvl[1] - lvl[0]
        same_level = lvl[-1] - corns[1]
        corns[0] = lvl[0] - same_level
        if same_level >= 0 and min(corns) >= 0:
            return sum(corns)*2
        else:
            return -1
    # check if even or odd
    if n_cows % 2 == 0:
        return even_cows(n_cows, lvl, corns)
    else:
        return odd_cows(n_cows, lvl, corns)

cnt = int(sys.stdin.readline())
for _ in range(cnt):
    print(draught())