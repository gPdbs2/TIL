# JAVA Chapter 5

문서 유형: 학습 자료
이해관계자: 익명
작성일시: 2022년 9월 3일 오후 4:44
최종 편집일시: 2022년 9월 4일 오후 4:32

# Chapter ****05. 객체지향 프로그래밍****

- 자바는 객체지향(Object Oriented) 프로그래밍 언어
    
    
- 객체지향에는 클래스, 객체, 인스턴스, 상속, 인터페이스, 다형성, 추상화 등의 많은 개념들이 존재

## ****01. 객체지향 프로그램이란?****

- 계산기 만들기
    - 계산기는 이전에 계산한 결괏값을 항상 메모리 어딘가에 저장하고 있어야 함
    - 계산기의 "더하기" 기능을 구현한 코드
        - add 메소드
            - 매개변수 num으로 받은 값을 이전에 계산한 결괏값에 더한 후 돌려주는 메소드
            - result 전역 변수(static) : 이전에 계산한 결괏값 유지
        
        ```java
        class Calculator {
            static int result = 0;
        
            static int add(int num) {
                result += num;
                return result;
            }
        }
        
        public class Sample {
            public static void main(String[] args) {
                System.out.println(Calculator.add(3));
                System.out.println(Calculator.add(4));
            }
        }
        
        // 결과값
        3 
        7
        ```
        
    
    - 만일 Sample 클래스에서 2대의 계산기가 필요한 상황이 발생할 경우
        - 각 계산기는 각각의 결괏값을 유지해야 함
            - Calculator 클래스 하나만으로는 결괏값 따로 유지할 수 없음
            
    - 이런 상황을 해결하려면 클래스를 각각 따로 만들어야 함
        
        ```java
        class Calculator1 {
            static int result = 0;
        
            static int add(int num) {
                result += num;
                return result;
            }
        }
        
        class Calculator2 {
            static int result = 0;
        
            static int add(int num) {
                result += num;
                return result;
            }
        }
        
        public class Sample {
            public static void main(String[] args) {
                System.out.println(Calculator1.add(3));
                System.out.println(Calculator1.add(4));
        
                System.out.println(Calculator2.add(3));
                System.out.println(Calculator2.add(7));
            }
        }
        
        // 결과값
        3
        7
        3
        10
        ```
        
        - 똑같은 일을 하는 Calculator1과 Calculator2 클래스 생성
    
    - 계산기가 3개, 5개, 10개로 점점 더 많이 필요해질 경우
        - 객체를 사용하면 간단하게 해결
            - Calculator 클래스의 static 키워드를 모두 삭제
            
            ```java
            class Calculator {
                int result = 0;
            
                int add(int num) {
                    result += num;
                    return result;
                }
            }
            
            public class Sample {
                public static void main(String[] args) {
                    Calculator cal1 = new Calculator();  // 계산기1 객체를 생성
                    Calculator cal2 = new Calculator();  // 계산기2 객체를 생성
            
                    System.out.println(cal1.add(3));
                    System.out.println(cal1.add(4));
            
                    System.out.println(cal2.add(3));
                    System.out.println(cal2.add(7));
                }
            }
            
            // 출력값은 클래스 2개 사용했을 때와 동일
            3
            7
            3
            10
            ```
            
        - Calculator 클래스로 만든 별개의 계산기 cal1, cal2(이것을 객체라고 부른다)가 각각의 역할 수행
        - 계산기(cal1, cal2)의 결괏값 역시 다른 계산기의 결괏값과 상관없이 독립적인 값을 유지
        - 객체를 사용하면 계산기 대수가 늘어나더라도 객체만 생성하면 됨
        - 클래스만 사용하는 경우와 달리 매우 간단해짐
    
    - sub 메소드
        - 빼기 기능
            
            ```java
            class Calculator {
                int result = 0;
            
                int add(int num) {
                    result += num;
                    return result;
                }
            
                int sub(int num) {
                    result -= num;
                    return result;
                }
            }
            ```
            
    

## ****02. 클래스****

