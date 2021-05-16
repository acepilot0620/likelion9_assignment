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

김민수={kor:85,eng:80,math:90,tam1:40,tam:45}
if(kor>=90):
    korc=1
elif(kor>=83):
    korc=2
elif(kor>=75):
    korc=3
elif(kor>=66):
    korc=4
elif(kor>=54):
    korc=5
elif(kor>=40):
    korc=6
elif(kor>=26):
    korc=7
elif(kor>=15):
    korc=8
elif(kor>=0):
    korc=9
stu=input("학생 이름을 입력하세요 : ")
print
("학생 : ",stu
,"국어 : ",korc," 등급",
"영어 : ",engc," 등급",
"수학 : ",mathc," 등급",
"탐구 : ",tamc," 등급")