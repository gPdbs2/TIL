# \n : 줄바꿈
print("백문이 불여일견\n백견이 불여일타")

# \" \' : 문장 내에서 따옴표
# 문자열 내부에 따옴표 사용 => 전체 문장(큰): 내부(작은) / 전체 문장(작은): 내부(큰)
print('저는 "나도코딩"입니다.')
print("저는 \"나도코딩\"입니다.")
print("저는 \'나도코딩\'입니다.")

# \\ : 문장 내에서 하나의 \
print("D:\\jhy_Git\\TIL\\나도코딩 Python 기본\\'3'. 문자열 처리\\'5'. 탈출 문자.py")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine")        # 내 출력 결과는 Pine 인데 강의는 PineApple 나온다, 왜?

# \b : 백스페이스 (한 글자 삭제)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")