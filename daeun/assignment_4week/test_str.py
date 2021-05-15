str="멋쟁이 사자처럼"

print(str[1:4])#1~번째 문자열까지 슬라이스
print(len(str)) #문자열의 길이
print(str.count('사')) #'사'라는 글자가 몇번 나오는지 카운팅

print(str.split()) #공백 기준으로 문자열 나눠 리스트로 반환
print(str.find('사')) #특정 문자 인덱스 찾기
print(str.index('사')) #find와 동일
#find와 index의 차이 : 찾고자하는 문자가 없을 때에 차이가 있음.