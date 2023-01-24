N = int(input())
student_list = []
for test_case in range(N):
    student = tuple(input().split())
    student_list.append(student)

student_list = sorted(student_list, key = lambda x: int(x[0]))
for i in student_list:
    print(*i)