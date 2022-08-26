# JAVA Chapter 2

이해관계자: 익명
작성일시: 2022년 8월 23일 오후 7:49
최종 편집일시: 2022년 8월 24일 오후 7:36

# Chapter ****02. 자바 시작하기****

## ****01. 자바 소스코드의 구조****

- **JAVA 소스코드의 구조**
    - *클래스명.java*
    
    ```java
    /* 클래스 블록 */
    public class 클래스명 {
    
        /* 메소드 블록 */
        [public|private|protected] [static] (리턴자료형|void) 메소드명1(입력자료형 매개변수, ...) {
            명령문(statement);
            ...
        }
    
        /* 메소드 블록 */
        [public|private|protected] [static] (리턴자료형|void) 메소드명2(입력자료형 매개변수, ...) {
            명령문(statement);
            ...
        }
        ...
    }
    ```
    
    - class 블록
        - 소스코드의 가장 바깥쪽 영역
    - 클래스명은 원하는 이름으로 지을 수 있음
        - 단, 클래스명은 소스파일의 이름(*클래스명.java*)과 동일하게 사용되어야 함
        - 참고 : public 클래스
    - class 블록은 메소드 블록들을 포함함
    - `[public|private|protected]`
        - 참고 : 접근 제어자
        - public, private, protected 또는 아무것도 오지 않을 수 있다
    - `[static]`
        - 참고 : 정적메소드와 변수
        - static 키워드가 올 수도 있고 오지 않을 수도 있다
    - `(리턴자료형|void)`
        - 메소드가 실행된 후 리턴되는 값의 자료형
        - 리턴값이 있을 경우에는 반드시 리턴 자료형을 표기
        - 리턴값이 없는 경우라면 void 로 표기
        - 둘 다 생략할 수는 없고 void 또는 리턴자료형이 반드시 있어야 함
    - 메소드명은 원하는 이름으로 지을 수 있음
    - 메소드 명 이후의 괄호`()`안의 값 : 메소드의 입력 인자
        - 입력 인자의 갯수는 제한 X
        - 입력 인자는 "입력자료형"+"매개변수명" 형태
    - 클래스 내에는 이러한 메소드들이 여러  올 수 있음

- **소스코드의 예**
    - *Sample.java*
    
    ```java
    public class Sample {
        public static void main(String[] args) {
            System.out.println("Hello java");
        }
    }
    ```
    

- **클래스 블록**
    - 소스코드의 가장 바깥쪽은 클래스(class) 블록
    
    ```java
    public class Sample {
        (... 생략 ...)
    }
    ```
    
    - 클래스 블록은 중괄호(`{}`)로 둘러싸야 함
        - `{` - 블록의 시작
        - `}` - 블록의 끝
    
    - public
        - 자바의 접근제어자
        - 어디서든 이 클래스에 접근할 수 있음
    - class → 클래스 블록을 만드는 키워드

- **메소드 블록**
    - 클래스 블록 내에 메소드 블록 존재
    
    ```java
    public class Sample {
        public static void main(String[] args) {
            (... 생략 ...)
        }
    }
    ```
    
    - 메소드 블록 역시 중괄호로 영역 구분
        - static
            - 메소드에 static 키워드가 붙을 경우 이 메소드는 클래스 메소드가 되어 객체를 만들지 않아도 "클래스명.메소드명" 형태로 호출 가능
        - void
            - 메소드의 리턴타입 중 하나로 void는 리턴값이 없음을 의미
        - String[] args
            - 메소드의 매개 변수
            - args
                - `String[]`배열 자료형
                - 인수를 의미하는 arguments의 약어로 관례적 이름
                - 다른 이름을 사용해도 상관없음

