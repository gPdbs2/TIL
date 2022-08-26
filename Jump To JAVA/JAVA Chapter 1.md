# JAVA Chapter 1

이해관계자: 익명
작성일시: 2022년 8월 18일 오후 6:10
최종 편집일시: 2022년 8월 23일 오후 7:49

# Chapter ****01. 자바란 무엇인가?****

## ****01. 자바에 대하여****

- JAVA
    - 썬 마이크로시스템즈의 제임스 고슬링(James Gosling)과 다른 연구원들이 개발한 객체 지향적 프로그래밍 언어
    - 우리나라 기업에서 사용하는 프로그램의 80% 이상은 자바로 만들어졌다 해도 과언이 아님
    - 우리나라에서 오랜 시간 굳건한 생태계를 구축하고 유지
        - 자바로 만들어진 수많은 라이브러리들이 존재

## ****02. 자바의 특징****

- ****간단하다 (Simple)****
    - 자바는 C++에 가깝지만 훨씬 간단
    - 자바는 고급 언어들에 들어 있는 여러 가지 요소들 중에서 반드시 필요하지 않다고 생각된 부분들은 모두 제거

- ****객체 지향적이다 (Object-oriented)****
    - 자바는 숫자(int, float, long 등)나 논리값(true, false)을 제외한 거의 모든 것이 객체로 구성
    - 실제로 자바는 Object Class에서 모든 Class를 파생

- ****인터프리터 언어이다 (Interpreted)****
    - 자바는 정확하게 말하면 컴파일 언어인 동시에 인터프리터 언어
    - 먼저 텍스트 소스를 컴파일하여 2진 파일(Class 파일)로 만든 다음 자바 런타임이 Class 파일을 Interprete하면서 실행
    - 먼저 시스템에 무관한 2진 파일을 만듦으로써 자바는 컴파일 언어에 가까운 속도와 시스템 독립성을 동시에 얻을 수 있음

- ****강력하다 (robust)****
    - 포인터 연산을 지원하지 않음
    - 이는 잘못된 주소를 가리킬 가능성을 사전에 없앤 것
    - 모든 메모리 접근을 자바 시스템이 관리하고 제한
    - 예외 핸들링을 하여 시스템 붕괴의 우려가 없음
    - resource 관리(garbage collection)를 하는데 사용이 끝난 resource를 시스템이 메모리에서 삭제하는 방식을 채택
        - 메모리 누출에 대한 고민을 프로그래머가 할 필요가 없음

- ****안전하다 (Secured)****
    - 포인터 개념이 없고 유형 정의가 강고
        - 실행 전에 클래스 파일을 이용한 프로그램의 검사가 가능
    - 프로그램 작성 시 자료형 타입에 굉장히 민감
    - 잘못된 코드를 작성하지 않게끔 도와주는 역할
    - 일단 컴파일만 되면 실행 시 오류가 발생하는 경우가 다른 언어에 비해 현저히 낮음
    - 자바의 이런 족쇄 같은 type check는 코드를 매우 명확하게 만들어 줌
    - 컴파일이 되었다면 코드에 결정적인 문제는 없는 것

- ****플랫폼 독립적이다 (Platform independent)****
    - 자바의 실행 파일은 이진 코드(클래스) 파일
        - 자바 런타임이 설치된 시스템에서는 어디서나 자바 프로그램을 실행 가능
    - 많은 특징이 있지만 가장 큰 특징이라면 한번 작성한 프로그램은 os에 상관없이 어디서든 돌려볼 수 있다는 점
        - 자바 프로그램이 Virtual Machine에 의해서 실행되기 때문
    - 처음에 이 방식은 Virtual Machine을 실행시켜서 프로그램을 돌려야 하기 때문에 좀 느리고 부담스러웠음
        - 지금은 하드웨어의 발전과 여러 기술들의 개발로 이러한 단점들이 대부분 사라져버린 상태

- ****멀티 쓰레딩을 지원한다 (Multithreaded)****
    - Multithread를 지원할 경우 하나의 프로그램 단위가 동일한 thread를 동시에 수행 가능
    - 특히 자바는 멀티 프로세서 하드웨어를 지원하도록 설계됨
        - 멀티 CPU 시스템에서 높은 효율 낼 수 있음

