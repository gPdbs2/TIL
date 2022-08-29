# JAVA Chapter 3

이해관계자: 익명
작성일시: 2022년 8월 24일 오후 7:37
최종 편집일시: 2022년 8월 29일 오후 11:53

# Chapter ****03. 자료형****

- **자료형**
    - 프로그래밍을 할 때 쓰이는 숫자, 문자열 등의 자료 형태로 사용하는 그 모든 것
    - 프로그램의 가장 기본이 되고 핵심적인 단위가 되는 것
    - 자료형을 충분히 이해하지 않고 프로그래밍을 시작하려는 것
        - 기초 공사가 마무리되지 않은 상태에서 빌딩을 세우는 것

## ****01. 숫자 (Number)****

- **정수**
    - **자료형 : int, long**
    - int와 long의 차이 → 표현할 수 있는 숫자의 범위
        
        
        | 자료형 | 표현범위 |
        | --- | --- |
        | int | 2147483648 ~ 2147483647 |
        | long | -9223372036854775808 ~ 9223372036854775807 |
        
        ```java
        int age = 10;
        long countOfStar = 8764827384923849L;
        ```
        
    - long 변수에 값을 대입할 때
        - 대입하는 숫자 값이 int 자료형의 최대값인 2147483647 보다 큰 경우
            - `8764827384923849L`과 같이 `L`접미사(또는 소문자 `l`, 소문자 'l'은 숫자 1과 비슷하게 보이므로 추천하지 않음)를 붙여 주어야 함
            - 만약 큰 숫자에 'L'과 같은 접미사를 누락 시 컴파일 에러 발생

- **실수**
    - **자료형 : float, double**
    - float와 double의 차이 → 표현할 수 있는 숫자 범위
        
        
        | 자료형 | 표현범위 |
        | --- | --- |
        | float | -3.4*10^38 ~ 3.4*10^38 |
        | double | -1.7*10^308 ~ 1.7*10^308 |
        
        ```java
        float pi = 3.14F;
        double morePi = 3.14159265358979323846;
        ```
        
    - 자바에서 실수형은 디폴트가 double
        - float 변수에 값을 대입할 때에는 3.14F 와 같이 `F`접미사(또는 소문자 `f`)를 꼭 붙여야 함
        - float 자료형에 값을 대입할 때 접미사 누락 시 컴파일 에러 발생
        
        ```java
        double d1 = 123.4;
        double d2 = 1.234e2;
        ```
        
    - `e2` : 10의 제곱

- **8진수와 16진수**
    - 8진수와 16진수는 int 자료형을 사용하여 표시
    - 0(숫자 '0')으로 시작하면 8진수
    - 0x(숫자 '0' + 알파벳 'x')로 시작하면 16진수
    
    ```java
    int octal = 023;    // 10진수: 19
    int hex = 0xC;     // 10진수: 12
    ```
    

- **숫자연산**
    - `+, -, *, /`기호를 이용하여 두 숫자 간 사칙연산 수행
        
        ```java
        public class Sample {
            public static void main(String[] args) {
                int a = 10;
                int b = 5;
                System.out.println(a+b);
                System.out.println(a-b);
                System.out.println(a*b);
                System.out.println(a/b);
            }
        }
        ```
        
    - 프로그램 출력
        
        ```java
        15
        5
        50
        2
        ```
        
    
    - %연산자 : 나머지 값 반환
        
        ```java
        public class Sample {
            public static void main(String[] args) {
                System.out.println(7 % 3);  // 1 출력
                System.out.println(3 % 7);  // 3 출력
            }
        }
        ```
        

- **증감연산 (++, —)**
    - 증감 연산자 : `++`, `--`
        
        ```java
        int i = 0;
        int j = 10;
        i++;
        j--;
        
        System.out.println(i);  // 1 출력
        System.out.println(j);  // 9 출력
        ```
        
    
    - `**++`, `--` 등의 연산자의 위치**
        - `i++` → 값이 참조된 후에 증가
            - ++ 연산자가 변수명 뒤에 붙으면 해당 코드가 실행되는 순간에는 i 값이 변경되지 않음
            - 문장이 실행된 이후에 i값이 증가
        - `++i` → 값이 참조되기 전에 증가
            - i 값이 먼저 증가된 후에 해당 코드가 실행

## ****02. 불 (boolean)****

- **bool 자료형**
    - 참 또는 거짓의 값을 갖는 자료형
    - 자료형의 명칭 : **boolean**
    - 불 자료형에 대입되는 값은 참(true) 또는 거짓(false)만 가능
    
    ```java
    boolean isSuccess = true;
    boolean isTest = false;
    ```
    

- ****불 연산****
    - 참, 거짓을 판단하는 연산
    
    ```java
    2 > 1             // 참
    1 == 2            // 거짓
    3 % 2 == 1        // 참 (3을 2로 나눈 나머지는 1이므로 참이다.)
    "3".equals("2")   // 거짓
    ```
    
    - 부울 연산의 결과는 참 또는 거짓
        - if문과 같은 조건문에 쓰이거나 불 자료형에 대입 가능

- **조건문**
    - 불 연산 → 조건문의 판단 기준으로 많이 사용
    
    ```java
    int base = 180;
    int height = 185;
    boolean isTall = height > base;
    
    if (isTall) {
        System.out.println("키가 큽니다.");
    }
    ```
    

```java
int i = 3;
boolean isOdd = i % 2 == 1;
System.out.println(isOdd);  // true 출력
```

- `i % 2 == 1`
    - i를 2로 나누었을 때 나머지가 1인지를 묻는 조건문
    - i는 3이므로 3을 2로 나눈 나머지는 1이 되어 참
        - isOdd 는 true 값

## ****03. 문자 (char)****

- `char` → 한 개의 문자 값에 대한 자료형
    
    ```java
    char a1 = 'a';
    ```
    
    - **주의)** 문자값을 `'`(단일 인용부호)로 감싸주어야 함
    - char는 문자값을 표현하는 방식이 다양하기 때문에 주의
    
    ```java
    char a1 = 'a';  // 문자로 표현
    char a2 = 97;  // 아스키코드로 표현
    char a3 = '\u0061';  // 유니코드로 표현
    
    System.out.println(a1);  // a 출력
    System.out.println(a2);  // a 출력
    System.out.println(a3);  // a 출력
    ```
    
    - 'a'라는 문자값을 위와 같이 'a', 97, '\u0061'과 같이 값을 설정해도 모두 같은 것
        - 첫번째 : 문자값
        - 두번째 : 아스키코드 값
        - 세번째 : 유니코드 값

## ****04. 문자열 (String)****