- ****객체에 대하여****
    - *Sample.java*
        
        ```java
        class Animal {
        }
        
        public class Sample {
            public static void main(String[] args) {
            }
        }
        ```
        
        - 보통 클래스는 특별한 경우가 아니라면 파일 단위로 하나씩 작성
    - 클래스에 존재하는 아주 중요한 기능
        - **객체(object)를 만드는 기능**
        
    - 객체 만들기
        
        ```java
        class Animal {
        }
        
        public class Sample {
            public static void main(String[] args) {
                Animal cat = new Animal();
            }
        }
        ```
        
        - `new`
            - 객체를 생성할 때 사용하는 키워드
    
    - **객체와 인스턴스**
        - 객체와 인스턴스의 차이
            - `Animal cat = new Animal()`
                - 이렇게 만들어진 cat → 객체
                - 그리고 cat이라는 객체는 Animal의 **인스턴스(instance)**
                - cat은 객체
                - cat은 Animal의 인스턴스
        - **인스턴스(instance)**
            - 특정 객체(cat)가 어떤 클래스(Animal)의 객체인지를 **관계**
            위주로 설명할 때 사용
    
    - 과자를 만드는 과자틀과 만들어진 과자들로 비유하면
        - 과자틀 → 클래스 (Class)
        - 과자틀에 의해서 만들어진 과자들 → 객체 (Object)
        
    - 많은 동물 객체(cat, dog, horse, ...)들을 Animal 클래스로 만들 수 있음
        
        ```java
        Animal cat = new Animal();
        Animal dog = new Animal();
        Animal horse = new Animal();
        ...
        ```
        

- ****객체 변수 (Instance variable)****
    - Animal 클래스에 의해 만들어진 동물에 이름 짓기
        
        ```java
        class Animal {
            String name;
        }
        
        public class Sample {
            public static void main(String[] args) {
                Animal cat = new Animal();
            }
        }
        ```
        
        - Animal 클래스에 name 이라는 String 변수 추가
            - 객체 변수
        - **객체 변수** → 인스턴스 변수, 멤버 변수, 속성이라고도 함
        - 객체와 객체 변수의 차이
            - 객체 : 클래스에 의해 생성되는 것
            - 객체 변수 : 그 클래스에 선언된 변수
        
    - 객체 변수는 변수이므로 값을 대입 가능
    - 객체 변수를 출력하려면?
        - 객체 변수에 어떻게 접근해야 하는지 알아야 함
        - 도트연산자(.)를 이용하여 접근 가능
            
            ```java
            객체.객체변수
            ```
            
        
        - `Animal cat = new Animal()` 에서 cat 이라는 객체 생성 시 cat 객체의 객체 변수 name에 접근 가능
            
            ```java
            cat.name   // 객체: cat, 객체변수: name
            ```
            
        
        - 객체 변수에 어떤 값이 대입되어 있는지 출력해보기
            
            ```java
            class Animal {
                String name;
            }
            
            public class Sample {
                public static void main(String[] args) {
                    Animal cat = new Animal();
                    System.out.println(cat.name);
                }
            }
            
            // 출력값
            null
            ```
            
            - null : 값이 할당되어 있지 않은 상태
            - 객체 변수로 name 을 선언했지만 아무런 값도 대입을 하지 않았기 때문에 null 이라는 값이 출력

