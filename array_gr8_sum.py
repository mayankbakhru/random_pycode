def main():
    numCases = int(input())
    for i in range(numCases):
        print(compute())
    return 0

def compute():
    size = int(input())
    array = list(map(int,input().split()))
    greatest = sum(array)
    for i in range(len(array)):
            if greatest  < sum(array[0:len(array)-i]):
                    greatest = sum(array[0:len(array)-i])
    return greatest


if __name__ == '__main__':main()