- ****원시(primitive) 자료형****
    - 원시(primitive) 자료형
        - int, long, double, float, boolean, char 등
    - primitive 자료형은 `new`키워드로 그 값을 생성할 수 없음
    - 리터럴(literal)로만 값 세팅 가능
    
    ```java
    boolean result = true;
    char capitalC = 'C';
    int i = 100000;
    ```
    
    - String 은 "Happy Java"와 같이 리터럴로 표기가 가능
    - But primitive 자료형은 아님
    - String → 리터럴 표현식을 사용할 수 있도록 자바에서 특별 대우해주는 자료형
    - **원시 자료형의 Wrapper 클래스**
        - int, long, double, float, boolean, char 등의 원시 자료형
            - 각각에 대응하는 Wrapper 클래스들이 존재
        
        | 원시자료형 | Wrapper 클래스 |
        | --- | --- |
        | int | Integer |
        | long | Long |
        | double | Double |
        | float | Float |
        | boolean | Boolean |
        | char | Char |
        - ArrayList, HashMap, HashSet 등은 데이터 저장시 원시 자료형 대신 그에 대응하는 Wrapper 클래스들을 사용해야 함

- ****문자열 내장 메소드****
    - ****equals****
        - 2개의 문자열이 동일한지를 비교하여 결과값을 리턴
        
        ```java
        String a = "hello";
        String b = "java";
        String c = "hello";
        System.out.println(a.equals(b)); // false 출력
        System.out.println(a.equals(c)); // true 출력
        ```
        
    - 문자열 a 와 문자열 b 는 "hello"와 "java"로 서로 같지 않다.
        - 따라서 equals 메소드 호출 시 false 를 리턴
    - 문자열 a 와 문자열 c 는 "hello"와 "hello"로 서로 같음
        - 따라서 true 를 리턴
    - 문자열의 값을 비교할때는 반드시 equals 를 사용
        - `==`연산자를 사용할 경우 다음과 같은 경우가 발생
    
    ```java
    String a = "hello";
    String b = new String("hello");
    System.out.println(a.equals(b));  // true
    System.out.println(a == b);  // false
    ```
    
    - 문자열 a와 b는 모두 "hello"로 같은 값이지만 equals 를 호출했을 때는 true,
    - `==`연산자를 이용했을 때는 false 리턴
    - a와 b는 값은 같지만 서로 다른 객체
    - `==`
        - 2개의 자료형이 동일한 객체인지를 판별할 때 사용하는 연산자
    
    - ****indexOf****
        - 문자열에서 특정 문자가 시작되는 위치(인덱스)를 리턴
        
        ```java
        String a = "Hello Java";
        ```
        
        - a 문자열에서 "Java"라는 문자열이 시작되는 위치를 알고 싶은 경우 다음과 같이 indexOf 사용
        
        ```java
        String a = "Hello Java";
        System.out.println(a.indexOf("Java"));  // 6 출력
        ```
        
        - "Hello Java" 라는 문자열에서 "Java"라는 문자열은 일곱번째 문자('J')부터 시작
        - 결과값이 6으로 나온 이유는 자바는 숫자를 0부터 세기 때문
    
    - ****contains****
        - 문자열에서 특정 문자열이 포함되어 있는지의 여부를 리턴
        
        ```java
        String a = "Hello Java";
        System.out.println(a.contains("Java"));  // true 출력
        ```
        
        - 문자열 a는 "Java"라는 문자열을 포함하고 있기 때문에 true를 리턴
    
    - ****charAt****
        - 문자열에서 특정 위치의 문자(char)를 리턴
        
        ```java
        String a = "Hello Java";
        System.out.println(a.charAt(6));  // "J" 출력
        ```
        
        - a 문자열에서 "J"라는 문자는 6번째 인덱스에 위치한 문자
            - 6이라는 숫자로 "J"라는 문자를 얻기 위해서는 다음과 같이 charAt을 사용
        - "Hello Java" 라는 문자열에서 "J"라는 문자는 일곱번째 문자
            - 6으로 문자를 찾아야 하는 이유는 자바는 숫자를 0부터 세기 때문
        
    - ****replaceAll****
        - 문자열 중 특정 문자열을 다른 문자열로 바꾸고자 할 때 사용
        
        ```java
        String a = "Hello Java";
        System.out.println(a.replaceAll("Java", "World"));  // Hello World 출력
        ```
        
        - "Hello Java" 라는 문자열에서 "Java"가 "World"로 바뀜
    
    - ****substring****
        - 문자열 중 특정 부분을 뽑아낼 경우에 사용
        
        ```java
        String a = "Hello Java";
        System.out.println(a.substring(0, 4));  // Hell 출력
        ```
        
        - substring(시작위치, 끝위치)와 같이 사용
            - 문자열의 시작위치에서 끝위치까지의 문자를 뽑아내게 됨
            
            ```java
            시작위치 <= a < 끝위치
            ```
            
    
    - ****toUpperCase****
        - 문자열을 모두 대문자로 변경할 때 사용
        - 모두 소문자로 변경할 때는 toLowerCase 사용
        
        ```java
        String a = "Hello Java";
        System.out.println(a.toUpperCase());  // HELLO JAVA 출력
        ```
        
    
    - ****split****
        - 문자열을 특정 구분자로 분리하는 메소드
        
        ```java
        String a = "a:b:c:d";
        String[] result = a.split(":");  // result는 {"a", "b", "c", "d"}
        ```
        
        - "a:b:c:d" 라는 문자열을 ":" 문자로 나누어 `{"a", "b", "c", "d"}`
         문자열 배열을 만들 수 있음
    

- ****문자열 포매팅****
    - 문자열 안의 특정한 값을 바꿔야 할 경우가 있을 때 이것을 가능하게 해주는 것
    - 문자열 안에 어떤 값을 삽입하는 방법
    
    - 문자열 포매팅 따라 하기
        - 숫자 바로 대입
        
        ```java
        System.out.println(String.format("I eat %d apples.", 3));  // "I eat 3 apples." 출력
        ```
        
        - 문자열 포매팅은 `String.format`메소드 사용
        - 문자열 안에서 숫자를 넣고 싶은 자리에 %d 문자를 넣어 주고
        - %d : 문자열 포맷 코드
    
    - 문자열 바로 대입
        - 숫자 대신 문자열을 넣었을 때
        
        ```java
        System.out.println(String.format("I eat %s apples.", "five"));  // "I eat five apples." 출력
        ```
        
        - 1번처럼 숫자를 바로 대입하나 위 예제처럼 숫자 값을 나타내는 변수를 대입하나 결과는 같음
    
    - 2개 이상의 값 넣기
        - 문자열 안에 1개가 아닌 여러 개의 값을 넣고 싶을 때
        
        ```java
        int number = 10;
        String day = "three";
        
        // "I ate 10 apples. so I was sick for three days." 출력
        System.out.println(String.format("I ate %d apples. so I was sick for %s days.", number, day));
        ```
        
        - 2개 이상의 값을 넣으려면 파라미터로 여러 개를 전달
    

