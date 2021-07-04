a = int(input("숫자 입력 : "))
b = 0
for i in range(a):
        print() # print("\n") 으로 쓰면 두 번 띄어짐. 파이썬은 print 자체에 줄넘김이 있어서
        b+=1
        for j in range(b):
            print("*", end='')
            
# 반복문 하나 쓰고 print("*"*(i+1)) 이런 식으로 쓰면 더 간단함
            