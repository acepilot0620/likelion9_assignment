#제어문
#분기문 (if문): 컴퓨터에게 선택의 여지와 조건을 부여하는 문법
#if(조건): 조건이 참일때 실행할 코드

#예제-1
##85점 이상 PASS, FAIL
    #score = int(input("점수를 입력해 주세요:"))
    #if (score>=85):
    #    print("pass")
    #else: 
    #    print("fail")

#예제-2
# ==:값이 일치하는지 물어보는 연산자 / = : 값을 대입하는 연산자
    #activity = input("너 동아리 뭐해?:")
    #if(activity=="멋쟁이사자처럼"):
    #   print("어, 너도 멋사야?")
    #else:
    #    print("..그래")

#예제-3
# 5000이상: 아웃백 / 3000이상: 학식 / 1000이상: 컵라면 / ㅠㅠ: 공깃밥
money= int(input("돈 얼마 있어?"))
    #if(money>=5000):
    #   print("아웃백 가자")
    #else:
    #    if(money>=3000):
    #        print("학식 먹자")
    #    else:
    #       if(money>=1000):
    #           print("컵라면 먹자")
    #        else:
    #           print("공깃밥 가즈아ㅏㅏㅏ")

# else if = elif / elif(조건) = else if(조건) = 아니면 만약에 (조건)이라면
#else: 이것도 저것도 다 아닐때

if(money>=5000):
    print("아웃백 가자")
elif(money>=3000):
    print("학식 먹자")
elif(money>=1000):
    print("컵라면 먹자")
else:
    print("공깃밥 가즈아")


