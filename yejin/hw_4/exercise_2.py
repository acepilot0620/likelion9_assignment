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

who = input("이름을 입력해주세요 >>")   # 이름 찾기
print("학생 : " + who)

num = name.index(who)   # 해당학생 인덱스 찾기

# 국어 등급
for i in range(9):
    if(kor_score[num] >= kor_cut[i]):
        rate = i+1
        print("국어 : " + str(rate) + "등급")
        break

# 영어 등급
for i in range(9):
    if(eng_score[num] >= eng_cut[i]):
        rate = i+1
        print("영어 : " + str(rate) + "등급")
        break

# 수학 등급
for i in range(9):
    if(math_score[num] >= math_cut[i]):
        rate = i+1
        print("수학 : " + str(rate) + "등급")
        break

# 탐구 평균 등급
tam = 0

# 탐구1 등급
for i in range(9):
    if(tam1_score[num] >= tam1_cut[i]):
        tam += i+1
        break

# 탐구2 등급
for i in range(9):
    if(tam2_score[num] >= tam2_cut[i]):
        tam += i+1
        break

mean = tam/2    # 평균
print("탐구 : " + str(mean) + "등급")

