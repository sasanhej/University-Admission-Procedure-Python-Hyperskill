cap = int(input())
students = []
departments = {'Biotech': [], 'Chemistry': [], 'Engineering': [], 'Mathematics': [], 'Physics': []}
file = open('applicants.txt', 'r')
raw = file.readlines()
file.close()

score = {'Biotech': ['physics', 'chemistry'], 'Chemistry': ['chemistry'], 'Engineering': ['math', 'computer science'], 'Mathematics': ['math'], 'Physics': ['physics', 'math']}

for i in raw:
    infos = i.strip("\n").split(" ")
    students.append((infos[0], infos[1], {'physics': int(infos[2]), 'chemistry': int(infos[3]), 'math': int(infos[4]), 'computer science': int(infos[5]), 'special exam': int(infos[6])}, (infos[7], infos[8], infos[9])))

for k in range(3):
    for i in departments:
        depsort = filter(lambda x: x[3][k] == i, sorted(students, key=lambda x: (-max(sum([x[2][l] for l in score[i]])/len(score[i]),x[2]['special exam']), x[0], x[1])))
        for j in depsort:
            if len(departments[i]) < cap:
                departments[i].append((j[0], j[1], max(sum([j[2][l] for l in score[i]])/len(score[i]), j[2]['special exam'])))
                students.pop(students.index(j))

for i in departments:
    print(i)
    departments[i] = sorted(departments[i], key=lambda x: (-x[2], x[0], x[1]))
    res = open(f'{i}.txt', 'w')
    for j in departments[i]:
        print(j[0], j[1], j[2])
        res.writelines(f"{j[0]} {j[1]} {j[2]}\n")
    res.close()
    print()
