# 랜덤 함수 : 무작위로 뽑아주는 함수
# Random 라이브러리 사용
from random import *

print(random())             # 0.0 이상 1.0 미만의 임의의 값 생성
print(random()*10)          # 0.0 ~ 10.0 미만의 임의의 값 생성
# 뒤의 소수점 자리를 보고 싶지 않으면 int로 감싸주기
print(int(random()*10))     # 1 ~ 10 미만의 임의의 값 생성
print(int(random()*10))
print(int(random()*10))
print(int(random()*10)+1)   # 1 ~ 10 이하의 임의의 값 생성
print(int(random()*10)+1)
print(int(random()*10)+1)
print(int(random()*10)+1)
print(int(random()*10)+1)
print(int(random()*10)+1)

# 로또 값 출력
print(int(random()* 45) +1)  # 1 ~ 45 이하의 임의의 값 생성
print(int(random()* 45) +1)
print(int(random()* 45) +1)
print(int(random()* 45) +1)
print(int(random()* 45) +1)
print(int(random()* 45) +1)

# randrange(a, b) : a 이상 b 미만
print(randrange(1, 46))     # 1 ~ 46 미만의 임의의 값 생성
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))
print(randrange(1, 46))

# randint(a, b) : a ~ b 사이 임의의 값 생성 (단, a와 b 둘 다 포함)
print(randint(1, 45))       # 1 ~ 45 이하의 임의의 값 생성
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))
print(randint(1, 45))