- ****명령문 (Statement)****
    - 메소드 블록 안에는 명령문(Statement) 존재
    
    ```java
    public class Sample {
        public static void main(String[] args) {
            System.out.println("Hello java");
        }
    }
    ```
    
    - 명령문(Statement)
        - 컴퓨터에 무언가 일을 시키는 문장
        - 반드시 세미콜론(`;`)을 붙여 문장의 끝을 표시
        - 메소드 블록 안에는 여러 개의 명령문이 있을 수 있음

## ****02. 변수와 자료형****

- ****변수명****
    
    ```java
    int a;
    String b;
    ```
    
    - 변수명은 마음대로 지을 수 있음
    - 단, 변수의 이름을 지을 때는 다음과 같이 지켜야 할 몇 가지 규칙 존재
        - 변수명은 숫자로 시작할 수 없다.
        - _(underscore) 와 $ 문자 이외의 특수문자는 사용할 수 없다.
        - 자바의 키워드는 변수명으로 사용할 수 없다. (예: int, class, return 등)
    - *[참고] 자바의 키워드*
        
        ```java
        abstract  continue  for         new        switch
        assert    default   goto        package    synchronized
        boolean   do        if          private    this
        break     double    implements  protected  throw
        byte      else      import      public     throws
        case      enum      instanceof  return     transient
        catch     extends   int         short      try
        char      final     interface   static     void
        class     finally   long        strictfp   volatile
        const     float     native      super      while
        ```
        
    
    - 변수명을 잘못 사용한 예
        
        ```java
        int 1st;   // 변수명은 숫자로 시작할 수 없다.
        int a#;    // 변수명에 특수문자를 사용할 수 없다.
        int class; // 키워드를 변수명으로 사용할 수 없다.
        ```
        

- ****자료형 (Type)****
    - 변수명 앞의 int, String 등
    - `int a;`  해석
        - 변수 b는 String 자료형 변수
        - 즉, b라는 변수에는 String 자료형 값(예: "a", "hello" 등의 문자열)만 담을 수 있음

- **변수에 값 대입하기**
    - 변수 선언 후 변수에 값 대입 가능
        
        ```java
        int a;
        String b;
        
        a = 1;
        b = "hello java";
        ```
        
    - 변수에 값을 대입할 때
        - `=`(assignment) 기호를 사용
    - 변수를 선언함과 동시에 값을 대입할 수도 있음
        
        ```java
        int a = 1;
        String b = "hello java";
        ```
        
    - int 자료형 변수인 a에 문자열을 대입 시
        
        ```java
        int a = "Hello java";
        
        // IDE에서는 다음과 같은 오류메시지 제공
        Type mismatch: cannot convert from String to int
        ```
        
        - String자료형을 int자료형으로 사용할 수 없다는 오류

- **자주 쓰이는 자료형**
    - 자바에서 가장 많이 사용되는 자료형
        - **int**
        - **long**
        - **double**
        - **boolean**
        - **char**
        - **String**
        - **StringBuffer**
        - **List**
        - **Map**
        - **Set**
    
    - StringBuffer, List 자료형에 해당되는 변수
        
        ```java
        StringBuffer sb;
        List myList;
        ```
        
        - "sb 변수는 StringBuffer 자료형 변수이다. sb 변수에는 StringBuffer 자료형에 해당하는 값만 담을 수 있다.",
        - "myList 변수는 List 자료형 변수이다. myList 변수에는 List 자료형에 해당하는 값만 담을 수 있다.”

- **사용자 정의 자료형**
    - 사용자가 직접 자료형을 만들 수도 있음
        - Animal 이라는 클래스를 만들기
        
        ```java
        class Animal {
        }
        ```
        
        - Animal 자료형 변수 만들기
        
        ```java
        Animal cat;
        ```
        
        - "cat 이라는 변수는 Animal 자료형 변수이다. “
        - “cat이라는 변수에는 Animal 자료형에 해당되는 값만 담을 수 있다.”

## ****03. 명명 규칙****

