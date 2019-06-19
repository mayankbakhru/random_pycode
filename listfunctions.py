def main():
    N = int(input())
    totCommands = list()
    result = list()
    while N > 0 :
        array = list(input().split())
        totCommands.append(array)
        N= N-1
    # print  (N)
    # print (totCommands)
    for i in range(len(totCommands)):
        if len(totCommands[i]) > 0:
            if totCommands[i][0] == 'insert':
                param1 = int(totCommands[i][1])
                param2 = int(totCommands[i][2])
                result.insert(param1,param2)
            elif totCommands[i][0] == 'remove':
                param1 = int(totCommands[i][1])
                result.remove(param1)
            elif totCommands[i][0] == 'append':
                param1 = int(totCommands[i][1])
                result.append(param1)
            elif totCommands[i][0] == 'sort':
                #param1 = int(totCommands[i][1])
                result.sort()
            elif totCommands[i][0] == 'print':
                #param1 = int(totCommands[i][1])
                print(result)
            elif totCommands[i][0] == 'pop':
                #param1 = int(totCommands[i][1])
                result.pop()
            elif totCommands[i][0] == 'reverse':
                #param1 = int(totCommands[i][1])
                result.reverse()
            else:
                print ("invalid function")
            #print (fnName,str(param1),str(param2))
            #result = fnName(result,param1,param2)
    



if __name__  == '__main__':main()
