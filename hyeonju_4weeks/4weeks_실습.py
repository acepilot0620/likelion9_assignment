#자료형[4]_문자열 실습& 내장함수
str="안녕하세요 안녕"
print(len(str))         #문자열의 길이: len(문자열변수)
print(str.count("안"))  #문자열 내에서 특정문자의 등장횟수
print(str.split())      #문자열을 (특정 기준으로) 나누기
print(str.findt(("녕"))  #특정 문자 인덱스 찾기

#자료형[5]_리스트 실습& 내장함수
list=["3","1","배가","4","고파요","5","1"]
print(list.index("고파요")) #리스트내의 특정 원소 인덱스 반환해주는 함수
print(list.count("1"))     #리스트내의 특정 원소 갯수 세기

#자료형[6]_딕셔너리 실습& 내장함수
pairs={"잔나비":"뜨거운 여름밤은","소히":"산책"}
pairs["스탠딩 에그"]="휴식"
del pairs["스탠딩 에그"]

#제어문[1]_분기문
score=int(input("점수를 입력해 주세요 : "))
if(score>=85):
   print("pass")
else:
   print("fail")

money=int(input("돈 얼마 있어? : "))
if(money>=5000):
  print("아웃백가자")
elif(money>=3000):
  print("학식 먹자")
elif(money>=1000):
   print("컵라면 먹자")
else:
   print("공기밥 가자")