- ****문자열 포맷 코드****
    
    
    | 코드 | 설명 |
    | --- | --- |
    | %s | 문자열(String) |
    | %c | 문자 1개(character) |
    | %d | 정수(Integer) |
    | %f | 부동소수(floating-point) |
    | %o | 8진수 |
    | %x | 16진수 |
    | %% | Literal % (문자 % 자체) |
    - %s 포맷 코드
        - 어떤 형태의 값이든 변환해 넣을 수 있음
        
        ```java
        System.out.println(String.format("I have %s apples",  3));  // "I have 3 apples" 출력
        System.out.println(String.format("rate is %s", 3.234));  // "rate is 3.234" 출력
        ```
        
        - 3을 문자열 안에 삽입하려면 %d를 사용하고, 3.234를 삽입하려면 %f를 사용해야 함
        - 하지만 %s를 사용하면 이런 것을 생각하지 않아도 됨
            - %s는 자동으로 % 뒤에 있는 값을 문자열로 바꾸기 때문
        

- **[포매팅 연산자 %d와 %를 같이 쓸 때는 %%를 쓴다]**
    
    ```java
    System.out.println(String.format("Error is %d%.", 98));
    ```
    
    - 당연히 "Error is 98%."가 출력될 것이라 예상될 것
        - But 오류(UnknownFormatConversionException) 발생
    
    ```java
    Exception in thread "main" java.util.UnknownFormatConversionException: Conversion = '.'
    (... 생략 ...)
    ```
    
    - 문자열 포맷 코드인 %d와 %가 같은 문자열 안에 존재하는 경우, %를 나타내려면 반드시 %%로 써야 하는 법칙이 있기 때문
    - 문자열 안에 %d 같은 포매팅 연산자가 없으면 %는 홀로 쓰여도 상관 없음
    - 위 예를 제대로 실행하려면
        
        ```java
        System.out.println(String.format("Error is %d%%.", 98));  // "Error is 98%." 출력
        ```
        

- ****포맷 코드와 숫자 함께 사용하기****
    - %d, %s 등의 포맷 코드 → 문자열 안에 어떤 값을 삽입하기 위해 사용
    - 하지만 포맷 코드를 숫자와 함께 사용하면 더 유용하게 사용
    
    - 정렬과 공백
        
        ```java
        System.out.println(String.format("%10s", "hi"));  // "        hi" 출력
        ```
        
        - `%10s`
            - 전체 길이가 10개인 문자열 공간에서 대입되는 값을 오른쪽으로 정렬하고 그 앞의 나머지는 공백으로 남겨 둬라
            - 반대쪽인 왼쪽 정렬 : `%-10s`
            
            ```java
            System.out.println(String.format("%-10sjane.", "hi"));  // "hi        jane." 출력
            ```
            
            - hi를 왼쪽으로 정렬하고 나머지는 공백으로 채웠음
        
    - 소수점 표현하기
        - 3.42134234를 소수점 네 번째 자리까지만 나타내고 싶은 경우
            
            ```java
            System.out.println(String.format("%.4f", 3.42134234));  // 3.4213 출력
            ```
            
        - 즉 여기서 '.' → 소수점 포인트
        - 그 뒤의 숫자 4 → 소수점 뒤에 나올 숫자의 개수
        
        - 숫자 3.42134234를 소수점 네 번째 자리까지만 표시하고 전체 길이가 10개인 문자열 공간에서 오른쪽으로 정렬
            
            ```java
            System.out.println(String.format("%10.4f", 3.42134234));  // '    3.4213' 출력
            ```
            
        
- ****System.out.printf****
    - `String.format`
        - 포매팅된 문자열을 리턴
        - 포매팅된 문자열을 출력하려면 `System.out.println`메소드를 함께 사용해야 함
        
        ```java
        System.out.println(String.format("I eat %d apples.", 3));  // "I eat 3 apples." 출력
        ```
        
        - 하지만 `System.out.printf`메소드를 사용 시
            - `String.format` 메소드 없이도 동일한 형식으로 포매팅된 문자열을 출력 가능
            
            ```java
            System.out.printf("I eat %d apples.", 3);  // "I eat 3 apples." 출력
            ```
            
    
    - `String.format` 과 `System.out.printf`의 차이
        - 전자 : 문자열을 리턴하는 메소드
        - 후자 : 문자열을 출력하는 메소드

## ****05. StringBuffer****

- **StringBuffer**
    - 문자열을 추가하거나 변경 할 때 주로 사용하는 자료형

- ****append****
    - StringBuffer 객체를 생성하고 문자열을 생성하는 예제
        
        ```java
        StringBuffer sb = new StringBuffer();  // StringBuffer 객체 sb 생성
        sb.append("hello");
        sb.append(" ");
        sb.append("jump to java");
        String result = sb.toString();
        System.out.println(result);
        ```
        
    - 결과값
        
        ```java
        hello jump to java
        ```
        

- StringBuffer 자료형
    - append 메소드를 사용하여 계속해서 문자열 추가 가능
    - `toString()`메소드를 이용 시 String 자료형으로 변경 가능
    
    ```java
    String result = "";
    result += "hello";
    result += " ";
    result += "jump to java";
    System.out.println(result);
    ```
    
- 결과값
    
    ```java
    hello jump to java
    ```
    

- 두 예제의 결과는 동일, But 내부적으로 객체가 생성되고 메모리가 사용되는 과정 다름
- 첫 번째 예제의 경우
    - StringBuffer 객체는 한 번만 생성
- 두 번째 예제의 경우
    - String 자료형에 `+`연산이 있을 때마다 새로운 String 객체가 생성됨 (문자열 간 `+`연산이 있는 경우 자바는 자동으로 새로운 String 객체 생성)
    - 총 4개의 String 자료형 객체 생성

- String 자료형은 한번 값이 생성되면 그 값을 변경 불가
    - immutable 하다 : 값을 변경할 수 없는 것
- trim, toUpperCase 등의 메소드
    - 문자열이 변경되는 것 처럼 생각 될 수도 있지만 해당 메소드 수행 시 또 다른 String 객체를 생성하여 리턴할 뿐임
- But StringBuffer는 이와 반대로 값을 변경 가능 → mutable 하다
    - 한 번 생성된 값을 언제든지 수정 가능

