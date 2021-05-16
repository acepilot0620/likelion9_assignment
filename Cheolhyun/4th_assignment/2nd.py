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


a = name.index(input("이름을 입력해 주세요 : "))

def rate(score, cut):
    for i in range(len(cut)):
        if score >= cut[i]:
            return i+1

print("학생 :", name[a])
print("국어 :", rate(kor_score[a], kor_cut))
print("영어 :", rate(eng_score[a], eng_cut))
print("수학 :", rate(math_score[a], math_cut))
print("탐구 :", (rate(tam1_score[a], tam1_cut)+rate(tam2_score[a], tam2_cut))/2)