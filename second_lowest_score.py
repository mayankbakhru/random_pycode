def main():
    N = int(input())
    students = dict()
    result = list()
    for _ in range(N):
        name = input()
        score = float(input())
        students[name]=score
    scores = set((students.values()))
    scores = sorted(scores)
    for key,value in students.items():
        if value == scores[1]:
            result.append(key)
    result.sort()
    for i in range(len(result)):
        print (result[i])


if __name__ == '__main__':main()