- 무조건 StringBuffer 사용하는 게 좋을까?
    - 상황에 따라 다름
    - StringBuffer 자료형은 String 자료형보다 무거운 편
    - `new StringBuffer()` 로 객체를 생성하는 것
        - 일반 String을 사용하는 것보다 메모리 사용량도 많고 속도 느림
        - 문자열 추가나 변경등의 작업이 많을 경우에는 StringBuffer를,
        - 문자열 변경 작업이 거의 없는 경우에는 그냥 String을 사용하는 것이 유리

- **StringBuilder**
    - StringBuffer와 비슷한 자료형
    - StringBuilder의 사용법은 StringBuffer의 사용법과 동일
    
    ```java
    StringBuilder sb = new StringBuilder();
    sb.append("hello");
    sb.append(" ");
    sb.append("jump to java");
    String result = sb.toString();
    System.out.println(result);
    ```
    
    - StringBuffer → 멀티 스레드 환경에서 안전하다는 장점
    - StringBuilder → StringBuffer보다 성능이 우수한 장점
        - 동기화를 고려할 필요가 없는 상황에서는 StringBuffer 보다는 StringBuilder를 사용하는 것이 유리

- ****insert****
    - 특정 위치에 원하는 문자열을 삽입 가능
    
    ```java
    StringBuffer sb = new StringBuffer();
    sb.append("jump to java");
    sb.insert(0, "hello ");
    System.out.println(sb.toString());
    ```
    
    - 결과값
        
        ```java
        hello jump to java
        ```
        
        - insert를 사용하여 0 번째 위치에 "hello " 라는 문자열 삽입

- ****substring****
    - String 자료형의 substring 메소드와 동일하게 사용
    
    ```java
    StringBuffer sb = new StringBuffer();
    sb.append("Hello jump to java");
    System.out.println(sb.substring(0, 4));
    ```
    
    - 결과값
        
        ```java
        Hell
        ```
        
    - substring(시작위치, 끝위치)
        - StringBuffer 객체의 시작위치에서 끝위치까지의 문자 추출
    

## ****06. 배열 (Array)****

- **배열**
    - 자료형의 종류가 아닌 자료형의 집합
    - 자료형 타입 바로 옆에 `[]`기호를 사용하여 표현
    - 1부터 10까지의 숫자들 중 홀수들의 집합은 다음과 같이 int 배열로 표현 가능
        
        ```java
        int[] odds = {1, 3, 5, 7, 9};
        ```
        
    - 예제와 같이 `int`자료형의 배열은 `int[]`로 표현
    - 요일의 집합 → String 배열로 표현
        
        ```java
        String[] weeks = {"월", "화", "수", "목", "금", "토", "일"};
        ```
        

- ****배열의 길이는 고정되어 있다****
    - 요일의 집합 예제
        
        ```java
        String[] weeks = new String[7];
        weeks[0] = "월";
        weeks[1] = "화";
        weeks[2] = "수";
        weeks[3] = "목";
        weeks[4] = "금";
        weeks[5] = "토";
        weeks[6] = "일";
        ```
        
        - 배열의 길이를 먼저 설정하여 배열 변수를 먼저 생성 후 그 값은 나중에 대입하는 방법
        - 초기값 없이 배열 변수를 만들 때에는 반드시 길이에 대한 숫자값 필요
        - 다음과 같은 코드는 불가능
            
            ```java
            String[] weeks = new String[];    // 길이에 대한 숫자값이 없으므로 컴파일 오류가 발생한다.
            ```
            

- ****배열의 값은 어떻게 접근할 수 있을까?****
    - 요일의 배열중 "목"에 해당되는 값을 얻으려면?
        - 인덱싱 활용
        
        ```java
        String[] weeks = {"월", "화", "수", "목", "금", "토", "일"};
        System.out.println(weeks[3]);
        ```
        
        - weeks[3] →  weeks 배열의 네번째 항목 (자바는 0부터 숫자 셈)

- ****배열의 길이****
    - 배열은 보통 for문과 함께 사용
    - for문에 배열이 사용될 경우
        - 배열의 길이만큼 for 문을 돌리는 것이 중요
        - 배열의 길이 → length를 이용해 구함
        
        ```java
        String[] weeks = {"월", "화", "수", "목", "금", "토", "일"};
        for (int i=0; i<weeks.length; i++) {
            System.out.println(weeks[i]);
        }
        ```
        
        - weeks 배열을 순서대로 출력하는 프로그램

- ****빈번한 배열의 오류****
    - 자바 코드를 작성하면서 보게 될 가장 많은 오류 중의 하나
        
        ```java
        ArrayIndexOutOfBoundsException
        ```
        
    - 요일 배열의 길이는 총 7개인데 만약 8번째 값을 얻으려고 시도 → 오류 발생
        
        ```java
        System.out.println(weeks[7]);  
        // 8번째 배열값이 없으므로 ArrayIndexOutOfBoundsException 오류가 발생한다.
        ```
        

## ****07. 리스트 (List)****

- ****ArrayList****
    - **List 자료형**
        - ArrayList, Vector, LinkedList 등의 List 인터페이스를 구현한 자료형
    - ****add****
        
        ```java
        import java.util.ArrayList;
        
        public class Sample {
            public static void main(String[] args) {
                ArrayList pitches = new ArrayList();
                pitches.add("138");
                pitches.add("129");
                pitches.add("142");
            }
        }
        ```
        
        - ArrayList를 사용하기 위해서는 ArrayList를 먼저 import
            - `import java.util.ArrayList`
        - ArrayList 객체인 pitches에 add 라는 메소드를 이용하여 투구 스피드를 저장
        - 첫번째 위치에 "133"이라는 투구 스피드를 삽입하고 싶다면 삽입할 위치를 파라미터로 넘겨줘야 함
            
            ```java
            pitches.add(0, "133");    // 첫번째 위치에 133 삽입.
            ```
            
        
        - 2번째 위치에 133을 삽입할 경우
            
            ```java
            pitches.add(1, "133");
            ```
            
        
    - **제네릭스**
        - 자바는 J2SE 5.0 버전 이후부터 `ArrayList<String> pitches = new ArrayList<>();`
         처럼 객체를 포함하는 자료형도 어떤 객체를 포함하는지에 대해서 명확하게 표현할 것을 권고
        - 인텔리제이에서 위의 예제와 같이 제네릭스 없이 코딩
            - 명확한 타입을 명시하라는 warning이 표시
    
    - ****get****
        - 특정 인덱스의 값을 추출
            
            ```java
            System.out.println(pitches.get(1));
            ```
            
    
    - ****size****
        - ArrayList의 갯수를 리턴
            
            ```java
            System.out.println(pitches.size());
            ```
            

