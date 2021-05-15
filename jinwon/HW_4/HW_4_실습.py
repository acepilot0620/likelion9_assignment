# 문자열 (내장함수)
str = "멋쟁이사자처럼좋아요"
print(str[1:4])

#문자열의 길이 : len(문자열 변수)
print(len(str))

#문자열 내에서 특정 문자의 등장 횟수 : 문자열 변수.count('특정문자')
print(str.count('사'))

#문자열을 (특정 기준으로) 나누기 : 문자열 변수.split()
print(str.split("'"))

#특정 문자 인덱스 찾기 : find('문자'), index('문자')
print(str.index('사'))

#리스트 (내장함수)
li = [3,1,"움칫",4,"둠칫",5,2,2,2,2]

#리스트 원소 오름차순 정렬해주는 함수 : 변수.sort()
li.sort()
print(li.sort())

#리스트 내의 특정 원소 인덱스 반환해주는 함수 : .index(요소)
print(li.index("움칫"))

# 리스트 내의 특정 원소의 갯수 세기 : .count(요소)
print(li.count(2))

#딕셔너리 (내장함수)

pairs = {'잔나비' : '뜨거운 여름밤은 가고 남은 건 볼품없지만', '소히':'산책','홍크':'어쩌면'}

# 하나의 키-value 쌍을 추가하는 방법
# 딕셔너리형 변수[키] = value
pairs['스텐딩 에그'] = '휴식'
print(pairs)

# 특정 키-value 삭제하는 방법 : del 함수
# del 변수[키]
del pairs['잔나비']
print(pairs)

# key로 value 얻기 : 변수.get(키)

v = pairs.get('잔나비')
print(v)

#if문
money = int(input("돈 얼마 있어? "))

if(money>=5000):
    print("아웃백 가자")
elif(money>=3000):
    print("학식 먹자")
elif(money>=1000):
    print("컵라면 먹자")
else:
    print("공기밥 가즈아ㅏㅏㅏ")