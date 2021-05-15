from su_neung import *

input_name=input("이름을 입력해주세요 :")
student_index=name.index(input_name)
subject="kor"

subject_score=subject+"_score"
student_score=globals()[subject_score][student_index]
print(student_score)

subject_cut=subject+"_cut"
score_cut=globals()[subject_cut]
print(score_cut)