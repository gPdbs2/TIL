# JAVA Chapter 3

이해관계자: 익명
작성일시: 2022년 8월 24일 오후 7:37
최종 편집일시: 2022년 8월 26일 오후 11:12

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

- 

## ****08. 맵 (Map)****

- 

## ****09. 집합 (Set)****

- 

## ****10. 상수집합 (Enum)****

- 

## ****11. 형 변환과 final****

-