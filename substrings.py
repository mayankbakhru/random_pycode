##Intent: to find if the two strings have common substrings

def main():
    n = int(input())
    counter = 0
    dict1 = dict()
    while True:
        if counter < n:
            s1 = input()
            s2 = input()
            counter = counter + 1
            dict1.update ({counter:[s1,s2,substring(s1,s2)]})
            continue
        else:
            break
    for v in dict1.values():
        print (v[2])
            
def substring(s1,s2):
    result = 'NO'
    for i in s1:
        if i in s2:
            result = 'YES'
            return result
    return result
        

if __name__ == "__main__":
    main()
