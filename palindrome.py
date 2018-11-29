
def main():
    print("\ninput a string:")
    str1=input()
    print ("String", str1, "is a palindrome:",PD(str1.lower()))
    

def PD(str1):
    strdict = {sd:0 for sd in str1}
    result = False
    odd_counter = 0
    for item in str1:
        strdict[item] = strdict[item] + 1
    for key in strdict:
        if (strdict[key] % 2 != 0):
            odd_counter = odd_counter + 1
    if (len(str1) % 2 == 0 and odd_counter == 0):
        result = True
    elif (len(str1) % 2 != 0 and odd_counter == 1):
        result = True
    else:
        result = False
    return result

if __name__ == '__main__': main()
