import sys
input = sys.stdin.readline
print("줄 수를 입력하세요 ", end="")
num = int(input())
for i in range(num):
    print((i+1)*"*")