- ****contains****
    - 리스트 안에 해당 항목이 있는지를 판별하여 그 결과를 boolean으로 리턴
        
        ```java
        System.out.println(pitches.contains("142"));
        ```
        

- ****remove****
    - 2가지 방식
        - **remove(객체)**
            - 리스트에서 객체에 해당되는 항목을 삭제하고 삭제한 결과(true, false)를 리턴
            
            ```java
            System.out.println(pitches.remove("129"));
            
            // 수행결과
            true
            ```
            
        - **remove(인덱스)**
            - 해당 인덱스의 항목을 삭제하고 삭제된 항목을 리턴
            
            ```java
            System.out.println(pitches.remove(0));
            
            // 수행결과
            138
            ```
            
            - pitches의 첫번째 항목은 "138"이므로 "138"이 삭제된 후 "138"을 리턴

- ****제네릭스(Generics)****
    - 제네릭스(Generics)
        
        ```java
        ArrayList<String> pitches = new ArrayList<String>();
        
        // 선호되는 방식
        ArrayList<String> pitches = new ArrayList<>();
        ```
        

- `<String>`이라는 제네릭스 표현식
    - "ArrayList 안에 담을 수 있는 자료형은 String 타입 뿐이다" 라는 의미
    - `<Integer>`, `<Animal>`, `<Dog>` 등 어떤 자료형도 사용 가능
    - 제네릭스를 이용하면 좀 더 명확한 타입체크 가능
    - 제네릭스를 사용하지 않은 경우
        
        ```java
        ArrayList pitches = new ArrayList();
        aList.add("138");
        aList.add("129");
        
        String one = (String) pitches.get(0);
        String two = (String) pitches.get(1);
        ```
        
        - ArrayList 안에 추가되는 객체는 Object 자료형으로 인식
        - Object 자료형은 모든 객체가 상속하고 있는 가장 기본적인 자료형
        - ArrayList 객체인 pitches에 값을 넣을 때는 문제가 안되지만
            - **But,** 값을 가져올 경우에는 항상 Object 자료형에서 String 자료형으로 형변환(casting) 해줘야 함
            
            ```java
            String one = (String) pitches.get(0); // Object 자료형을 String 자료형으로 캐스팅한다.
            ```
            
        - pitches 안에는 String 객체 이외의 객체도 넣을 수 있기 때문에 형 변환 과정에서 잘못된 형변환으로 인한 오류가 발생할 가능성이 있음
        
    - 위의 코드를 제네릭스를 사용해 변경할 경우
        
        ```java
        ArrayList<String> pitches = new ArrayList<>();
        aList.add("138");
        aList.add("129");
        
        String one = pitches.get(0);  // 형 변환이 필요없다.
        String two = pitches.get(1);  // 형 변환이 필요없다.
        ```
        
        - 제네릭스로 자료형을 선언하기만 하면 그 이후로는 자료형에 대한 형변환 과정이 필요 X
        - 이미 컴파일러가 pitches에는 반드시 String 자료형만 추가 되어야 함을 알기 때문
    
    - 이렇게 제네릭스를 이용하면 형변환에 의한 불필요한 코딩과 잘못된 형변환에 의한 런타임 오류 방지

- ****다양한 방법으로 ArrayList 만들기****
    - ArrayList의 add 메소드를 사용 → ArrayList 객체에 요소를 추가 가능
        
        ```java
        import java.util.ArrayList;
        
        public class Sample {
            public static void main(String[] args) {
                ArrayList<String> pitches = new ArrayList<>();  // 제네릭스를 사용한 표현
                pitches.add("138");
                pitches.add("129");
                pitches.add("142");
                System.out.println(pitches);  // [138, 129, 142] 출력
            }
        }
        ```
        

- 이미 데이터가 존재할 경우에는 보다 편하게 ArrayList를 생성 가능
    
    ```java
    import java.util.ArrayList;
    import java.util.Arrays;
    
    public class Sample {
        public static void main(String[] args) {
            String[] data = {"138", "129", "142"};  // 이미 투구수 데이터 배열이 있다.
            ArrayList<String> pitches = new ArrayList<>(Arrays.asList(data));
            System.out.println(pitches);  // [138, 129, 142] 출력
        }
    }
    ```
    

- `java.util.Arrays`클래스의 asList 메소드
    - 이미 존재하는 문자열 배열로 ArrayList를 생성 가능

- String 배열 대신 String 자료형을 여러개 전달하여 생성 가능
    
    ```java
    import java.util.ArrayList;
    import java.util.Arrays;
    
    public class Sample {
        public static void main(String[] args) {
            ArrayList<String> pitches = new ArrayList<>(Arrays.asList("138", "129", "142"));
            System.out.println(pitches);
        }
    }
    ```
    

- ****String.join****
    - 콤마를 각 요소 중간에 삽입
        
        ```java
        import java.util.ArrayList;
        import java.util.Arrays;
        
        public class Sample {
            public static void main(String[] args) {
                ArrayList<String> pitches = new ArrayList<>(Arrays.asList("138", "129", "142"));
                String result = "";
                for (int i = 0; i < pitches.size(); i++) {
                    result += pitches.get(i);
                    result += ",";  // 콤마를 추가한다.
                }
                result = result.substring(0, result.length() - 1);  // 마지막 콤마는 제거한다.
                System.out.println(result);  // 138,129,142 출력
            }
        }
        ```
        
        - pitches를 갯수만큼 루프를 돌면서 뒤에 콤마를 더하고 최종적으로 마지막 콤마를 제거하는 방법
    
    - `String.join`을 사용
        
        ```java
        import java.util.ArrayList;
        import java.util.Arrays;
        
        public class Sample {
            public static void main(String[] args) {
                ArrayList<String> pitches = new ArrayList<>(Arrays.asList("138", "129", "142"));
                String result = String.join(",", pitches);
                System.out.println(result);  // 138,129,142 출력
            }
        }
        ```
        
        - `String.join("구분자", 리스트객체)`
            - 리스트의 각 요소에 "구분자"를 삽입하여 하나의 문자열로 만들 수 있음
        - 문자열 배열에도 사용 가능
            
            ```java
            public class Sample {
                public static void main(String[] args) {
                    String[] pitches = new String[]{"138", "129", "142"};
                    String result = String.join(",", pitches);
                    System.out.println(result);  // 138,129,142 출력
                }
            }
            ```
            
        - `String.join`메소드는 Java 8 버전부터 사용