- ****동적이다 (Dynamic)****
    - 자바 인터페이스를 이용 시 하나의 모듈을 갱신할 때 다른 모듈을 모두 갱신할 필요 없음
        - 인터페이스가 모든 인스턴스 변수와 도구의 실행문을 배제한 채 객체 간의 상호 작용을 정의하기 때문

## ****03. Hello World 출력****

- ****JDK 설치****
    - 개발 환경 : 자바로 프로그램을 만들 수 있는 컴퓨팅 환경
    - 프로그램 소스를 작성하는 툴, 작성한 소스를 컴파일 하는 프로그램 등을 설치
    - JDK : `Java Development Kit`
    - JDK 다운로드 URL
        - • [https://www.oracle.com/java/technologies/downloads/](https://www.oracle.com/java/technologies/downloads/)
        - 구글 검색창에서 "JDK Download" 로 검색
        - 윈도우즈 환경이라면 msi 파일로 설치하는 것을 추천
        
        ![Untitled](JAVA%20Chapter%201%2054c37eef3fd04f51ad2cbd1e93f11ecd/Untitled.png)
        
    
    - JDK는 default로 설치 시 아마도 다음과 비슷한 디렉터리에 설치될 것
        - c:\program files\java\jdk-17.0.1
        - JDK 설치 버전에 따라 directory명 다름
    - 본인의 JDK 설치 디렉터리를 기억할 것
        - 설치한 JDK 디렉터리는 앞으로 진행할 설명에서 필요
    - JDK 설치가 완료되었다면 자바 프로그램 작성을 도와주는 도구인 인텔리제이(IntelliJ) 설치
    - IDE(Intergrated Development Environment), 통합 개발 환경
        - 프로그램 작성을 도와주는 툴들
    - 자바 프로그래밍을 도와주는 IDE 중 가장 많이 추천되는 툴은 IntelliJ

- ****자바 소스와 컴파일****
    - JDK를 설치했다면 JDK가 설치된 디렉터리의 bin이라는 하위 디렉터리에 javac.exe와 java.exe 파일이 저장되어 있을 것
    - java.exe만 있고 javac.exe가 없다면 JDK가 아닌 JRE를 설치한 것이므로 다시 JDK를 설치
        - JRE : `Java Runtime Environment` , JDK보다는 작은 개념
            - 자바가 실행될 수 있는 최소한의 파일들이 설치되어 있는 환경
            - JRE에는 javac.exe와 같은 자바 소스를 컴파일하기 위한 도구는 설치되지 않음
    - javac : java compiler
        - 자바 파일을 컴파일할 때 사용하는 것
    - 컴파일 : 프로그래머가 작성한 소스 코드를 컴퓨터가 이해할 수 있는 말(기계어)로 바꾸는 행위
    - 자바 파일 (자바 소스) :  자바 프로그램에 의해 `.java`라는 확장자를 가진 파일로 저장된 파일
    - 자바로 작성한 파일을 실행하기 위해서는 두 번의 단계를 거쳐야 함
        - `.java`파일을 `.class`파일로 바꾸어 주는 컴파일 단계
        - `.class`파일을 실행하는 단계
    - 프로그램 실행 과정
        
        ![Untitled](JAVA%20Chapter%201%2054c37eef3fd04f51ad2cbd1e93f11ecd/Untitled%201.png)
        
        - Compiler = javac.exe   /   Java VM = java.exe
        - 위 그림 서술
            1. 소스 코드(MyPrograme.java)를 작성
            2. 컴파일러(Compiler)는 자바 소스 코드를 이용하여 클래스 파일(MyProgram.class)을 생성 
                1. 컴파일 된 클래스 파일은 Java VM(Java Virtual Machine)이 인식할 수 있는 바이너리 파일
            3. Java VM(JVM)은 클래스 파일의 바이너리 코드를 해석하여 프로그램을 수행
            4. MyProgram 수행 결과가 컴퓨터에 반영
    
    - 왜 자바는 컴파일을 하고 나면 exe 파일이 아닌 class 파일이 생성될까?
        - `c` 또는 `c++`등으로 작성된 프로그램은 최종 결과물로 exe 파일 만들어 냄
        - 물론 java도 exe 프로그램으로 만들어 낼 수 있음
        - 다만 JVM이 exe에 포함되는 형식으로 가능
            - exe 파일이 무척 커진다는 단점 발생
    
    - `c`, `c++`등의 언어에서 만들어진 실행 파일
        - JVM같은 중간 단계를 거치지 않음 → 빠른 속도로 수행 가능
        - 하지만 운영체제마다 별도의 실행 파일을 작성해야 한다는 단점 존재
    
    - 자바는 JVM이라는 중간 단계가 있음
        - C 등의 언어보다 속도 느림
        - 하지만 한 번 작성한 클래스 파일은 어떤 OS에서라도 사용 가능

- ****따라해 보기****
    - 명령창 열기
        - 시작 → “프로그램 및 파일 검색” 입력창에 ‘cmd’ 라고 입력 후 Enter
        - 또는 윈도우+R 입력 후 나오는 팝업창에 ‘cmd’ 입력
        
        ```basic
        C:\Users\pahkey>
        ```
        
    - javac 명령어 수행
        
        ```basic
        C:\Users\pahkey>javac
        'javac'은(는) 내부 또는 외부 명령, 실행할 수 있는 프로그램, 또는
        배치 파일이 아닙니다.
        ```
        
    - 위와 같은 결과가 나온다면
        - set 명령어를 이용하여 PATH 변수에 jdk/bin 디렉토리 추가
        
        ```basic
        C:\Users\pahkey>set PATH=%PATH%;"C:\program files\java\jdk-17.0.1\bin"
        ```
        
        - 이전에 기억해 둔 JDK 디렉터리를 사용해야 한다.
    
    ```basic
    C:\Users\pahkey>javac
    Usage: javac <options> <source files>
    where possible options include:
      -g                         Generate all debugging info
      -g:none                    Generate no debugging info
      -g:{lines,vars,source}     Generate only some debugging info
    
    ... 생략 ...
    ```
    
    - 명령창을 닫고 다시 열면 PATH 변수가 사라짐
    - PATH 값을 영구설정
        - "내컴퓨터" --> 고급설정 --> 환경변수 --> PATH 값에 위에서 사용한 jdk/bin경로(예:`C:\program files\java\jdk-17.0.1\bin`)를 추가
    
    - 자바파일(`.java`) 작성
        - HelloWorld.java
        
        ```java
        C:\Users\pahkey>copy con HelloWorld.java
        class HelloWorld {
        }
        ^Z
        ```
        
    - `copy con`명령을 이용해서 java 파일을 작성
        - 파일에 더 이상 적을 내용이 없을 때 ^Z (Ctrl + Z)를 입력하면 파일 생성
        
    - HelloWorld.java
        
        ```java
        class HelloWorld {
        }
        ```
        
    
    - 자바파일을 컴파일
        
        ```java
        C:\Users\pahkey>javac HelloWorld.java
        ```
        
    
    - dir 명령어로 class 파일이 생성되었는지 확인
        
        ```java
        C:\Users\pahkey>dir HelloWorld.class
         C 드라이브의 볼륨에는 이름이 없습니다.
         볼륨 일련 번호: 3ACB-12C2
        
         C:\Users\pahkey 디렉터리
        
        2014-04-11  오후 04:34               194 HelloWorld.class
                       1개 파일                 194 바이트
                       0개 디렉터리  47,143,202,816 바이트 남음
        ```
        
    
    - type 명령어로 클래스 파일의 내용 확인
        - type 명령어 → 파일의 내용을 확인할 수 있는 시스템 명령어
        - 생성한 클래스파일을 실행
            - java.exe : 클래스를 실행시키는 명령어
            
            ```java
            C:\Users\pahkey>java HelloWorld
            오류: HelloWorld 클래스에서 기본 메소드를 찾을 수 없습니다. 다음 형식으로 기본메소드를 정의하십시오.
               public static void main(String[] args)
            또는 JavaFX 응용 프로그램 클래스는 javafx.application.Application을(를) 확장해야 합니다.
            ```
            
        
        - 클래스 파일을 실행
            - `java 클래스파일명`과 같이 실행
        - 단, 클래스파일명에서 `.class` 확장자 부분은 제외하고 이름만 입력하여 실행

- ****인텔리제이 설치****
    - 다운로드 URL
        - [https://www.jetbrains.com/ko-kr/idea/download/](https://www.jetbrains.com/ko-kr/idea/download/)
        - community version 설치

- ****main 메소드****
    - HelloWorld 클래스를 실행하려면 main 메소드를 작성해야 함
    - 메소드(method)
        - 함수(function)와 동일한 개념
        - 다만 클래스 내의 함수는 보통 함수라고 말하지 않고 메소드라고 함
        - 자바는 모든 것이 클래스 기반
            - 자바에서 사용되는 함수는 모두 메소드
        - HelloWorld.java 파일에 main 메소드 추가
        
        ```java
        public class HelloWorld {
            public static void main(String[] args) {
                System.out.println("Hello World");
            }
        }
        ```
        
    
    - public
        - 메소드의 접근 제어자
        - 누구나 이 메소드에 접근할 수 있다는 의미
    - static
        - 이 메소드는 인스턴스 생성 없이 실행 가능
    - void
        - 메소드의 리턴 값 없음
        - 사전적으로 "텅 빈" 이라는 뜻
    - String[]
        - 문자열을 나타내는 자바의 자료형
        - `[]`가 있는 경우
            - 한 개가 아닌 여러 개의 값으로 이루어진 배열임을 의미
    - args
        - String[] 자료형에 대한 변수명
    - System.out.println
        - 표준 출력으로 데이터를 보내는 자바의 내장 메소드
        - 문자열을 화면에 출력
    
    - main 메소드는 프로그램 실행을 위해서 반드시 필요
    - 꼭 위와 같은 형태의 main 메소드만 가능
        - 일종의 자바의 규칙임
    
    - 프로그램 실행
        - Run → Run → HelloWorld
        - 출력 결과
        
        ```java
        Hello World
        
        Process finished with exit code 0
        ```
        
        - 인텔리제이에서 작성한 자바 파일을 Run 명령으로 실행
            - .class 파일을 만드는 컴파일 과정(javac.exe)과 실행 과정(java.exe)자동 진행

## ****04. 자바에 대하여****

- **클래스 생성**
    - GuGu 클래스를 생성
    
    ```java
    public class GuGu {
    }
    ```
    

- ****main 메소드****
    - GuGu 클래스를 실행할 수 있는 main 메소드 작성
    
    ```java
    public class GuGu {
        public static void main(String[] args) {
        }
    }
    ```
    

- ****변수****
    - main 메소드에 문장 추가
    
    ```java
    public class GuGu {
        public static void main(String[] args) {
            int n;
        }
    }
    ```
    
    - int : 정수를 의미하는 예약어
    - n : 변수
    - 세미콜론(;) : 문장이 종료되었음을 의미
        - 세미콜론을 생략하면 컴파일 오류 발생
        - 문장의 끝에는 항상 세미콜론이 있어야 함
    - 위 문장의 의미 : n 변수에 정수 값을 저장할 수 있음
    - 변수 n에 정수값을 저장(대입)
        - 대입 연산자(`=`) 이용
        
        ```java
        n = 5;
        ```
        
        - 자바 프로그래밍도 수학과 마찬가지로 변수를 사용하고 변수에 그 값을 할당 가능
        - But 약간의 차이점 존재
            - `int`와 같이 변수명 앞에 뭔가 붙어있다는 점
        - int
            - integer(정수)의 약자
            - 자바에서는 정수를 나타내는 자료형
        
        - 변수명 앞에 있는 자료형
            - 변수에 저장되는 값(자료)들이 어떤 형태(형)인지를 나타내는 역할
            - 자료형 → 자료(값)의 형태를 의미하는 말
        
        - n 변수를 int 자료형으로 선언 시 n 변수에는 정수값만을 대입 가능
            
            ```java
            int n;
            ```
            
        
        - 변수 n은 정수만을 허용
            - 4라는 값은 대입이 가능
            - But "123"과 같은 문자열은 대입 시 컴파일 오류 발생
            
            ```java
            public class GuGu {
                public static void main(String[] args) {
                    int n;
                    n = 4;  // OK
                    n = "123";  // 컴파일 오류
                }
            }
            ```
            
        
        - 주석(Comment)
            - `//`부터 시작되는 문장
            - 프로그램 동작과는 전혀 상관이 없는 문장
            - 프로그래머가 코드에 대한 설명을 달아 놓기 위해 사용
        
        - 구구단 2단 구현
            
            ```java
            public class GuGu {
                public static void main(String[] args) {
                    int n = 2;
                }
            }
            ```
            
        - `int n = 2`처럼 변수 선언과 동시에 값 할당 가능
        - n 변수에 2라는 정수값이 저장된 것
            
            ```java
            public class GuGu {
                public static void main(String[] args) {
                    int n = 2;
            
                    System.out.println(n*1);
                    System.out.println(n*2);
                    System.out.println(n*3);
                    System.out.println(n*4);
                    System.out.println(n*5);
                    System.out.println(n*6);
                    System.out.println(n*7);
                    System.out.println(n*8);
                    System.out.println(n*9);
                }
            }
            ```
            
        - GuGu 클래스를 실행
            - 인텔리제이 메뉴에서 `Run -> Run -> GuGu`
        - 3단 구현 시
            - n의 값을 3으로 변경 후 실행

- ****메소드****
    - 2단부터 9단까지의 결과를 모두 한번에 보고 싶을 때
    - 한 개의 숫자를 입력으로 받아 그 숫자에 대한 구구단을 출력하는 메소드
    - dan 메소드가 추가된 GuGu 클래스
    
    ```java
    public class GuGu {
        public void dan(int n) {
            System.out.println(n*1);
            System.out.println(n*2);
            System.out.println(n*3);
            System.out.println(n*4);
            System.out.println(n*5);
            System.out.println(n*6);
            System.out.println(n*7);
            System.out.println(n*8);
            System.out.println(n*9);
        }
    }
    ```
    
    - main 메소드에 구현했던 내용이 dan 메소드로 옮겨져 있음
    - dan 메소드
        - 입력으로 정수값을 받아 1부터 9까지의 값을 곱한 값을 출력하는 메소드
    - 메소드의 가장 중요한 부분은 바로 입력과 출력
    - dan 메소드의 입력과 출력
        - 입력 - 정수 자료형 1개 (int n)
        - 출력 - 없음 (void)
    - 메소드는 이러한 입출력을 반드시 선언
    
    ```java
    public void dan(int n) {
            (... 생략 ...)
        }
    ```
    
    - public으로 선언 → 이 메소드는 어떤 곳에서든 호출 가능
    - void → 출력값(리턴값)이 없음
    - dan → 메소드의 이름
    - `(int n)`  → 입력 항목
    - 출력은 반드시 하나지만 입력은 여러 개가 올 수 있음
        - 괄호() 이용하여 여러 개를 선언할 수 있게 되어 있음
        - 입력 항목이 2개일 경우
        
        ```java
        public void dan(int n, int m) {
                (... 생략 ...)
            }
        ```
        
    - 중괄호로 묶인 블록(`{ ... }`)
        - 메소드의 내용

- ****객체****
    - GuGu클래스는 반드시 main 메소드부터 시작
        - main 메소드에서 dan 메소드 호출
        
        ```java
        (... 생략 ...)
            public static void main(String[] args) {
                int n = 3;
                GuGu gugu = new GuGu();  // GuGu 클래스의 객체 생성
                gugu.dan(n);  // 객체를 통해 dan 메소드 호출
            }
        (... 생략 ...)
        ```
        
        - GuGu 클래스의 객체 만들기
            - new 키워드를 이용
        
        ```java
        GuGu gugu = new GuGu();
        ```
        
    - `GuGu gugu`문장
        - gugu가 GuGu 클래스의 자료형임을 나타냄
        - gugu변수에는 GuGu 클래스로 생성한 객체만 대입 가능
    
    - gugu 객체를 생성 시
        - gugu 객체를 통해 GuGu 클래스의 dan 메소드 사용 가능
        
    - 객체를 통해 클래스의 메소드에 접근
        - 도트 연산자(.) 이용
        
        ```java
        gugu.dan(n);
        ```
        
    
    - gugu 객체를 통해 dan 메소드를 호출
        - 2단부터 9단까지 전부 출력 가능
        
        ```java
        public class GuGu {
            public void dan(int n) {
                System.out.println(n*1);
                System.out.println(n*2);
                System.out.println(n*3);
                System.out.println(n*4);
                System.out.println(n*5);
                System.out.println(n*6);
                System.out.println(n*7);
                System.out.println(n*8);
                System.out.println(n*9);
            }
        
            public static void main(String[] args) {
                GuGu gugu = new GuGu();
                gugu.dan(2);
                gugu.dan(3);
                gugu.dan(4);
                gugu.dan(5);
                gugu.dan(6);
                gugu.dan(7);
                gugu.dan(8);
                gugu.dan(9);
            }
        }
        ```
        

- **static 메소드**
    - GuGu 클래스의 dan 메소드를 호출
        - GuGu 클래스의 객체를 먼저 생성 후
        - 그 객체의 메소드인 dan 메소드를 호출
    - dan 메소드를 main 메소드처럼 static으로 선언
        - 객체 생성 없이 메소드 호출만으로 가능
    
    ```java
    public class GuGu {
        public static void dan(int n) {
            (... 생략 ...)
        }
    
        public static void main(String[] args) {
            dan(2);
        }
    }
    ```
    

- ****for 문****
    - dan 메소드를 개선
    
    ```java
    public void dan(int n) {
            System.out.println(n*1);
            System.out.println(n*2);
            System.out.println(n*3);
            System.out.println(n*4);
            System.out.println(n*5);
            System.out.println(n*6);
            System.out.println(n*7);
            System.out.println(n*8);
            System.out.println(n*9);
        }
    ```
    
    - 1부터 9까지 숫자를 반복
        - for 문을 사용
        
        ```java
        for(int i=1; i<10; i++) {
            System.out.println(i);
        }
        ```
        
    
    - for문
        - 세미콜론(;)을 구분자로 세 부분(초기치, 조건문, 증가치)으로 나뉨
        
        ```java
        for(초기치; 조건문; 증가치) {
            (... 수행문 ...)
        }
        ```
        
        - 초기치 → `int i=1`
        - 조건문 → `i<10`
        - 증가치 → `i++`
        - 해석
            - 정수 `i`값이 1부터 시작하여 10보다 작을 때 까지 i값을 1 만큼씩 증가
    
    - dan 메소드에 for문을 적용
        
        ```java
        public class GuGu {
            public void dan(int n) {
                for (int i = 1; i < 10; i++) {   // i에 1~9 까지의 값이 반복하여 대입된다.
                    System.out.println(n * i);
                }
            }
        
            public static void main(String[] args) {
                GuGu gugu = new GuGu();
                gugu.dan(2);
                gugu.dan(3);
                gugu.dan(4);
                gugu.dan(5);
                gugu.dan(6);
                gugu.dan(7);
                gugu.dan(8);
                gugu.dan(9);
            }
        }
        ```
        
    
    - main 메소드 for문 적용
        
        ```java
        public class GuGu {
            public void dan(int n) {
                for (int i = 1; i < 10; i++) {
                    System.out.println(n * i);
                }
            }
        
            public static void main(String[] args) {
                GuGu gugu = new GuGu();
                for (int i = 2; i < 10; i++) {   // i에 2~9 까지의 값이 반복하여 대입된다.
                    gugu.dan(i);
                }
            }
        }
        ```
        

- ****구구단 완성****
    - 완성된 구구단 프로그램
    - *GuGu.java*
        
        ```java
        public class GuGu {
            public void dan(int n) {
                for (int i = 1; i < 10; i++) {
                    System.out.println(n * i);
                }
            }
        
            public static void main(String[] args) {
                GuGu gugu = new GuGu();
                for (int i = 2; i < 10; i++) { 
                    gugu.dan(i);
                }
            }
        }
        ```