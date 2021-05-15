from su_neung import *

def score_cal(student_index, subject):
    score_result=0

    subject_score=subject+"_score"
    student_score=globals()[subject_score][student_index]
    subject_cut=subject+"_cut"
    score_cut=globals()[subject_cut]

    for i in range(len(score_cut)):
        if student_score<score_cut[i]:
            score_result=i+2
        elif student_score==score_cut[i]:
            score_result=i+1
        
    return score_result

input_name=input("이름을 입력해주세요 :")
student_index=name.index(input_name)
trans_sub=['국어', '영어', '수학', '탐구1', '탐구2']
subjects=['kor', 'eng', 'math', 'tam1', 'tam2']
print("학생 : "+input_name)

for i in range(len(subjects)-1):
    if subjects[i]=="tam1":
        tam1_cut=(score_cal(student_index, subjects[i]))
        tam2_cut=(score_cal(student_index, subjects[i+1]))
        tam_cut=(tam1_cut+tam2_cut)/2
        round(tam_cut, 2)
        print("탐구 : "+str(tam_cut)+"등급")
        break
    else:
        print(subjects[i]+" : "+str(score_cal(student_index, subjects[i]))+"등급")
