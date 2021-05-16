number=2
#print(number+1)
#banjang =input("반장의 이름을 입력하세요")
#print("우리반 반장이름은",banjang)
#number1= int(input("첫번째 숫자를 입력하세요 : "))
#number2=int(input("두번째 숫자를 입력하세요 : "))
#print(number1+number2)
#num1=float(input("여기에 첫번째 숫자를 입력하세요 :"))
#num2=float(input("여기에 두번째 숫자를 입력하세요 :"))
#print(num1*num2)
#몫://
#나머지:%
#몫+나머지:/
str="멋쟁'이 사'자처럼"
str2="은 좋은 동아리입니다"
print(str*3)
#[x:y]-->x번째 인덱스부터 y인덱스 '전까지'
print(str[1:4])
#문자열의 길이:len(문자열 변수)
print(len(str))
#문자열 내에서 특정 문자의 등장 횟수: 문자열 변수.count('특정문자')
print(str.count('사'))
#문자열을 (특정 기준으로) 나누기: 문자열 변수.split()
print(str.split("'")) # ()안에 아무것도 없으면 공백을 기준으로 나눈다.
#특정 문자 인덱스 찾기: find.('문자'), index('문자') 
print(str.index('자'))
#인덱싱 슬라이싱
li=[3,1,5,2]
#print(li[3]), print(li[0:3])
#리스트의 길이를 구해주는 함수: print(len(li))
#리스트 원소 오름차순 정렬해주는 함수: 변수.sort()
print(li)
li.sort()
print(li) #print(li.sort())는 안된다.
#리스트 내의 특정 원소 인덱스 반환해주는 함수 : .index(요소)
print(li.index(2))
#리스트 내의 특정 원소의 갯수 세기 : .count(요소)
print(li.count(2))
#딕셔너리 (내장함수)
pairs = {'잔나비': '뜨거운 여름밤은 가고 남은 건 볼품없지만', '소희': '산책', '홍크': '어쩌면'}
#하나의 키-value 쌍을 추가하는 방법
#딕셔너리형 변수[키] = value
pairs['스탠딩 에그']='휴식'
#특정 키- value 삭제하는 방법 : del 함수
#del 변수[키]
del pairs['잔나비']
print(pairs)
#key로 value 얻기 : 변수.get(키)
v= pairs.get('소희')
print(v)
# 제어문 - 분기문
# if(조건):
#예시 -1 , 85점 이상 pass, fail
#score= int(input("정수를 입력해 주세요"))
#if(score>=85):
    #print('pass')
#else:
    #print('fail')
#activity=input("너 동아리 뭐해? : ")
#if(activity=="멋사"):
    #print("어, 너도 멋사야?")
#else:
    #print('그래')
#money= int(input("돈 얼마 있어?"))
#if (money>=5000):
    #print('아웃백 가자')
#elif(money>=5000):
        #print('학식 먹자')
#elif(money>=1000):
     #print("컵라면")
#else:
    #print('공기밥 ㄱㄱ')
#else if = elif

#def 함수이름(인자): 
# 실행코드
#리턴값
#지역변수: 함수 안에 있는 변수
#전역변수: 코드 전체 영역에서 영향력 갖는 변수/ 쓰지 않기

print('input : 줄 수를 입력하세요 : ', end="")
user_input = input()
for i in range (1,int(user_input)+1):
    print(i*'*')

#이름을 입력해주세요 >>김민수  
#학생 : 김민수
#국어: 2등급
#영어: 4등급
#수학: 2등급
#탐구: 1.5등급

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



   
student= input( '이름을 입력해주세요 >>' )
print('학생 :', student)

ind= name.index(student)
for i in range(9):
    if (kor_score[ind]>=kor_cut[i]) :
        print('국어:' ,int(i+1),'등급')
        break

for i in range(9):
    if (eng_score[ind]>=eng_cut[i]) :
        print('영어:' ,int(i+1),'등급')
        break

for i in range(9):
    if (math_score[ind]>=math_cut[i]) :
        print('수학:' ,int(i+1),'등급')
        break

average= [1.5,3.5,1.5,1,1]
print('탐구:', average[ind], '등급')





    

#average=(tam1_cut.index()+tam2_cut.index())/2
#print('탐구:', average,'등급')


