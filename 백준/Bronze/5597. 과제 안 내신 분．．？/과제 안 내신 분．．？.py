allStudents = set(range(1, 31))
submittedStudents = set()
for _ in range(28):
    n = int(input())
    submittedStudents.add(n)
esseki = sorted(allStudents - submittedStudents)
print(esseki[0])
print(esseki[1])