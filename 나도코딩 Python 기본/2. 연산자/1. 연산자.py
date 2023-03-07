# 사직연산
print(1+1)          # 2
print(3-2)          # 1
print(5*2)          # 10
print(6/3)          # 2.0

# 제곱 및 n제곱
print(2**3)         # 2^3 = 8

# 나머지, 몫 구하기
print(5%3)          # 나머지 2
print(10%3)         # 나머지 1
print(5//3)         # 몫 1
print(10//3)        # 몫 3

# 비교 연산
print(10 > 3)       # True
print(4 >= 7)       # False
print(10 < 3)       # False
print(5 <= 5)       # True

# 앞과 뒤의 값에 대한 일치 여부
print(3 == 3)               # True
print(4 == 2)               # False
print(3+4 == 7)             # True

# 같지 않다
print(1 != 3)               # True
print(not (1 != 3))         # False

# 2개 이상의 항을 한 번에 연산
# 1) and 연산
print((3 > 0) and (3 < 5))  # True
print((3 > 0) & (3 < 5))    # True

# 2) or 연산
print((3 > 0) or (3 > 5))   # True
print((3 > 0) | (3 > 5))    # True

# 3) 연속된 항
print(5 > 4 > 3)            # True
print(5 > 4 > 7)            # False