- ****메소드****
    - **메소드(Method)**
        - 객체 변수에 값을 대입하는 가장 보편적인 방법
        - 클래스 내에 구현된 함수
        - Animal 클래스의 객체 변수인 name 에 값을 대입
            - setName 메소드를 추가
            
            ```java
            class Animal {
                String name;
            
                public void setName(String name) {
                    this.name = name;
                }
            }
            
            public class Sample {
                public static void main(String[] args) {
                    Animal cat = new Animal();
                    System.out.println(cat.name);
                }
            }
            ```
            
            - Animal 클래스에 추가된 setName 메소드의 형태
                - 입력 : String name
                - 출력: void (리턴값 없음)
            - 입력으로 name이라는 문자열 받고, 출력은 없는 형태의 메소드
        
        - setName 메소드의 내부
            
            ```java
            this.name = name;
            ```
            
            - 객체가 메소드를 호출하기 위해서는 `객체.메소드`로 호출
        
        - setName메소드를 호출
            
            ```java
            cat.setName("boby");
            ```
            
            - setName 메소드의 입력으로 "boby"와 같은 문자열 전달
                - setName메소드 → 입력항목으로 문자열을 필요로 함
        
        - setName메소드를 호출할 수 있도록 main메소드 수정
            
            ```java
            class Animal {
                String name;
            
                public void setName(String name) {
                    this.name = name;
                }
            }
            
            public class Sample {
                public static void main(String[] args) {
                    Animal cat = new Animal();
                    cat.setName("boby");  // 메소드 호출
                    System.out.println(cat.name);
                }
            }
            ```
            
            - `cat.name` 출력 전에 setName 메소드가 먼저 호출
            
        - main메소드에서 `cat.setName("boby")`
            - "boby"라는 입력값으로 setName 메소드를 호출
                - etName함수의 입력항목 name에 "boby"라는 문자열이 전달
        - setName 메소드의 `this.name = name;`문장 해석
            
            ```java
            this.name = "boby";
            ```
            
            - `this`
                - Animal 클래스에 의해서 생성된 객체
            - `Animal cat = new Animal()`  → cat이라는 객체 생성
            - `cat.setName("boby")` → cat객체에 의해 setName 메소드 호출
            - setName 메소드 내부에 선언된 this → cat 객체 지칭
        
        - `this.name = "boby";` 문장 해석
            
            ```java
            cat.name = "boby";
            ```
            
        
        - 객체 변수에 값을 대입하는 방법
            
            ```java
            객체.객체변수 = 값
            ```
            
            - `cat.name = "boby"`
                - 객체 cat의 객체변수 name에 "boby"라는 값을 대입
        
        - main 메소드를 다시 실행
            
            ```java
            main 메소드를 다시 실행
            ```
            
            - cat.name은 이제 null이 아니라 "boby"임을 확인

- ****객체 변수는 공유되지 않는다****
    - main메소드를 다음과 같이 변경
        
        ```java
        class Animal {
            String name;
        
            public void setName(String name) {
                this.name = name;
            }
        }
        
        public class Sample {
            public static void main(String[] args) {
                Animal cat = new Animal();
                cat.setName("boby");
        
                Animal dog = new Animal();
                dog.setName("happy");
            }
        }
        ```
        
        - cat객체에는 "boby"라는 이름을 대입
        - dog객체에는 "happy"라는 이름을 대입
    
    - setName 메소드에 의해 실행되는 문장
        
        ```java
        cat.name = "boby";
        dog.name = "happy";
        ```
        
        - `dog.name = "happy"`라는 문장이 나중에 수행
            - cat.name의 값도 "happy"라는 값으로 변경되지는 않을까?
    
    - 확인
        
        ```java
        class Animal {
            String name;
        
            public void setName(String name) {
                this.name = name;
            }
        }
        
        public class Sample {
            public static void main(String[] args) {
                Animal cat = new Animal();
                cat.setName("boby");  // 메소드 호출
        
                Animal dog = new Animal();
                dog.setName("happy");
        
                System.out.println(cat.name);
                System.out.println(dog.name);
            }
        }
        ```
        
        - 출력 결과
            
            ```java
            boby
            happy
            ```
            
    
    - 결과를 보면 **name 객체 변수는 공유되지 않는다**는 것을 확인할 수 있음
    
    - 클래스에서 가장 중요한 부분
        - **객체 변수의 값이 독립적으로 유지된다**
    - 객체 지향적(Object Oriented)이라는 말의 의미
        - 객체 변수의 값이 독립적으로 유지되기 때문에 가능한 것

## ****03. 메소드(Method)****

- **메소드**
    - 다른 프로그래밍 언어에는 **함수**라는 것이 별도로 존재
    - 자바의 함수는 따로 존재하지 않고 클래스 내에 존재
    - 이러한 클래스 내의 함수

