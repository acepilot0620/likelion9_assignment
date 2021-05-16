print("Hello world!\n")

a = 3
b = 2

print(a//b)

c = 'hello'
d = " world"

#string 쓰면 자동으로 list로 됨(array)

print(c+d)

# 안녕

print(c[0]+d[1])

e = "파이썬 재밌다."

# a[0:3] = '파이썬'     0부터 '2'까지. 3 제외!
# a[4:] = '재밌다.'
# a[-1:-3] = '
# a[4:-5] = '재밌다. 파이썬'
# 0,1,2,3,4 = -5,-4,-3,-2,-1

a_list = [1,2,3,4,5]
#list는 넣어주면 크기가 자동으로 늘어남
# + 쓰면 리스트 합쳐줌. * 리스트 반복함

print(len(a_list))

# del a_list[-2] -> 4 빠지고 저절로 줄어들어서 1,2,3,5 됨

# 리스트 관련함수 : append, sort, reverse, index, insert, remove, pop, count 등

b_tuple = (1,2,3,4)
# 튜플 = 리스트계의 상수. 다 되는데 값 수정만 안됨

dictionary = {'key':'value','1':'안녕','3':'프티관, 어의관'}
print(dictionary['key'])
# 딕셔너리. json이랑 연동이 됨