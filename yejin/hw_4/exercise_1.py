n = int(input("줄 수를 입력하세요 "))

for i in range(n):
    i += 1
    for j in range(i):
        print("*", end="")
    print(end="\n")