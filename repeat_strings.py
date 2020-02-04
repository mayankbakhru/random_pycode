def main():
    s = input()
    n = int(input())

    # if ( len(s) == 1 and s == 'a'):
    #     print (n)
    #     return 0
    print (buildstring(s,n))
    #print (str1)
    #print(findoccur(str1))

def buildstring(s,n):
    result = 0
    if len(s) >= n:
        return findoccur(s[0:n])
    else:
        div = int(n / len(s))
        mod = n % len(s)
        if div !=0:
            result += div * findoccur(s)
        if mod != 0:
            result += findoccur(s[0:mod])
    return result

def findoccur(str1):
    counter = 0
    for i in str1:
        if i == 'a':
            counter += 1
    return counter

if __name__ == "__main__":
    main()
