def main ():
    numClouds = int(input())
    cloudList = list(map(int, input().rstrip().split())) #nature of cloud 0 safe, 1 unsafe
    print(jump(numClouds,cloudList))
def jump(n, clist):
    spath= 0
    skipflag = 0
    counter = 0
    for i in clist:
        if skipflag == 1:
            counter += 1
            skipflag = 0
            continue
        if counter == len (clist) - 2:
            spath += 1
            break
        if counter == len (clist) - 1:
            break
        if clist[counter + 2] == 0:
                spath += 1
                skipflag = 1
        elif clist[counter + 1] == 0:
                spath += 1
        else:
            print ("error in data")
        counter += 1
    return spath  

if __name__ == "__main__":
    main()