- ****메소드를 사용하는 이유?****
    - 여러 번 반복해서 사용된다
        - 언제고 또다시 사용할 만한 가치가 있는 부분이다
    - 어떤 입력값을 주었을 때 어떤 리턴값을 돌려준다
        
        ```java
        int sum(int a, int b) {
            return a+b;
        }
        ```
        
        - *sum 메소드는 입력값으로 두개의 값(int 자료형 a, int 자료형 b)을 받으며 리턴값은 두 개의 입력값을 더한 값(int 자료형)이다.*
        
        - **return**
            - 메소드의 결과 값을 돌려주는 명령어
        
        ```java
        public class Sample {
            int sum(int a, int b) {
                return a + b;
            }
        
            public static void main(String[] args) {
                int a = 3;
                int b = 4;
        
                Sample sample = new Sample();
                int c = sample.sum(a, b);
        
                System.out.println(c);  // 7 출력
            }
        }
        ```
        
    
    - `Sample sample = new Sample()`
        - 자기 자신의 객체 생성
        - 성한 클래스를 단독으로 실행시켜 테스트할 때 자주 사용

- ****매개변수와 인수****
    - 매개변수(parameter)
        - 메소드에 입력으로 전달된 값을 받는 변수
    - 인수(arguments)
        - 메소드를 호출할 때 전달하는 입력값
    
    ```java
    public class Sample {
        int sum(int a, int b) {  // a, b 는 매개변수
            return a+b;
        }
    
        public static void main(String[] args) {
            Sample sample = new Sample();
            int c = sample.sum(3, 4);  // 3, 4는 인수
    
            System.out.println(c);  // 7 출력
        }
    }
    ```
    

- **같은 의미를 가진 여러 가지 용어들에 주의**
    - 입력값의 다른 말
        - 메소드의 인수, 매개변수 등
    - 결괏값의 다른 말
        - 출력값, 반환 값, 돌려주는 값 등
    - 많은 용어가 여러 가지 다른 말로 표현되지만 의미는 동일한 경우 多

- ****메소드의 입력값과 리턴값****
    - 메소드
        - 들어온 입력값을 가지고 어떤 처리를 해 적절한 리턴값을 돌려주는 블랙박스
        
        ```java
        입력값 ---> 메소드(블랙박스) ----> 리턴값
        ```
        
    
    - ****메소드의 구조****
        
        ```java
        리턴자료형 메소드명(입력자료형1 매개변수1, 입력자료형2 매개변수2, ...) {
            ...    
            return 리턴값;  // 리턴자료형이 void 인 경우에는 return 문이 필요없다.
        }
        ```
        
    
    - **return 자료형**
        - 메소드 수행 후 돌려줄 값의 자료형
        - return 이라는 명령을 사용
    
    - **입출력 유무에 따른 메소드의 분류**
        - 입력과 출력이 모두 있는 메소드
        - 입력과 출력이 모두 없는 메소드
        - 입력은 없고 출력은 있는 메소드
        - 입력은 있고 출력은 없는 메소드

- ****일반적인 메소드****
    - 입력 값이 있고 리턴값이 있는 메소드
        
        ```java
        int sum(int a, int b) {
            return a+b;
        }
        ```
        
        - sum 메소드의 입출력 자료형
            - 입력 값 - int 자료형 a, int 자료형 b
            - 리턴 값 - int 자료형
        - sum 메소드
            - 두 개의 입력값을 받아 서로 더한 결과값을 돌려주는 메소드
    
    - 입력값과 리턴값이 있는 메소드
        
        ```java
        리턴값받을변수 = 객체.메소드명(입력인수1, 입력인수2, ...)
        ```
        
    
    - sum 메소드의 사용 예
        
        ```java
        Sample sample = new Sample();
        int result = sample.sum(3, 4);
        ```
        
        - `sample.sum(3, 4)`호출 후 리턴값을 저장하는 result의 자료형은 int 로 해야 함
            - sum 메소드의 리턴타입이 int로 되어 있기 때문
        - sum 메소드의 리턴타입
            - `int sum(int a, int b) { ...`에서 보듯이 메소드명(sum) 바로 좌측에 표기