- ****클래스 명****
    - 자바 프로그램은 클래스단위
    - 자바 프로그램을 만드는 것은 자바 클래스를 만드는 것과 같음
    - 자바 클래스의 이름은 사실 아무렇게나 지어도 되긴 하지만 관행적으로 여겨지는 규칙 존재
        - 클래스명은 명사로 함
        - 여러 개의 단어가 섞이는 경우 각 단어의 첫번째 문자는 대문자이어야 함(CamelCase라고도 한다)
        
        ```java
        class Cookie {}
        class ChocoCookie {}
        ```
        

- **메소드 명**
    - 메소드명은 동사로 함
    - 클래스명과 마찬가지로 여러 개의 단어가 섞이는 경우 각 단어의 첫번째 문자는 대문자이어야 함
    - 단, 처음 시작하는 문자는 항상 소문자로 시작
    
    ```java
    run();
    runFast();
    getBackground();
    ```
    

- **변수 명**
    - 변수 이름은 짧지만 의미가 있어야 함
        - (변수명을 통해 변수의 사용 의도를 알 수 있게 지어야 함)
    - 순서를 의미하는 임시적인 정수의 변수명은 i, j, k, m, n을 사용
        - (문자의 경우 c, d, e 등을 사용)
    - 변수명에 `_`, `$` 기호를 사용할 수 있지만 시작 문자로 사용하지 않음

## ****04. 주석****

- **주석(Comment)**
    - 프로그램 소스코드에 프로그래머의 의견이나 설명을 적은 것
    - 프로그램 소스에 삽입하더라도 프로그램 수행에 전혀 영향을 끼치지 않음
    - 컴파일 시 주석은 자동으로 제외되기 때문

- **두 가지 주석**
    - 블록 주석
        
        ```java
        /*
        프로그램의 저작권
        
        이 프로그램의 저작권은 홍길동에게 있습니다.
        Copyright 2013.
        */
        public class MyProgram {
            ...
        ```
        
        - `/*` : 블록주석의 시작
        - `*/` : 블록주석의 끝
        - 소스 코드내에서 한 블록(메소드, 클래스, 일정부분)에 대한 설명을 할 때 주로 사용
    - 라인 주석
        
        ```java
        int age; // 동물의 나이
        ```
        
        - `//`기호가 시작된 곳부터 해당 라인의 끝까지가 주석문
        - 코드의 특정부분(한 라인)에 대한 설명이 필요할 경우 사용

- **주석이 적은 코드, 많은 코드, 어떤 게 좋은 코드인가?**
    - 주석이 없는 코드가 좋다
        - "Simple Code”
            - 주석이 있을 필요가 없을 정도로 이해하기 쉽고 누가 봐도 명확한 코드
        - 주석은 이해하기 어려운 곳에 주로 작성
        - 하지만 Simple Code를 작성할 수 없는 입장이라면 주석은 어쩔 수 없이 꼭 필요

- **적절하지 못한 주석**
    - 누구나 알고 있는 뻔한 내용의 주석을 다는 것은 소스코드를 지저분하게 만듦
    
    ```java
    a++; // a의 값을 증가
    ```
    

- **주석 사용 시 주의할 점**
    - 주석의 내용도 소스코드가 변경되면 업데이트 되어야 함
    - 소스코드에 달린 엉뚱한 주석문은 소스코드를 읽는 다른 이에게 엄청난 혼란 야기

- **임시 백업**
    - 주석을 사용하는 또 다른 이유
        - 현재 작성한 소스코드의 특정 부분을 잠시 사용하지 않게 만들고 싶은 경우에도 사용
    - 기존의 코드보다 좀 더 업그레이드 된 코드를 작성하고 싶은 경우 기존 코드를 모두 삭제하고 시작하는 것이 아니라 잠시 주석처리하고 새로운 코드를 만드는 것이 유리
        - 주석처리한 기존코드를 참고할 수도 있고 최악의 경우에 기존의 코드로 쉽게 돌아갈 수 있기 때문
            - 주석만 해제하면 됨