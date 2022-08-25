# JAVA Chapter 3

이해관계자: 익명
작성일시: 2022년 8월 24일 오후 7:37
최종 편집일시: 2022년 8월 25일 오후 7:53

# Chapter ****03. 자료형****

- **자료형**
    - 프로그래밍을 할 때 쓰이는 숫자, 문자열 등의 자료 형태로 사용하는 그 모든 것
    - 프로그램의 가장 기본이 되고 핵심적인 단위가 되는 것
    - 자료형을 충분히 이해하지 않고 프로그래밍을 시작하려는 것
        - 기초 공사가 마무리되지 않은 상태에서 빌딩을 세우는 것
    - 

## ****01. 숫자 (Number)****

- **정수**
    - 자료형 : int, long
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
            - `8764827384923849L`과 같이 `L`접미사(또는 소문자 `l`, 소문자 'l'은 숫자 1과 비슷하게 보이므로 추천하지 않는다.)를 붙여 주어야 함
            - 만약 큰 숫자에 'L'과 같은 접미사를 누락 시 컴파일 에러 발생

- **실수**
    - 자료형 : float, double
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

- 
    - 

## ****05. StringBuffer****

- 

## ****06. 배열 (Array)****

- 

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