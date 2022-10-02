def romanToInt():
    # MCMXCIV
        s = input('Enter roman numeral:\n')
        xlat={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        negs = {'I':['V','X'],'X':['L','C'],'C':['D','M']}
        intVal=0
        i=0
        intString = list()
        opStr = list()
        while i< len(s):    
            intString.append(xlat[s[i]])
            # print(str(len(s)) + '\t'+ str(i))
            if (s[i] in negs.keys()) and i <= (len(s)-2) :
                if (s[i+1] in negs[s[i]]):
                    opStr.append('-')
                else:
                    opStr.append('+')
            else:
                # print(False)
                opStr.append('+')

            i = i+1

        i = 0
        while i < len(intString):
            if opStr[i] == '+':
                temp = intString[i]
            else:
                temp = intString[i]*-1
            intVal +=temp
            # print(intVal)
            i = i+1
        print(intVal)
        

if __name__ == "__main__":
    romanToInt()
