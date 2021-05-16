pairs={
    '잔니비' : '뜨거운 여름밤은 가고',
    '소히' : '산책',
    '홍크' : '어쩌면'
}

print(pairs)
pairs['스탠딩 에그']='휴식' #하나의 키 - value 쌍 추기
print(pairs)
del pairs['잔나비'] #해당 키-value 쌍을 삭제
print(pairs)

v = pairs.get('소히')
print(v)