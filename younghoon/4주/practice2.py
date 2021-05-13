import sys
import su_neung as s

input = sys.stdin.readline
print("이름을 입력해주세요 >>", end="")
name = str(input())[:-1]

subject = ["국어", "영어", "수학", "탐구", "탐구2"]
grade = [1,1,1,1,1]

for i in range(len(s.kor_cut)):
    if s.kor_score[s.name.index(name)] < s.kor_cut[i] : grade[0]+=1
    elif s.kor_score[s.name.index(name)] == s.kor_cut[i] : pass
    if s.eng_score[s.name.index(name)] < s.eng_cut[i] : grade[1]+=1
    elif s.eng_score[s.name.index(name)] == s.eng_cut[i] : pass
    if s.math_score[s.name.index(name)] < s.math_cut[i] : grade[2]+=1
    elif s.math_score[s.name.index(name)] == s.math_cut[i] : pass
    if s.tam1_score[s.name.index(name)] < s.tam1_cut[i] : grade[3]+=1
    elif s.tam1_score[s.name.index(name)] == s.tam1_cut[i] : pass
    if s.tam2_score[s.name.index(name)] < s.tam2_cut[i] : grade[4]+=1
    elif s.tam2_score[s.name.index(name)] == s.tam2_cut[i] : pass

grade[3] = (grade[3]+grade[4])/2
print("학생 : "+name)
for i in range(4):
    print("{0} : {1}등급".format(subject[i],grade[i]))