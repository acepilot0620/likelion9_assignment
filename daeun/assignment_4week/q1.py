line=int(input("줄 수를 입력하세요 :"))

for i in range(1, line+1): # range(시작숫자, 종료숫자)
    for j in range(i):#별찍기
        print("*", end="")
    print()#개행