- ****리스트 정렬하기****
    - 순서대로 정렬 → 리스트의 **sort 메소드**를 사용해야 함
        
        ```java
        import java.util.ArrayList;
        import java.util.Arrays;
        import java.util.Comparator;
        
        public class Sample {
            public static void main(String[] args) {
                ArrayList<String> pitches = new ArrayList<>(Arrays.asList("138", "129", "142"));
                pitches.sort(Comparator.naturalOrder());  // 오름차순으로 정렬
                System.out.println(pitches);  // [129, 138, 142] 출력
            }
        }
        ```
        
    
    - sort 메소드에는 정렬기준을 파라미터로 전달
        - 오름차순(순방향) 정렬 - `Comparator.naturalOrder()`
        - 내림차순(역방향) 정렬 - `Comparator.reverseOrder()`
    
    - sort 메소드로 정렬후에 pitches를 출력
        - `[129, 138, 142]`처럼 오름차순으로 정렬되어 출력되는 것을 확인
    - 리스트의 `sort`메소드는 Java 8 버전부터 사용

## ****08. 맵 (Map)****

- 자바의 **맵(Map)**
    - 대응관계를 쉽게 표현할 수 있게 해 주는 자료형
    - Associative array, Hash라고도 불림
    - 맵(Map)은 사전(dictionary)과 비슷
        - **Map은 Key와 Value를 한 쌍으로 갖는 자료형**
    
    - Map은 리스트나 배열처럼 순차적으로(sequential) 해당 요소 값을 구하지 않고 key를 통해 value를 얻음
    - 맵(Map)의 가장 큰 특징
        - key로 value를 얻어낸다는 점

- ****HashMap****
    - ****put****
        - key와 value가 String 형태인 HashMap을 만들고 항목값들을 입력
            
            ```java
            import java.util.HashMap;
            
            public class Sample {
                public static void main(String[] args) {
                    HashMap<String, String> map = new HashMap<>();
                    map.put("people", "사람");
                    map.put("baseball", "야구");
                }
            }
            ```
            
        - HashMap 역시 제네릭스를 이용
            - HashMap 의 제네릭스는 Key, Value 모두 String 타입

- ****get****
    - key에 해당되는 value값을 얻기 위해서
        
        ```java
        System.out.println(map.get("people"));  // "사람" 출력
        ```
        
    - **get** 메소드를 이용하면 value값을 얻을 수 있음
    - 위 예제는 "people" Key에 대응되는 Value 값으로 "사람"이라는 문자열을 출력
    
    - **getOrDefault**
        - 맵의 key에 해당하는 value가 없을 경우
            - get 메소드를 사용하면 다음처럼 null이 리턴
            
            ```java
            System.out.println(map.get("java"));  // null 출력
            ```
            
            - 이때 null 대신 디폴트 값을 얻고 싶은 경우에는 getOrDefault 메소드 사용
            
            ```java
            System.out.println(map.getOrDefault("java", "자바"));  // "자바" 출력
            ```
            

- ****containsKey****
    - 맵(Map)에 해당 키(key)가 있는지를 조사하여 그 결과값을 리턴
        
        ```java
        System.out.println(map.containsKey("people"));  // true 출력
        ```
        
        - "people"이라는 키는 존재하므로 true가 출력

- ****remove****
    - 맵(Map)의 항목을 삭제하는 메소드
    - key값에 해당되는 아이템(key, value)을 삭제한 후 그 value 값을 리턴
        
        ```java
        System.out.println(map.remove("people"));  // "사람" 출력
        ```
        
        - "people"에 해당되는 아이템(people:사람)이 삭제된 후 "사람"이 출력

- ****size****
    - Map의 갯수를 리턴
        
        ```java
        System.out.println(map.size());  // 1 출력
        ```
        
        - "people", "baseball" 두 값을 가지고 있다가 "people"항목이 삭제되었으므로 1이 출력

- ****keySet****
    - 맵(Map)의 모든 Key를 모아서 리턴
        
        ```java
        import java.util.HashMap;
        
        public class Sample {
            public static void main(String[] args) {
                HashMap<String, String> map = new HashMap<>();
                map.put("people", "사람");
                map.put("baseball", "야구");
                System.out.println(map.keySet());  // [baseball, people] 출력
            }
        }
        keySet()
        ```
        
    - `keySet()`
        - Map의 모든 Key를 모아서 Set 자료형으로 리턴
    - Set 자료형은 다음과 같이 List 자료형으로 바꾸어 사용할 수 있음
        
        ```java
        List<String> keyList = new ArrayList<>(map.keySet());
        ```
        
    
    - **LinkedHashMap과 TreeMap**
        - Map의 가장 큰 특징은 순서에 의존하지 않고 key로 value를 가져오는 데 있음
        - 하지만 가끔은 Map에 입력된 순서대로 데이터를 가져오고 싶은 경우도 있고 때로는 입력된 key에 의해 소트된 데이터를 가져오고 싶을 수도 있을 것
        - 이런 경우 LinkedHashMap과 TreeMap을 사용하는 것이 유리
            - LinkedHashMap
                - 입력된 순서대로 데이터 저장
            - TreeMap
                - 입력된 key의 오름차순 순서로 데이터 저장

## ****09. 집합 (Set)****

- **집합 자료형은 어떻게 만들까?**
    - HashSet
        - 집합 자료형 만들기
            
            ```java
            import java.util.Arrays;
            import java.util.HashSet;
            
            public class Sample {
                public static void main(String[] args) {
                    HashSet<String> set = new HashSet<>(Arrays.asList("H", "e", "l", "l", "o"));
                    System.out.println(set);  //  [e, H, l, o] 출력
                }
            }
            ```
            

- **Set 자료형**
    - HashSet, TreeSet, LinkedHashSet 등의 Set 인터페이스를 구현한 자료형
    - 여기서 말하는 Set 자료형은 인터페이스

- **집합 자료형의 특징**
    - 문자열 배열로 HashSet 자료형을 만들었는데 출력된 자료형에는 `l`문자가 하나 빠져 있고 순서도 뒤죽박죽
        - 집합 자료형에는 다음과 같은 2가지 큰 특징이 있기 때문
            - 중복을 허용하지 않는다.
            - 순서가 없다(Unordered).
    - 리스트나 배열은 순서가 있음(ordered)
        - 인덱싱을 통해 자료형의 값을 얻을 수 있음
    - But 집합 자료형은 순서가 없기(unordered) 때문에 인덱싱으로 값을 얻을 수 없음
        - 맵 자료형과 비슷
        - 맵 자료형 역시 순서가 없는 자료형이라 인덱싱을 지원하지 않음
        - 중복을 허용하지 않는 집합 자료형의 특징
            - 자료형의 중복을 제거하기 위한 필터 역할로 종종 사용

