python = "Python is Amazing"
print(python.lower())       # 소문자 처리
print(python.upper())       # 대문자 처리
print(python[0].isupper())  # 인덱스 0에 위치한 문자가 대문자인지 참/거짓 구분
print(len(python))          # 전체 문자열 길이
print(python.replace("Python", "Java")) # 문자열 내의 문자 교체

index = python.index("n")   # 입력한 문자의 인덱스 찾기
print(index)
index = python.index("n", index+1)   # 앞에서 찾은 인덱스(5)의 다음 값(6)부터 n 문자의 인덱스 찾기
print(index)

print(python.find("n"))
print(python.find("Java"))  # 내가 원하는 값이 문자열에 포함되어 있지 않은 경우 "-1 출력"
# print(python.index("Java")) # "ValueError 발생" => python 이라는 변수에 Java 라는 문자가 없다
print("Hi")

print(python.count("n"))    # python 이라는 변수 내에 n 이라는 문자가 몇 개 등장하는지 계산
