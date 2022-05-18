from math import floor
def websolve(puzzle):
    def check_valid(i,r):

        valid = True
        check = puzzlea[i][r]
        #check row
        for side in range(9):
            if check == puzzlea[i][side] and side != r:
                valid = False
        #check column
        for v in range(9):
            if check == puzzlea[v][r] and v != i:
                valid = False
        #check box
        check_box = [floor(i/3),floor(r/3)]
        for small_row in range(check_box[0]*3,check_box[0]*3+3):
            for small_col in range(check_box[1]*3,check_box[1]*3+3):
                if puzzlea[small_row][small_col] == check and [i,r] != [small_row,small_col]:
                    valid = False
        return valid
    puzzlea = []
    for i in puzzle:
        puzzlea.append(i)
    puzzleam = []
    for i in range(9):
        puzzleam.append(puzzlea[i*9:9*(i+1)])
    puzzlea = puzzleam
    valid = True
    zeroes = []
    backtracked = []
    for i in range(9):
        for r in range(9):
            if puzzlea[i][r] == '0':
                zeroes.append([i,r])
    while len(zeroes) > 0:
        for t in range(int(puzzlea[zeroes[0][0]][zeroes[0][1]])+1,10):
            puzzlea[zeroes[0][0]][zeroes[0][1]] = str(t)
            if check_valid(zeroes[0][0],zeroes[0][1]):
                backtracked.append([zeroes[0][0],zeroes[0][1]])
                zeroes.pop(0)
                break
        else:
            puzzlea[zeroes[0][0]][zeroes[0][1]] = '0'
            zeroes.insert(0,backtracked[-1])
            backtracked.pop(-1)
    return puzzlea