- **교집합, 차집합, 합집합 구하기**
    - 집합 자료형을 정말 유용하게 사용하는 경우
        - 교집합, 합집합, 차집합을 구할 때
    - 2개의 집합 자료형을 만든 후 s1은 1부터 6까지의 값을 가지게 되었고, s2는 4부터 9까지의 값을 가지게 되었다.
        
        ```java
        import java.util.Arrays;
        import java.util.HashSet;
        
        public class Sample {
            public static void main(String[] args) {
                HashSet<Integer> s1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6));
                HashSet<Integer> s2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8, 9));
            }
        }
        ```
        
        - 제네릭스로 int를 사용하고 싶은 경우
            - int의 Wrapper 클래스인 Integer를 대신 사용해야 함
    
    - **교집합**
        - **retainAll** 메소드 → 교집합을 간단히 구할 수 있음
        - s1과 s2의 교집합
            - s1의 데이터를 유지하기 위해 s1으로 intersection이라는 HashSet 객체를 Copy하여 생성
            - 만약 intersection 대신 s1에 retainAll 메소드를 사용하면 s1의 내용이 변경될 것임
            - retainAll 메소드로 교집합 수행 후 intersection 출력
                - 교집합에 해당되는 `[4, 5, 6]`이 출력
            
            ```java
            import java.util.Arrays;
            import java.util.HashSet;
            
            public class Sample {
                public static void main(String[] args) {
                    HashSet<Integer> s1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6));
                    HashSet<Integer> s2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8, 9));
            
                    HashSet<Integer> intersection = new HashSet<>(s1);  // s1으로 intersection 생성
                    intersection.retainAll(s2);  // 교집합 수행
                    System.out.println(intersection);  // [4, 5, 6] 출력
                }
            }
            ```
            

- **합집합**
    - **addAll** 메소드 → 합집합 구할 수 있음
    - 4, 5, 6처럼 중복해서 포함된 값은 한 개씩만 표현
        - 합집합의 결과로 `[1, 2, 3, 4, 5, 6, 7, 8, 9]`을 출력
        
        ```java
        import java.util.Arrays;
        import java.util.HashSet;
        
        public class Sample {
            public static void main(String[] args) {
                HashSet<Integer> s1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6));
                HashSet<Integer> s2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8, 9));
        
                HashSet<Integer> union = new HashSet<>(s1);  // s1으로 union 생성
                union.addAll(s2); // 합집합 수행
                System.out.println(union);  // [1, 2, 3, 4, 5, 6, 7, 8, 9] 출력
            }
        }
        ```
        

- 차집합
    - removeAll 메소드 → 차집합 구하는 용도
        - 차집합의 결과로 `[1, 2, 3]` 출력
        
        ```java
        import java.util.Arrays;
        import java.util.HashSet;
        
        public class Sample {
            public static void main(String[] args) {
                HashSet<Integer> s1 = new HashSet<>(Arrays.asList(1, 2, 3, 4, 5, 6));
                HashSet<Integer> s2 = new HashSet<>(Arrays.asList(4, 5, 6, 7, 8, 9));
        
                HashSet<Integer> substract = new HashSet<>(s1);  // s1으로 substract 생성
                substract.removeAll(s2); // 차집합 수행
                System.out.println(substract);  // [1, 2, 3] 출력
            }
        }
        ```
        

- **집합 자료형 관련 메소드**
    - ****값 추가하기(add)****
        - 집합 자료형에 값을 추가할 때 **add 메소드**를 사용
            
            ```java
            import java.util.HashSet;
            
            public class Sample {
                public static void main(String[] args) {
                    HashSet<String> set = new HashSet<>();
                    set.add("Jump");
                    set.add("To");
                    set.add("Java");
                    System.out.println(set);  // [Java, To, Jump] 출력
                }
            }
            ```
            
    - ****값 여러 개 추가하기(addAll)****
        - 여러 개의 값을 한꺼번에 추가할 때 addAll 메소드를 사용
        - 합집합을 구할 때도 addAll을 사용
            
            ```java
            import java.util.Arrays;
            import java.util.HashSet;
            
            public class Sample {
                public static void main(String[] args) {
                    HashSet<String> set = new HashSet<>();
                    set.add("Jump");
                    set.addAll(Arrays.asList("To", "Java"));
                    System.out.println(set);  // [Java, To, Jump] 출력
                }
            }
            ```
            

- ****특정 값 제거하기(remove)****
    - 특정 값을 제거하고 싶을 때 remove 메소드를 사용
        
        ```java
        import java.util.Arrays;
        import java.util.HashSet;
        
        public class Sample {
            public static void main(String[] args) {
                HashSet<String> set = new HashSet<>(Arrays.asList("Jump", "To", "Java"));
                set.remove("To");
                System.out.println(set);  // [Java, Jump] 출력
            }
        }
        ```
        
    
    - **TreeSet과 LinkedHashSet**
        - Set 자료형은 순서가 없다는 특징 있음
        - 하지만 가끔은 Set에 입력된 순서대로 데이터를 가져오고 싶은 경우도 있고, 때로는 오름차순으로 정렬된 데이터를 가져오고 싶을 수도 있음
            - TreeSet과 LinkedHashSet을 사용
                - **TreeSet** - 오름차순으로 값을 정렬하여 저장
                - **LinkedHashSet** - 입력한 순서대로 값을 정렬하여 저장

## ****10. 상수집합 (Enum)****

- **Enum 만들기**
    - 예) 어떤 커피숍에서 판매하는 커피의 종류
        - 아메리카노
        - 아이스 아메리카노
        - 카페라떼
    - 3종류의 커피를 판매한다고 하면 다음과 같이 Enum 으로 상수집합 만들 수 있음
        
        ```java
        enum CoffeeType {
            AMERICANO,
            ICE_AMERICANO,
            CAFE_LATTE
        };
        ```
        
    
    - 정의한 상수 집합 사용
        
        ```java
        public class Sample {
            enum CoffeeType {
                AMERICANO,
                ICE_AMERICANO,
                CAFE_LATTE
            };
        
            public static void main(String[] args) {
                System.out.println(CoffeeType.AMERICANO);  // AMERICANO 출력
                System.out.println(CoffeeType.ICE_AMERICANO);  // ICE_AMERICANO 출력
                System.out.println(CoffeeType.CAFE_LATTE);  // CAFE_LATTE 출력
            }
        }
        ```
        
    
    - 반복문에서 사용
        
        ```java
        public class Sample {
            enum CoffeeType {
                AMERICANO,
                ICE_AMERICANO,
                CAFE_LATTE
            };
        
            public static void main(String[] args) {
                for(CoffeeType type: CoffeeType.values()) {
                    System.out.println(type);  // 순서대로 AMERICANO, ICE_AMERICANO, CAFE_LATTE 출력
                }
            }
        }
        ```
        