- ****입력값이 없는 메소드****
    - 입력값이 없는 메소드
        
        ```java
        String say() {
            return "Hi";
        }
        ```
        
        - say 메소드의 입출력 자료형
            - 입력 값 - 없음
            - 리턴 값 - String 자료형
    
    - 입력 인수부분을 나타내는 괄호 안이 비어있는 경우
        
        ```java
        public class Sample {
            String say() {
                return "Hi";
            }
        
            public static void main(String[] args) {
                Sample sample = new Sample();
                String a = sample.say();
                System.out.println(a);  // "Hi" 출력
            }
        }
        ```
        
        - say 메소드
            - `say()`처럼 괄호 안에 아무런 값도 넣지 않고 써야 함
            - 입력값은 없지만 리턴값으로 'Hi'라는 문자열을 돌려줌
            - `String a = sample.say()`
                - a에는 "Hi"라는 문자열이 대입될 것
    
    - 입력값이 없고 리턴값만 있는 메소드
        
        ```java
        리턴값받을변수 = 객체.메소드명()
        ```
        

- ****리턴값이 없는 메소드****
    - 리턴값이 없는 메소드
        
        ```java
        void sum(int a, int b) {
            System.out.println(a+"과 "+b+"의 합은 "+(a+b)+"입니다.");
        }
        ```
        
        - sum 메소드의 입출력 자료형
            - 입력 값 - int 자료형 a, int 자료형 b
            - 리턴 값 - void (없음)
    
    - 리턴값이 없는 메소드는 돌려주는 값 없음
        - 명시적으로 리턴타입 부분에 **void** 라고 표기
        
        ```java
        public class Sample {
            void sum(int a, int b) {
                System.out.println(a+"과 "+b+"의 합은 "+(a+b)+"입니다.");
            }
        
            public static void main(String[] args) {
                Sample sample = new Sample();
                sample.sum(3, 4);
            }
        }
        ```
        
    - 출력 문자열
        
        ```java
        3과 4의 합은 7입니다.
        ```
        
    
    - 리턴값이 없는 메소드
        
        ```java
        객체.메소드명(입력인수1, 입력인수2, ...)
        ```
        

- ****입력값도 리턴값도 없는 메소드****
    
    ```java
    void say() {
        System.out.println("Hi");
    }
    ```
    
    - say 메소드의 입출력 자료형
        - 입력 값 - 없음
        - 리턴 값 - void (없음)
    
    - 입력 값을 받는 곳도 없고 return문도 없으니 입력값도 리턴값도 없는 메소드
    
    - 해당 메소드 사용 방법
        
        ```java
        public class Sample {
            void say() {
                System.out.println("Hi");
            }
        
            public static void main(String[] args) {
                Sample sample = new Sample();
                sample.say();
            }
        }
        ```
        
    
    - 입력값도 리턴값도 없는 메소드
        
        ```java
        객체.메소드명()
        ```
        

- ****return의 또 다른 쓰임새****
    - 특별한 경우에 메소드를 빠져나가기를 원할 때
        - return을 단독으로 사용하여 메소드를 즉시 빠져나가기 가능
        
        ```java
        public class Sample {
            void sayNick(String nick) {
                if ("fool".equals(nick)) {
                    return;
                }
                System.out.println("나의 별명은 "+nick+" 입니다.");
            }
        
            public static void main(String[] args) {
                Sample sample = new Sample();
                sample.sayNick("angel");
                sample.sayNick("fool");  // 출력되지 않는다.
            }
        }
        ```
        
        - sayNick 메소드
            - 입력으로 받은 문자열 값을 받아서 출력하는 메소드
            - 리턴값은 없음
        
        - 문자열을 출력한다는 것 ≠ 리턴값이 있다는 것
        - 메소드의 리턴값
            - 오로지 return문에 의해서만 생성
        
        - 메소드 수행 시 특정 조건에 따라 메소드를 즉시 빠져나가고 싶은 경우 return 문 이용
        - return 문만을 써서 메소드를 빠져나가는 방법은 리턴자료형이 void인 메소드에만 해당
            - 리턴자료형이 명시되어 있는 메소드에서 return 문만 작성하면 컴파일 오류 발생

