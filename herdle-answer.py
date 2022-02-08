import sys

def herdle():

    puzzle_answer = []
    puzzle_guess = []

    def split_into_chars(string):
        res = []
        for char in string:
            res.append(char)
        return res

    answer_as_oned = []
    for _ in range(3):
        temp = sys.stdin.readline().strip()
        splitted = split_into_chars(temp)
        answer_as_oned += splitted
        puzzle_answer.append(splitted)

    for _ in range(3):
        temp = sys.stdin.readline().strip()
        splitted = split_into_chars(temp)
        puzzle_guess.append(splitted)

    same_place = 0
    exists = 0
    for x in range(3):
        for y in range(3):
            if puzzle_answer[x][y] == puzzle_guess[x][y]:
                same_place += 1
                answer_as_oned.remove(puzzle_answer[x][y])

    for x in range(3):
        for y in range(3):
            if puzzle_guess[x][y] in answer_as_oned and puzzle_answer[x][y] != puzzle_guess[x][y]:
                exists += 1
                answer_as_oned.remove(puzzle_guess[x][y])
    
    return [same_place, exists]

answer = herdle()

print(answer[0])
print(answer[1])