- **Enum 은 왜 필요한가?**
    - **Enum 의 장점**
        - 매직넘버(1과 같은 숫자 상수값)를 사용할 때보다 코드가 명확해 짐
            - **매직넘버** : 프로그래밍에서 상수로 선언하지 않은 숫자
        - 잘못된 값을 사용함으로 인해 발생할수 있는 위험성이 사라짐
        - 오늘 판매된 커피의 갯수를 리턴하는 메소드
            - 입력으로 들어온 커피의 종류가 오늘 몇 개 판매되었는지를 리턴하는 메소드
            
            ```java
            /**
             * 오늘 판매된 커피의 갯수를 리턴하는 메소드이다.
             * @param type 커피의 종류 (1: 아메리카노, 2: 아이스 아메리카노, 3: 카페라떼)
             */
            int countSellCoffee(int type) {
                ... 생략 ...
            }
            ```
            
            - 아메리카노의 오늘 판매 갯수를 알기 위해서는 다음과 같이 숫자 1을 넘겨야 함
            - 숫자 1이 아메리카노임을 기억하고 사용해야 한다는 불편함 발생
                
                ```java
                int americano = countSellCoffee(1);
                ```
                
            - 다음과 같이 사용할 경우에도 문제가 발생
                
                ```java
                int result = countSellCoffee(99);  // 99 타입은 존재하지 않으므로 오류가 발생한다.
                ```
                
        - 메소드 변경
            
            ```java
            enum CoffeeType {
                AMERICANO,
                ICE_AMERICANO,
                CAFE_LATTE
            };
            
            /**
             * 오늘 판매된 커피의 갯수를 리턴하는 메소드이다.
             * @param type 커피의 종류 (CoffeType)
             */
            int countSellCoffee(CoffeType type) {
                ... 생략 ...
            }
            ```
            
        
        - 메소드를 변경하면 이 메소드는 숫자 대신 CoffeeType을 파라미터로 사용해야 함
            
            ```java
            int americano = countSellCoffee(CoffeType.AMERICANO);  // 아메리카노의 오늘 판매갯수
            ```
            
            - 숫자 1을 사용했을때 보다 코드가 명확
            - countSellCoffee 메소드에는 CoffeType에 정의된 상수만 전달
                - 엉뚱한 숫자값에 의한 오류가 발생하지 않음

## ****11. 형 변환과 final****

- **형 변환**
    
    ```java
    String num = "123";
    ```
    
    - 자료형은 문자열이지만 그 내용은 숫자로 이루어진 값
        - 문자열을 정수(integer)로 바꿀 수 있음
    - **Integer 클래스**
        - int자료형의 Wrapper 클래스
        - 문자열을 정수로 바꾸고자 할 때 사용
        
        ```java
        public class Sample {
            public static void main(String[] args) {
                String num = "123";
                int n = Integer.parseInt(num);
                System.out.println(n);  // 123 출력
            }
        }
        ```
        
        - 반대로 정수 123을 문자열 "123"으로 바꾸는 방법
            - 정수를 문자열로 바꾸는 가장 쉬운 방법
                - 정수 앞에 빈 문자열(`""`)을 더해 주는 것
            
            ```java
            public class Sample {
                public static void main(String[] args) {
                    int n = 123;
                    String num1 = String.valueOf(n);
                    String num2 = Integer.toString(n);
                    System.out.println(num1);  // 123 출력
                    System.out.println(num2);  // 123 출력
                }
            }
            ```
            
        
        - 소숫점이 포함되어 있는 숫자형태의 문자열
            - `Double.parseDouble`또는 `Float.parseFloat`사용
            
            ```java
            public class Sample {
                public static void main(String[] args) {
                    String num = "123.456";
                    double d = Double.parseDouble(num);
                    System.out.println(d);
                }
            }
            ```
            
        
        - 정수와 실수 사이의 형 변환도 가능
            
            ```java
            public class Sample {
                public static void main(String[] args) {
                    int n1 = 123;
                    double d1 = n1;.  // 정수를 실수로 바꿀때에는 캐스팅이 필요없다.
                    System.out.println(d1);  // 123.0 출력
            
                    double d2 = 123.456;
                    int n2 = (int) d2;. // 실수를 정수로 바꿀때에는 반드시 정수형으로 캐스팅해 주어야 한다.
                    System.out.println(n2);  // 소숫점이 생략된 123 출력
                }
            }
            ```
            
        
        - 실수를 정수로 변환하면 실수의 소숫점은 제거됨
            - 실수 형태의 문자열을 정수로 변경 시 NumberFormatException이 발생하므로 주의
            
            ```java
            public class Sample {
                public static void main(String[] args) {
                    String num = "123.456";
                    int n = Integer.parseInt(num);  // 실수 형태의 문자열을 정수로 변환할 경우 NumberFormatException이 발생한다.
                }
            }
            ```
            

- **final**
    - 자료형에 값을 단 한번만 설정할 수 있게 강제하는 키워드
        - 값을 한 번 설정하면 그 값을 다시 설정할 수 없음
        
        ```java
        public class Sample {
            public static void main(String[] args) {
                final int n = 123;  // final 로 설정하면 값을 바꿀수 없다.
                n = 456;  // 컴파일 에러 발생
            }
        }
        ```
        
    
    - 리스트의 경우도 final로 선언 시 재할당 불가능
        
        ```java
        import java.util.ArrayList;
        import java.util.Arrays;
        
        public class Sample {
            public static void main(String[] args) {
                final ArrayList<String> a = new ArrayList<>(Arrays.asList("a", "b"));
                a = new ArrayList<>(Arrays.asList("c", "d"));  // 컴파일 에러 발생
            }
        }
        ```
        
    
    - final은 프로그램 수행 도중 그 값이 변경되면 안되는 상황에 사용
    
    - **Unmodifiable List**
        - 리스트의 경우 final로 선언 시 리스트에 값을 더하거나(add) 빼는(remove) 것은 가능
            - 재할당만 불가능할 뿐
        - 만약 그 값을 더하거나 빼는 것도 불가능하게 하고 싶은 경우
            - `List.of`
                - 수정이 불가능한 리스트(Unmodifiable List)를 생성해야 함
                
                ```java
                import java.util.List;
                
                public class Sample {
                    public static void main(String[] args) {
                        final List<String> a = List.of("a", "b");
                        a.add("c");  // UnsupportedOperationException 발생
                    }
                }
                ```