- ****메소드 내에서 선언된 변수의 효력 범위****
    - 메소드안에서 사용하는 변수의 이름을 메소드 밖에서 사용한 이름과 동일하게 사용한다면?
        
        ```java
        public class Sample {
            void varTest(int a) {
                a++;
            }
        
            public static void main(String[] args) {
                int a = 1;
                Sample sample = new Sample();
                sample.varTest(a);
                System.out.println(a);
            }
        }
        ```
        
        - varTest 메소드
            - 입력으로 들어온 int 자료형의 값을 1만큼 증가시키는 역할
    
    - main 메소드 분석
        - 먼저 main메소드에서 a라는 int 자료형의 변수를 생성하고 1을 대입
        - varTest 메소드를 입력 값 a를 주어 호출
        - 그 다음에 a의 값을 출력
        - 당연히 varTest 메소드에서 a의 값을 1만큼 증가시켰으니 2가 출력되어야 할 것 같으나 1이라는 결과 값이 나옴
            - 메소드 내에서 사용되는 변수 = 메소드 안에서만 쓰여지는 변수
        - `public void varTest(int a) {`에서 입력 인수를 뜻하는 변수 a
            - 메소드 안에서만 쓰이는 변수
            - 메소드 밖의 변수 a가 아니다
    
    - 변수이름을 a로 사용한 varTest메소드
        - 변수이름을 b로 사용한 varTest와 기능적으로 완전히 동일
        
        ```java
        public void varTest(int b) {
            b++;
        }
        ```
        
        - 메소드에서 쓰이는 변수
            - 메소드 밖의 변수 이름들과는 전혀 상관 없음
        - **로컬 변수** (local variable) : 메소드 내에서만 쓰이는 변수
    
    - varTest라는 메소드를 이용해 메소드 외부의 a를 1만큼 증가시키는 방법
        
        ```java
        public class Sample {
            int varTest(int a) {
                a++;
                return a;
            }
        
            public static void main(String[] args) {
                int a = 1;
                Sample sample = new Sample();
                a = sample.varTest(a);
                System.out.println(a);
            }
        }
        ```
        
        - 해법은 위 예처럼 varTest메소드에 return문을 이용하는 방법
        - varTest 메소드 → 입력으로 들어온 값을 1만큼 증가시켜 리턴
            - `a = sample.varTest(a)`
                - a의 값은 다시 varTest 메소드의 리턴값으로 대입
                - 1만큼 증가된 값으로 a의 값이 변경
    
    - 객체를 넘기는 방법 (위 예제와 비교)
        
        ```java
        public class Sample {
        
            int a;  // 객체변수 a
        
            void varTest(Sample sample) {
                sample.a++;
            }
        
            public static void main(String[] args) {
                Sample sample = new Sample();
                sample.a = 1;
                sample.varTest(sample);
                System.out.println(sample.a);
            }
        }
        ```
        
        - a 라는 int 자료형 변수 → Sample 클래스의 객체변수로 선언
        - varTest 메소드
            - Sample 클래스의 객체를 입력받아 해당 객체의 객체변수 a의 값을 1만큼 증가시키는 역할하도록 수정
        - main메소드
            - varTest메소드에 1이라는 값을 전달하던 것을 Sample 클래스의 객체인 sample을 넘기도록 수정
        
        - 수정 후 프로그램 실행 시
            - sample객체의 객체변수 a의 값이 원래는 1이었으나
            - varTest 메소드 실행 후 1만큼 증가되어 2가 출력되는 것을 확인
        - varTest 메소드의 입력 파라미터가 값이 아님
            - Sample 클래스의 객체라는 사실에 주목할 것
        - 메소드가 객체를 전달 받으면?
            - 메소드 내의 객체는 전달받은 객체 그 자체로 수행
            - 입력으로 전달받은 sample 객체의 객체변수 a의 값 증가
        
        - 메소드의 입력항목이 값인지 객체인지를 구별하는 기준
            - 입력항목의 자료형이 primitive 자료형인지 아닌지?
            - int 자료형과 같은 primitive 자료형인 경우 → 값이 전달
            - 그 이외의 경우(reference 자료형) → 객체가 전달
        
        - **this 활용하기**
            - sample 객체를 이용하여 varTest라는 메소드를 호출할 경우
                - 굳이 sample 객체를 전달할 필요 없음
                - 전달하지 않더라도 varTest 메소드는 this라는 키워드를 이용해 객체에 접근 가능
            - this를 이용하여 varTest메소드를 수정한 버전
                
                ```java
                public class Sample {
                
                    int a;  // 객체변수 a
                
                    void varTest() {
                        this.a++;
                    }
                
                    public static void main(String[] args) {
                        Sample sample = new Sample();
                        sample.a = 1;
                        sample.varTest();
                        System.out.println(sample.a);  // 2 출력
                    }
                }
                ```
                

