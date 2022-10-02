def intToRoman():
    # MCMXCIV
        num = input('Enter int:\n')
        S =list()
        i = int(num)
        while (i>0):
            M = int(i/1000)
            # print(M)
            i = i - (M*1000)
            while M > 0:
                S.append('M')
                M = M - 1
            C = int(i/100)
            i = i - (C*100)
            if C == 4:
                S.append('CD')
            elif C == 9:
                S.append('CM')
            else:
                if C >= 5:
                    S.append('D')
                    C = C - 5
                while C > 0:
                    S.append('C')
                    C = C - 1
            X = int(i/10)
            i = i - (X*10)
            if X == 4:
                S.append('XL')
            elif X == 9:
                S.append('XC')  
            else:
                if X >= 5:
                    S.append('L')
                    X = X - 5
                while X > 0:
                    S.append('X')
                    X = X - 1
            I = int(i)
            i = i - int(i)
            if I == 4:
                S.append('IV')
            elif I == 9:
                S.append('IX')  
            else:
                if I >= 5:
                    S.append('V')
                    I = I - 5
                while I > 0:
                    S.append('I')
                    I = I - 1
        print(''.join(S))
        
        

if __name__ == '__main__':
    intToRoman()
