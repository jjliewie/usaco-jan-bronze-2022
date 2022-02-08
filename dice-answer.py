import sys
k = int(sys.stdin.readline())

def dice(d1, d2):

    def win(p, q):
        cnt1, cnt2 = 0, 0
        for i in p:
            for j in q:
                if i > j: cnt1+= 1
                if j > i: cnt2+=1
        if cnt1 > cnt2: return True
        return False

    # brute force
    first_win = False
    if win(d1, d2):
        first_win = True

    for a in range(1, 11):
        for b in range(1, 11):
            for c in range(1, 11):
                for d in range(1, 11):
                    d3 = [a, b, c, d]
                    if first_win: 
                        if win(d3, d1) and win(d2, d3):
                            return "yes"
                    else:
                        if win(d3, d2) and win(d1, d3):
                            return "yes"
    
    return "no"


for i in range(k):
    dice_numbers = list(map(int, sys.stdin.readline().split()))
    dice1 = dice_numbers[:4]
    dice2 = dice_numbers[4:]
    print(dice(dice1, dice2))