## ****04. Call by value****

- 메소드에 객체를 전달할 경우
    - 메소드에서 객체의 객체변수(속성) 값을 변경 가능
    
    ```java
    class Updater {
        void update(int count) {
            count++;
        }
    }
    
    class Counter {
        int count = 0;  // 객체변수
    }
    
    public class Sample {
        public static void main(String[] args) {
            Counter myCounter = new Counter();
            System.out.println("before update:"+myCounter.count);
            Updater myUpdater = new Updater();
            myUpdater.update(myCounter.count);
            System.out.println("after update:"+myCounter.count);
        }
    }
    ```
    

- **한 개의 자바파일에 2개 이상의 클래스 선언하기**
    - Sample.java라는 파일 내
        - Sample, Updater, Counter라는 클래스 3개
        - 하나의 java파일 내에는 여러 개의 클래스 선언 가능
            - 단, 파일명이 Sample.java라면 Sample.java 내의 Sample 클래스는 public 으로 선언하라는 관례(규칙) 존재
        - Updater 클래스
            - 전달받은 숫자를 1만큼 증가시키는 update라는 메소드 보유
        - Counter 클래스
            - count라는 객체변수 보유
        - Sample클래스의 main메소드
            - Counter클래스에 의해 생성된 객체의 객체변수 count의 값을 Updater클래스를 이용하여 증가시키려고 시도
    
    - 위 예제 결과 값
        
        ```java
        before update:0
        after update:0
        ```
        
        - 객체 변수 count의 값을 update메소드에 넘겨서 변경
            - 그러나 값에 변화 없음
            - update 메소드 → 값(int 자료형)을 전달받았기 때문
    
    - 예제 변경
        
        ```java
        class Updater {
            void update(Counter counter) {
                counter.count++;
            }
        }
        
        class Counter {
            int count = 0;  // 객체변수
        }
        
        public class Sample {
            public static void main(String[] args) {
                Counter myCounter = new Counter();
                System.out.println("before update:"+myCounter.count);
                Updater myUpdater = new Updater();
                myUpdater.update(myCounter);
                System.out.println("after update:"+myCounter.count);
            }
        }
        ```
        
        - 이전 예제와의 차이점
            - update 메소드의 입력항목
                - 기존 :  `int count` → 값 전달받음
                - 현재 : `Counter counter` → 객체 전달받음
        
        - update 메소드를 호출하는 부분도 수정됨
            
            ```java
            update 메소드를 호출하는 부분
            ```
            
        
        - 변경된 클래스 실행 시 결과 값
            
            ```java
            before update:0
            after update:1
            ```
            
            - myCounter 객체의 count 값이 1만큼 증가

- 메소드의 입력으로 객체를 전달받는 경우
    - 메소드가 입력받은 객체를 그대로 사용
        - 메소드가 객체의 속성값을 변경하면 메소드 수행 후에도 객체의 변경된 속성값 유지

## ****05. 상속자****

## ****06. 생성자****

## ****07. 인터페이스****

## ****08. 다형성****

## ****09. 추상클래스****