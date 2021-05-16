import sys

#1
num = sys.stdin.readline().strip()

print("줄 수를 입력하세요" + num)

for i in range(1,int(num)+1):
    print("*" * i)