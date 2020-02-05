import random
import sys
sys.setrecursionlimit(10**6)
# Program is written to count number of islands in a given 2x2 matrix.
# Consecutive 1s in rows and colums up and down make a island(not diagnally)
# 0s are considered water.
checked = list()

def main ():
    row = int(input())
    col = int(input())
    twod = gen_twod(row,col)
    print_twod (twod,row, col)
    counter = 0
    for r in range(row):
        for c in range(col):
            
            if twod[r][c] == 1 and (r,c) not in checked:
                counter +=1
                
                checkaround(twod,r,c, row, col)
    print ("number of islands " +str(counter))
             

def checkaround(twod,r,c,row,col):
    neighbors = list()
    neighbors.append((r,c-1))
    neighbors.append((r,c+1))
    neighbors.append((r+1,c))
    neighbors.append((r-1,c))
    for i in neighbors:
        if i[0] < 0 or i[1] < 0 or i[0] >= row or i[1] >= col :
            continue
        else:
            if twod[i[0]][i[1]] == 1 and (i[0],i[1]) not in checked:
                checked.append((i[0],i[1]))
                checkaround(twod,i[0],i[1],row,col)
            else:
                checked.append((i[0],i[1]))
                continue
    return 0

def print_twod(twod, row, col):
    for i in range(row):
        for j in range(col):
            print (twod[i][j], end =' ')
        print('')

def gen_twod(row,col):
    
    twod = list()
    for i in range(row):
        rowlist = list()
        for j in range(col):
            rowlist.append(int(round(random.uniform(0,1),0)))
        twod.append(rowlist)

    return twod


if __name__ == "__main__":
    main()
