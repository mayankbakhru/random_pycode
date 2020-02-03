def main():
    numSteps = int(input())
    dos = input() #Direction of steps
    print(countvalleys (dos,numSteps))
    #print(countvalleys (['DDUUDUD'],7))
def countvalleys(dos,numSteps):
    start = -1
    finish = -1
    nD = 0
    nU = 0
    vcount = 0
    mcount = 0
    current = None
    for i in dos :
        if (start == -1 and finish == -1):
            start = 1 
            finish = 0
            if i == 'D' :
                vcount += 1
                nD = 1
                current = 'V'            
            else :
                mcount += 1
                nU = 1
                current = 'M'
            
        elif (start == 1 and finish == 0):
            if (i == 'D'):
                nD += 1
            else:
                nU += 1
            if (nU - nD == 0):
                start = -1
                finish = -1
                nD = 0
                nU = 0
    return vcount





    

if __name__ == "__main__":
    main()
