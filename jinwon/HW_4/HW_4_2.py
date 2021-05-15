import sys

#2
name = ['김민수','박설희','이민지','김서연','김종규']

kor_score = [85,82,90,74,65]
eng_score = [80,75,95,65,70]
math_score = [90,75,95,80,85]
tam1_score = [40,35,40,42,50]
tam2_score = [45,30,48,45,45]

kor_cut = [90,83,75,66,54,40,26,15,0]
eng_cut = [97,93,85,75,61,43,25,16,0]
math_cut = [92,88,76,63,37,21,14,11,0]
tam1_cut = [42,38,32,27,20,13,9,5,0]
tam2_cut = [45,39,33,25,20,15,12,8,0]

print("이름을 입력해주세요")

student = sys.stdin.readline().strip()
stu_index = name.index(student)

skip = [False for _ in range(5)]

for i in range(len(kor_cut)):
    if kor_score[stu_index] >= kor_cut[i] and not skip[0]:
        kor_grade = i+1
        skip[0] = True
    if eng_score[stu_index] >= eng_cut[i] and not skip[1]:
        eng_grade = i+1
        skip[1] = True
    if math_score[stu_index] >= math_cut[i] and not skip[2]:
        math_grade = i+1
        skip[2] = True
    if tam1_score[stu_index] >= tam1_cut[i] and not skip[3]:
        tam1_grade = i+1
        skip[3] = True
    if tam2_score[stu_index] >= tam2_cut[i] and not skip[4]:
        tam2_grade = i+1
        skip[4] = True

attribute = ['학생', '국어', '영어', '수학', '탐구']
result = [student, str(kor_grade), str(eng_grade), str(math_grade), str((tam1_grade + tam2_grade)/2)]

for i in range(len(attribute)):
    if(i == 0):
        print('%s : %s' % (attribute[i], result[i]))
    elif(i > 0):
        print('%s : %s등급' % (attribute[i], result[i]))