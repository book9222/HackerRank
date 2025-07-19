if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    queryn_name = input()
    
    avg_score = sum(student_marks[queryn_name])/len(student_marks[queryn_name])
    # print(round(avg_score,2))
    print("{:.2f}".format(avg_score))