from su_neung import *

input_name=input("이름을 입력해주세요 :")

student_index=name.index(input_name)

def score_cal(student_index, subject):
    score_result=0

    if subject=="kor":
        student_score=kor_score[student_index]
        score_cut=kor_cut
    if subject=="eng":
        student_score=eng_score[student_index]
        score_cut=eng_cut
    if subject=="math":
        student_score=math_score[student_index]
        score_cut=math_cut
    if subject=="tam1":
        student_score=tam1_score[student_index]
        score_cut=tam1_cut
    if subject=="tam2":
        student_score=tam2_score[student_index]
        score_cut=tam2_cut
    
    student_score=int(student_score)

    if student_score>=score_cut[0]:
        score_result=1
    elif student_score<score_cut[0] and student_score>=score_cut[1]:
        score_result=2
    elif student_score<score_cut[1] and student_score>=score_cut[2]:
        score_result=3
    elif student_score<score_cut[2] and student_score>=score_cut[3]:
        score_result=4
    elif student_score<score_cut[3] and student_score>=score_cut[4]:
        score_result=5
    elif student_score<score_cut[4] and student_score>=score_cut[5]:
        score_result=6
    elif student_score<score_cut[5] and student_score>=score_cut[6]:
        score_result=7
    elif student_score<score_cut[6] and student_score>=score_cut[7]:
        score_result=8
    elif student_score<score_cut[7]:
        score_result=9
        
    return score_result

print("학생 : "+input_name)

subject="kor"
print("국어 : "+str(score_cal(student_index, subject))+"등급")

subject="eng"
print("영어 : "+str(score_cal(student_index, subject))+"등급")

subject="math"
print("수학 : "+str(score_cal(student_index, subject))+"등급")

subject="tam1"
tam1_cut=score_cal(student_index, subject)

subject="tam2"
tam2_cut=score_cal(student_index, subject)

tam_cut=(tam1_cut+tam2_cut)/2
round(tam_cut, 2)
print("탐구 : "+str(tam_cut)+"등급")
