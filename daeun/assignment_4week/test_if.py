#예제 1

score=int(input("점수를 입력해주세요"))

if(score>=85):
    print("pass")
else:
    print("fail")

#예제 2
activity=input("너 동아리 뭐해? :")

if(activity=="멋쟁이사자처럼"):
    print("어, 너도 멋사야?")
else:
    print("...그래...")

#예제3
money=int(input("돈 얼마 있어? "))

if(money>=50000):
    print("아웃백 가자")
elif(money>-33000):
    print("학식 먹자")
else:
    print("굶자")