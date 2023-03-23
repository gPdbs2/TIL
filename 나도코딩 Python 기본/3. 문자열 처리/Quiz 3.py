# Quiz 3. 사이트별로 비밀번호를 만들어주는 프로그램을 작성하시오.

# ex. http://naver.com
# 규칙 1 : http:// 부분은 제외 => naver.com
# 규칙 2 : 처음 만나는 점(.) 이후 부분 제외 => naver
# 규칙 3 : 남은 글자 중 처음 세 자리(nav) + 글자 갯수(5) + 글자 내 'e' 갯수(1) + "!" 로 구성

# ex. 생성된 비밀번호 nav51!


# 나의 답
internet = "http://naver.com"
title = internet[7:12]
word = internet[7:10]
print(str(word) + len(title) + title.count("e") + "!")


# 강의 정답
url = "http://naver.com"

# 규칙 1
my_str = url.replace("http://", "")
# print(my_str)

# 규칙 2  # my_str[0:5] => 0~5 직전까지 (0, 1, 2, 3, 4)
my_str = my_str[:my_str.index(".")]
# print(my_str)

# 규칙 3
pw = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{0} 의 비밀번호는 {1}입니다.".format(url, pw))