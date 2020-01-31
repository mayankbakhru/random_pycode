def main():
    total_socks = int(input())
    colors = list(map(int, input().rstrip().split()))
    if len(colors) != total_socks:
        print ("error")
        return 0
    if not(1<=total_socks<=100) or not(1<=len(colors)<=100):
        print("error")  
        return 0
    numPairs = pair_up(total_socks,colors)
    print(numPairs)

def pair_up(total_socks,colors):
    counter = 1
    numPairs = 0
    for i in colors:
        ind = -1
        ind = colors.index(i,counter,total_socks) if i in colors[counter:total_socks] else -1
        counter = counter + 1
        if ind != -1:
            numPairs += 1
            #print ("inside pair_up" + str(numPairs))
            #print (ind)
            colors.pop(ind)
    return numPairs

if __name__ == "__main__":
    main()

""" Learnings:
1. 
index function on list returns the first occurence of the element.
index function on a list throws an error if the element is not found 
to handle that error I used a tertiary operator """


