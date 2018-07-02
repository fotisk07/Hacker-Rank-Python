def read_input():
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    return student_marks
    
if __name__ == '__main__':
    read_input()
    
    marks = student_marks[query_name]
    grade = sum(marks) / len(marks)
    print("{0:.2f}".format(grade))
