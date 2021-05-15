line=int(input("줄 수를 입력하세요 :"))

for i in range(1, line+1):
    for j in range(i):
        print("*", end="")
    print()#줄바꿈