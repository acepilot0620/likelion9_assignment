#이름을 입력해주세요 >>김민수  
#학생 : 김민수
#국어: 2등급
#영어: 4등급
#수학: 2등급
#탐구: 1.5등급

# 딕셔너리(내장함수)

    #pairs = {'잔나비': '뜨거운 여름밤은 가고 남은 건 볼품없지만', '소히': '산책' , '홍크' : '어쩌면'}

# 하나의 키-value 쌍을 추가하는 방법
# 딕셔너리형 변수 [키] = value
    #print(pairs)
    #pairs['스탠딩 에그'] = '휴식'
    #print(pairs)

# 특정 키-value 삭제하는 방법: del 함수
# del 변수[키]
    #del pairs['잔나비']
    #print(pairs)

# key로 value 얻기: 변수.get(키)
    #v= pairs.get('잔나비')
    #print(v)


name = ['김민수','박설희','이민지','김서연','김종규']
#kor_score = [85,82,90,74,65]
#eng_score = [80,75,95,65,70]
#math_score = [90,75,95,80,85]
#tam1_score = [40,35,40,42,50]
#am2_score = [45,30,48,45,45]

#kor_cut = [90,83,75,66,54,40,26,15,0]
#eng_cut = [97,93,85,75,61,43,25,16,0]
#math_cut = [92,88,76,63,37,21,14,11,0]
#tam1_cut = [42,38,32,27,20,13,9,5,0]
#tam2_cut = [45,39,33,25,20,15,12,8,0]

kor_score = {'김민수': '85','박설희': '82','이민지': '90','김서연': '74','김종규': '65'}
eng_score = {'김민수': '80','박설희': '75','이민지': '95','김서연': '65','김종규': '70'}
math_score = {'김민수': '90','박설희': '75','이민지': '95','김서연': '80','김종규': '85'}
tam1_score = {'김민수': '40','박설희': '35','이민지': '40','김서연': '42','김종규': '50'}
tam2_score = {'김민수': '45','박설희': '30','이민지': '48','김서연': '45','김종규': '45'}

김민수=

# 등급 도출 함수
#kor_cut = [90,83,75,66,54,40,26,15,0]
if(kor_score>=90):
    print("1등급")
elif(kor_score>=83):
    print("2등급")
elif(kor_score>=75):
    print("3등급")
elif(kor_score>=66):
    print("4등급")
elif(kor_score>=54):
    print("5등급")
elif(kor_score>=40):
    print("6등급")
elif(kor_score>=26):
    print("7등급")
elif(kor_score>=15):
    print("8등급")
else:
    print("9등급")

#이름입력
name= input("이름을 입력해 주세요:")
print(name)
print(kor_score)
#print("영어:"name)
#print("수학:"name)
#print("탐구:"name)


