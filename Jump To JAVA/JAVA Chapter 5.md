# JAVA Chapter 5

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

## ****05. 상속****

- ****상속****
    - Animal 클래스를 상속하는 Dog 클래스 만들기
        
        ```java
        class Animal {
            String name;
        
            void setName(String name) {
                this.name = name;
            }
        }
        
        class Dog extends Animal {
        }
        
        public class Sample {
            public static void main(String[] args) {
                Dog dog = new Dog();
                dog.setName("poppy");
                System.out.println(dog.name);  // poppy 출력
            }
        }
        ```
        
    
    - **extends** : **클래스 상속**을 위해서 사용
    - Dog 클래스는 Animal 클래스를 상속
        - Dog 클래스에 name 이라는 객체변수와 setName 이라는 메소드를 만들지 않았음
        - But 그대로 사용 가능

- ****부모 클래스의 기능을 확장****
    - Dog 클래스에 sleep 메소드 추가
        
        ```java
        class Animal {
            String name;
        
            void setName(String name) {
                this.name = name;
            }
        }
        
        class Dog extends Animal {
            void sleep() {
                System.out.println(this.name+" zzz");
            }
        }
        
        public class Sample {
            public static void main(String[] args) {
                Dog dog = new Dog();
                dog.setName("poppy");
                System.out.println(dog.name);  // poppy 출력
                dog.sleep();  // poppy zzz 출력
            }
        }
        ```
        
        - Dog 클래스 → Animal 클래스보다 좀 더 많은 기능(sleep메소드가 추가되었다.) 가짐
    
    - 부모 클래스를 상속받은 자식 클래스
        - 부모 클래스의 기능에 더해 좀 더 많은 기능을 갖도록 작성

- ****IS-A 관계****
    - Dog 클래스는 Animal 클래스를 상속
        - Dog는 Animal의 하위 개념
    - `IS-A`관계
        - "Dog `is a`Animal" 과 같이 말할 수 있는 관계
        - IS-A 관계(상속관계)에 있을 때 자식 클래스의 객체
            - 부모 클래스의 자료형인 것처럼 사용 가능
        
        ```java
        Animal dog = new Dog();  // Dog is a Animal
        ```
        
    - 주의할 점
        - Dog객체를 Animal 자료형으로 사용할 경우
            - Dog 클래스에만 존재하는 sleep 메소드를 사용할 수 없음
            - Animal 클래스에 구현된 setName 메소드만 사용 가능
        - 이 반대의 경우 즉 부모 클래스로 만들어진 객체를 자식 클래스의 자료형으로는 사용 X
            - 다음 코드는 컴파일 오류 발생
            
            ```java
            // 컴파일 오류: 부모 클래스로 만든 객체는 자식 클래스의 자료형으로 사용할 수 없다.
            Dog dog = new Animal();  
            ```
            
        
        - 개념적으로 살펴 보면
            
            ```java
            Animal dog = new Dog();  // Dog is a Animal (O)
            
            Dog dog = new Animal();  // Animal is a Dog (X)
            ```
            
            - 첫 번째 코드 : "개로 만든 객체는 동물 자료형이다.”
            - 두 번째 코드 : "동물로 만든 객체는 개 자료형이다.”
                - 동물로 만든 객체
                    - "개" 자료형 외에 "호랑이" 자료형이나 "사자" 자료형도 가능
                - 개념적으로 봐도 두 번째는 성립 불가
            
    - **Object 클래스**
        - 자바에서 만드는 모든 클래스
            - Object 클래스를 상속받음
        - Object 클래스를 상속하도록 코딩하지 않아도 자바에서 만들어지는 모든 클래스는 자동으로 상속받게끔 되어 있음
            
            ```java
            class Animal extends Object {
                String name;
            
                void setName(String name) {
                    this.name = name;
                }
            }
            ```
            
        - 따라서 자바에서 만드는 모든 객체 → Object 자료형으로 사용 가능
            
            ```java
            Object animal = new Animal();  // Animal is a Object
            Object dog = new Dog();  // Dog is a Object
            ```
            
    

- ****메소드 오버라이딩 (Method overriding)****
    - **메소드 오버라이딩(Method Overriding)**
        - 부모클래스의 메소드를 자식클래스가 동일한 형태로 또다시 구현하는 행위
    
    - Dog 클래스를 좀 더 구체화 시키는 HouseDog 클래스 생성
        
        ```java
        class Animal {
            String name;
        
            void setName(String name) {
                this.name = name;
            }
        }
        
        class Dog extends Animal {
            void sleep() {
                System.out.println(this.name+" zzz");
            }
        }
        
        class HouseDog extends Dog {
        }
        
        public class Sample {
            public static void main(String[] args) {
                HouseDog houseDog = new HouseDog();
                houseDog.setName("happy");
                houseDog.sleep();  // happy zzz 출력
            }
        }
        ```
        
        - HouseDog 클래스를 실행해 보면 sleep 메소드 호출돼 아래의 결과 출력
            
            ```java
            happy zzz
            ```
            
        
        - HouseDog 클래스로 만들어진 객체들
            - sleep 메소드 호출 시 "happy zzz" 가 아닌 "happy zzz in house" 를 출력해야 할 때
            
            ```java
            class Animal {
                String name;
            
                void setName(String name) {
                    this.name = name;
                }
            }
            
            class Dog extends Animal {
                void sleep() {
                    System.out.println(this.name + " zzz");
                }
            }
            
            class HouseDog extends Dog {
                void sleep() {
                    System.out.println(this.name + " zzz in house");
                }
            }
            
            public class Sample {
                public static void main(String[] args) {
                    HouseDog houseDog = new HouseDog();
                    houseDog.setName("happy");
                    houseDog.sleep();  // happy zzz in house 출력
                }
            }
            ```
            
            - 해당 결과 값
                
                ```java
                happy zzz in house
                ```
                
        
        - HouseDog 클래스에 Dog 클래스와 동일한 형태(입출력이 동일)의 sleep 메소드를 구현
            - HouseDog 클래스의 sleep 메소드가 Dog 클래스의 sleep 메소드보다 더 높은 우선순위
                - HouseDog 클래스의 sleep 메소드가 호출

- ****메소드 오버로딩 (method overloading)****
    - **메소드 오버로딩(method overloading)**
        - 입력항목이 다른 경우 동일한 이름의 메소드를 만드는 것
    
    - HouseDog 클래스에 메소드 추가("변경"이 아니라 "추가"임에 주의)
        
        ```java
        void sleep(int hour) {
            System.out.println(this.name+" zzz in house for " + hour + " hours");
        }
        ```
        
        - 이미 sleep이라는 메소드가 있으나 동일한 이름의 sleep메소드 또 생성 가능
            - 단, 메소드의 입력항목이 다를 경우만 가능
            - 새로 만든 sleep메소드는 → 입력항목으로 hour라는 int 자료형 추가
    
    - 새로 만든 sleep메소드를 테스트 하기 위해 main메소드 변경 및 실행
        
        ```java
        class Animal {
            String name;
        
            void setName(String name) {
                this.name = name;
            }
        }
        
        class Dog extends Animal {
            void sleep() {
                System.out.println(this.name + " zzz");
            }
        }
        
        class HouseDog extends Dog {
            void sleep() {
                System.out.println(this.name + " zzz in house");
            }
        
            void sleep(int hour) {
                System.out.println(this.name + " zzz in house for " + hour + " hours");
            }
        }
        
        public class Sample {
            public static void main(String[] args) {
                HouseDog houseDog = new HouseDog();
                houseDog.setName("happy");
                houseDog.sleep();  // happy zzz in house 출력
                houseDog.sleep(3);  // happy zzz in house for 3 hours 출력
            }
        }
        ```
        
        - 출력 결과
            
            ```java
            happy zzz in house
            happy zzz in house for 3 hours
            ```
            

- ****다중 상속****
    - **다중 상속**
        - 클래스가 동시에 하나 이상의 클래스를 상속받는 것
        - C++, 파이썬 등 많은 언어들이 다중 상속을 지원
        - **But 자바는 다중 상속 지원하지 않음**
        
        - 만약 다중 상속 지원한다면?
            
            ```java
            class A {
                public void msg() {
                    System.out.println("A message");
                }
            }
            
            class B {
                public void msg() {
                    System.out.println("B message");
                }
            }
            
            class C extends A, B {
                public void static main(String[] args) {
                    C test = new C();
                    test.msg();
                }
            }
            ```
            
            - 자바가 다중 상속을 지원한다고 가정 후 A, B 라는 클래스를 동시에 상속(extends A, B)하도록 함
                - `test.msg();`실행 시
                    - A 클래스의 msg 메소드를 실행해야 할까?
                    - 아니면 B 클래스의 msg 메소드를 실행해야 할까?
            
            - 다중 상속 지원 시 애매모호한 부분 발생
                - 자바는 이러한 불명확한 부분을 애초에 잘라 낸 언어
            - 다중 상속을 지원하는 다른 언어들
                - 동일한 메소드를 상속받는 경우 우선 순위등을 적용해 해결

## ****06. 생성자****

- ****생성자(Constructor)****
    - **생성자(Constructor)**
        - 메소드명이 클래스명과 동일하고 리턴 자료형을 정의하지 않는 메소드
    - 생성자의 규칙
        1. 클래스명과 메소드명이 동일하다.
        2. 리턴타입을 정의하지 않는다. (void도 사용하지 않는다.)
    - 생성자는 객체가 생성될 때 호출
    - 메소드와 마찬가지로 다양한 입력을 받을 수 있음
    - 생성자 사용 시 필수적인 행동을 객체 생성 시에 제어 가능
    
    - HouseDog 클래스에 생성자 추가
        
        ```java
        (... 생략 ...)
        
        class HouseDog extends Dog {
            HouseDog(String name) {
                this.setName(name);
            }
        
            void sleep() {
                System.out.println(this.name + " zzz in house");
            }
        
            void sleep(int hour) {
                System.out.println(this.name + " zzz in house for " + hour + " hours");
            }
        }
        
        (... 생략 ...)
        ```
        
        - 생성자 → new 키워드가 사용될 때 호출
            
            ```java
            new 클래스명(입력인수, ...)
            ```
            
        
        - HouseDog 클래스에 만든 생성자
            - 입력값으로 문자열을 필요로 하는 생성자
            
            ```java
            HouseDog(String name) {
                this.setName(name);
            }
            ```
            
            - new 키워드로 객체를 만들 때 문자열을 전달해야만 함
                
                ```java
                // 생성자 호출 시 문자열을 전달해야 한다.
                HouseDog dog = new HouseDog("happy");   
                ```
                
            
            - 다음의 경우 컴파일 오류 발생
                
                ```java
                HouseDog dog = new HouseDog();
                ```
                
            - 오류가 발생하는 이유
                - 객체 생성 방법이 생성자의 규칙과 맞지 않기 때문
                - 생성자가 선언된 경우 생성자의 규칙대로만 객체를 생성 가능
        
        - HouseDog 클래스에 생성자를 선언
            - `new HouseDog()` 사용하는 main 메소드에서 컴파일 오류 발생
            - main 메소드 수정
                
                ```java
                (... 생략 ...)
                
                public class Sample {
                    public static void main(String[] args) {
                        HouseDog dog = new HouseDog("happy");
                        System.out.println(dog.name);
                    }
                }
                ```
                
            
            - main 메소드 실행 시 생성자에 의해 name 객체변수에 값이 설정
                - 출력 결과
                    
                    ```java
                    happy
                    ```
                    

- ****디폴트(default) 생성자****
    - ****디폴트(default) 생성자****
        - 생성자의 입력 항목이 없고 생성자 내부에 아무 내용이 없는 생성자
        
    - 코드 비교
        
        ```java
        class Dog extends Animal {
            void sleep() {
                System.out.println(this.name + " zzz");
            }
        }
        ```
        
        - 다른 코드
        
        ```java
        class Dog extends Animal {
            Dog() {
            }
        
            void sleep() {
                System.out.println(this.name + " zzz");
            }
        }
        ```
        
        - 디폴트 생성자를 구현
            - `new Dog()`
                - Dog 클래스의 객체가 만들어 질 때 위에 구현한 디폴트 생성자가 실행
        
    - 클래스에 생성자가 하나도 없다면?
        - 컴파일러는 자동으로 디폴트 생성자 추가
    - 사용자가 작성한 생성자가 하나라도 구현되어 있다면?
        - 컴파일러는 디폴트 생성자 추가 X

- ****생성자 오버로딩****
    - **생성자 오버로딩(Overloading)**
        - 입력 항목이 다른 생성자를 여러 개 만드는 것 (메소드 오버로딩과 동일한 개념)
        - 하나의 클래스에 여러 개의 입력항목이 다른 생성자 만들기 가능
            
            ```java
            class Animal {
                String name;
            
                void setName(String name) {
                    this.name = name;
                }
            }
            
            class Dog extends Animal {
                void sleep() {
                    System.out.println(this.name + " zzz");
                }
            }
            
            class HouseDog extends Dog {
                HouseDog(String name) {
                    this.setName(name);
                }
            
                HouseDog(int type) {
                    if (type == 1) {
                        this.setName("yorkshire");
                    } else if (type == 2) {
                        this.setName("bulldog");
                    }
                }
            
                void sleep() {
                    System.out.println(this.name + " zzz in house");
                }
            
                void sleep(int hour) {
                    System.out.println(this.name + " zzz in house for " + hour + " hours");
                }
            }
            
            public class Sample {
                public static void main(String[] args) {
                    HouseDog happy = new HouseDog("happy");
                    HouseDog yorkshire = new HouseDog(1);
                    System.out.println(happy.name);  // happy 출력
                    System.out.println(yorkshire.name);  // yorkshire 출력
                }
            ```
            
            - HouseDog 클래스는 두 개의 생성자
                - String 자료형을 입력으로 받는 생성자
                - int 자료형을 입력으로 받는 생성자
                - 두 생성자의 차이 → 입력항목
                
            - HouseDog 클래스의 객체는 두 가지 방법으로 생성 가능
                
                ```java
                HouseDog happy = new HouseDog("happy");  // 문자열로 생성
                HouseDog yorkshire = new HouseDog(1);  // 숫자값으로 생성
                ```
                
        

## ****07. 인터페이스****

- ****인터페이스는 왜 필요한가?****
    - 어떤 동물원 사육사가 하는 일
        
        난 동물원의 사육사이다.
        
        육식동물이 들어오면 난 먹이를 던져준다.
        
        호랑이가 오면 사과를 던져준다.
        
        사자가 오면 바나나를 던져준다.
        
        - Animal, Tiger, Lion, Zookeeper 클래스 작성
            - *Sample.java*
            
            ```java
            class Animal {
                String name;
            
                void setName(String name) {
                    this.name = name;
                }
            }
            
            class Tiger extends Animal {
            }
            
            class Lion extends Animal {
            }
            
            class ZooKeeper {
                void feed(Tiger tiger) {  // 호랑이가 오면 사과를 던져준다.
                    System.out.println("feed apple");
                }
            
                void feed(Lion lion) {  // 사자가 오면 바나나를 던져준다.
                    System.out.println("feed banana");
                }
            }
            
            public class Sample {
                public static void main(String[] args) {
                    ZooKeeper zooKeeper = new ZooKeeper();
                    Tiger tiger = new Tiger();
                    Lion lion = new Lion();
                    zooKeeper.feed(tiger);  // feed apple 출력
                    zooKeeper.feed(lion);  // feed banana 출력
                }
            }
            ```
            
            - Dog 클래스와 마찬가지로 Animal을 상속한 Tiger와 Lion 등장
            - ZooKeeper 클래스
                - 사육사 클래스
                - 호랑이가 왔을 때, 사자가 왔을 때 각각 다른 feed 메소드 호출
            
        - 출력 결과
            
            ```java
            feed apple
            feed banana
            ```
            
        
    - 육식동물이 추가 될 때마다 feed 메소드를 추가해야 한다면?
        - 매우 귀찮을 것
        - 이런 어려움을 극복하기 위해 인터페이스의 도움 필요

- ****인터페이스 작성하기****
    - 인터페이스
        - class가 아닌 **interface** 라는 키워드 이용해 작성
    - 코드 상단에 육식동물(Predator) 인터페이스 추가
        
        ```java
        interface Predator {
        }
        
        class Animal {
            String name;
        
            void setName(String name) {
                this.name = name;
            }
        }
        
        (... 생략 ...)
        ```
        
    
    - 인터페이스 구현
        - **implements** 라는 키워드 사용
    - Tiger, Lion 클래스는 작성한 인터페이스를 구현하도록(Implements) 수정
        
        ```java
        (... 생략 ...)
        
        class Tiger extends Animal implements Predator {
        }
        
        class Lion extends Animal implements Predator {    
        }
        
        (... 생략 ...)
        ```
        
    - Tiger, Lion 클래스가 Predator 인터페이스를 구현
        - ZooKeeper 클래스의 feed 메소드 변경
        - 변경 전
        
        ```java
        (... 생략 ...)
        
        class ZooKeeper {
            void feed(Tiger tiger) {
                System.out.println("feed apple");
            }
        
            void feed(Lion lion) {
                System.out.println("feed banana");
            }
        }
        
        (... 생략 ...)
        ```
        
        - 변경 후
            
            ```java
            (... 생략 ...)
            
            class ZooKeeper {
                void feed(Predator predator) {
                    System.out.println("feed apple");
                }
            }
            
            (... 생략 ...)
            ```
            
            - feed 메소드의 입력으로 Tiger, Lion을 각각 필요로 했음
                - But, Predator라는 인터페이스로 대체
            - tiger, lion
                - 각각 Tiger, Lion의 객체이기도 하지만 Predator 인터페이스의 객체
                    - Predator를 자료형의 타입으로 사용
        
        - 상속에서 본 IS-A 관계 → 인터페이스에서도 적용
            - tiger - Tiger 클래스의 객체, Predator 인터페이스의 객체
            - lion - Lion 클래스의 객체, Predator 인터페이스의 객체
    
    - **다형성(폴리모피즘)**
        - 객체가 한 개 이상의 자료형 타입을 갖게 되는 특성
        
    - 어떤 육식동물이 추가되더라도 ZooKeeper는 feed 메소드를 추가할 필요 X
    - But 육식동물이 추가 될 때마다 Predator 인터페이스를 구현한 클래스 작성
        
        ```java
        class Crocodile extends Animal implements Predator {
        }
        ```
        
    - 중요 클래스를 작성 시
        - 클래스의 구현체와 상관없이 인터페이스를 기준으로 중요 클래스를 작성해야 함
            - 구현체(Tiger, Lion, Crocodile,...)는 늘어날 수 있으나, 인터페이스(Predator)는 하나

- ****인터페이스의 메소드****
    - 위 클래스에서 문제 발생
        - 아래의 ZooKeeper클래스의 feed 메소드를 보면 호랑이가 오던지, 사자가 오던지 무조건 "feed apple" 이라는 문자열 출력
            
            ```java
            (... 생략 ...)
            
            class ZooKeeper {
                public void feed(Predator predator) {
                    System.out.println("feed apple");  // 항상 feed apple 만을 출력한다.
                }
            }
            
            (... 생략 ...)
            ```
            
        - Predator 인터페이스에 다음과 같은 메소드를 추가
            
            ```java
            interface Predator {
                String getFood();
            }
            
            (... 생략 ...)
            ```
            
            - getFood 라는 메소드 추가
                - 그런데 메소드에 몸통이 없다?
        
    - 인터페이스의 메소드
        - 메소드의 이름과 입출력에 대한 정의만 있고 그 내용은 無
            - 인터페이스는 규칙이기 때문
        - getFood라는 메소드
            - 인터페이스를 implements한 클래스들이 구현해야만 하는 것
    
    - 인터페이스에 위처럼 메소드를 추가
        - Tiger, Lion 등의 Predator 인터페이스를 구현한 클래스들에서 컴파일 오류 발생
    - 오류를 해결하려면 Tiger, Lion 클래스에 getFood 메소드 구현
        
        ```java
        (... 생략 ...)
        
        class Tiger extends Animal implements Predator {
            public String getFood() {
                return "apple";
            }
        }
        
        class Lion extends Animal implements Predator {
            public String getFood() {
                return "banana";
            }
        }
        
        (... 생략 ...)
        ```
        
        - Tiger, Lion 클래스의 getFood 메소드
            - 육식동물의 먹이인 "apple", "banana"를 각각 리턴하도록 작성
    
    - 인터페이스의 메소드
        - 항상 public으로 구현
    
    - ZooKeeper 클래스 변경 가능
        
        ```java
        (... 생략 ...)
        
        class ZooKeeper {
            void feed(Predator predator) {
                System.out.println("feed "+predator.getFood());
            }
        }
        
        (... 생략 ...)
        ```
        
        - feed 메소드가 "feed apple" 을 출력하던 것
            - `"feed "+predator.getFood()`를 출력하도록 변경
        
        - 출력 결과
            
            ```java
            feed apple
            feed banana
            ```
            

- ****인터페이스의 핵심과 개념****
    - **왜 인터페이스가 필요한 지에 대해서 이해**하는 것 ⇒ 가장 중요
    - ZooKeeper 클래스
        - 육식 동물들의 종류만큼의 feed 메소드가 필요했음
        - Predator 인터페이스 이용하여 구현
            - 단 한 개의 feed 메소드로 구현 가능해짐
    - 여기서 중요한 점
        - 메소드의 갯수가 줄어들었다는 점 X
        - ZooKeeper 클래스
            - 동물들의 종류에 의존적인 클래스 → 동물들의 종류와 상관없는 독립적인 클래스가 됨
    
    - 인터페이스 → USB 포트 같은 존재
        
        
        | 물리적 세계 | 자바 세계 |
        | --- | --- |
        | 컴퓨터 | ZooKeeper |
        | USB 포트 | Predator |
        | 하드디스크, 디지털카메라,... | Tiger, Lion, Crocodile,... |
    - 상속과 인터페이스
        - **상속**
            - 자식 클래스가 부모 클래스의 메소드를 오버라이딩 하지 않고 사용
                - 해당 메소드를 반드시 구현해야 한다는 **"강제성” 갖지 못함**
        - **인터페이스**
            - 인터페이스의 메소드를 반드시 구현해야 하는 **"강제성"을 갖는다**

- ****디폴트 메소드****
    - 인터페이스의 메소드
        - 몸통(구현체)을 가질 수 없음
    - 디폴트 메소드를 사용
        - 실제 구현된 형태의 메서드 가질 수 있음
    
    - Predator 인터페이스에 디폴트 메소드 추가
        
        ```java
        interface Predator {
            String getFood();
        
            default void printFood() {
                System.out.printf("my food is %s\n", getFood());
            }
        }
        ```
        
    
    - **디폴트 메소드**
        - 메소드명 가장 앞에 "default" 라고 표기해야 함
        - 디폴트 메스드는 오버라이딩 가능
            - printFood 메서드 → 실제 클래스에서 다르게 구현하여 사용 가능

- ****스태틱 메소드****
    - 인터페이스에 스태틱 메소드 구현
        - `인터페이스명.스태틱메소드명`
            - 일반 클래스의 스태틱 메소드를 사용하는 것과 동일하게 사용 가능
    
    - Predator 인터페이스에 스태틱 메소드를 추가
        
        ```java
        interface Predator {
            String getFood();
        
            default void printFood() {
                System.out.printf("my food is %s\n", getFood());
            }
        
            int LEG_COUNT = 4;  // 인터페이스 상수
        
            static int speed() {
                return LEG_COUNT * 30;
            }
        }
        ```
        
        - 다음과 같이 사용 가능
            
            ```java
            Predator.speed();
            ```
            
    - **인터페이스 상수**
        - 위 코드에서 사용한 `int LEG_COUNT = 4;`문장
            - 인터페이스에 정의한 상수
        - 인터페이스에 정의한 상수
            - `int LEG_COUNT=4;`
            - `public static final`을 생략해도 자동으로 적용

## ****08. 다형성****

- **다형성** (폴리모피즘, Polymorphism)
    - Sample.java 파일에 Bouncer(경비원) 클래스 추가
        
        ```java
        interface Predator {
            (... 생략 ...)
        }
        
        class Animal {
            (... 생략 ...)
        }
        
        class Tiger extends Animal implements Predator {
            (... 생략 ...)
        }
        
        class Lion extends Animal implements Predator {
           (... 생략 ...)
        }
        
        class ZooKeeper {
            (... 생략 ...)
        }
        
        class Bouncer {
            void barkAnimal(Animal animal) {
                if (animal instanceof Tiger) {
                    System.out.println("어흥");
                } else if (animal instanceof Lion) {
                    System.out.println("으르렁");
                }
            }
        }
        
        public class Sample {
            public static void main(String[] args) {
                Tiger tiger = new Tiger();
                Lion lion = new Lion();
        
                Bouncer bouncer= new Bouncer();
                bouncer.barkAnimal(tiger);
                bouncer.barkAnimal(lion);
            }
        }
        ```
        
        - 경비원 클래스는 동물을 짖게(barkAnimal) 하여 건물 지킴
        - barkAnimal 메소드
            - 입력으로 받은 animal 객체가
                - Tiger의 객체인 경우 → "어흥" 출력
                - Lion의 객체인 경우 → "으르렁" 출력
        
        - `instanceof`
            - 어떤 객체가 특정 클래스의 객체인지 조사할 때 사용되는 자바의 내장 명령어
            - `animal instanceof Tiger`
                - "animal 객체는 Tiger 클래스로 만들어진 객체인가?” 묻는 조건문
        
    - **IS-A 관계**
        - barkAnimal 메소드의 입력자료형
            - Tiger나 Lion이 아닌 Animal
            - But barkAnimal 메소드 호출 시 tiger또는 lion객체를 전달 가능
                - Tiger, Lion 클래스
                    - Animal이라는 부모 클래스를 상속한 자식 클래스
            
            - 자식 클래스에 의해서 만들어진 객체
                - 언제나 부모 클래스의 자료형으로 사용 가능
                
                ```java
                Animal tiger = new Tiger();  // Tiger is a Animal
                Animal lion = new Lion();  // Lion is a Animal
                ```
                
                - 출력 결과
                    
                    ```java
                    어흥
                    으르렁
                    ```
                    
    
    - Crocodile, Leopard 등의 클래스 추가 시 → barkAnimal 메소드 수정
        
        ```java
        class Bouncer {
            void barkAnimal(Animal animal) {
              if (animal instanceof Tiger) {
                    System.out.println("어흥");
                } else if (animal instanceof Lion) {
                    System.out.println("으르렁");
                } else if (animal instanceof Crocodile) {
                  System.out.println("쩝쩝");
                } else if (animal instanceof Leopard) {
                  System.out.println("캬옹");
                }
            }
        }
        ```
        
        - 동물 클래스가 추가될 때마다 분기문이 추가되어야 함 → 좋은 방법 X
    
    - Barkable 인터페이스 작성, Tiger클래스와 Lion 클래스가 Barkable 인터페이스를 구현하도록 변경
        
        ```java
        interface Predator {
            (... 생략 ...)
        }
        
        interface Barkable {
            void bark();
        }
        
        class Animal {
            (... 생략 ...)
        }
        
        class Tiger extends Animal implements Predator, Barkable {
            public String getFood() {
                return "apple";
            }
        
            public void bark() {
                System.out.println("어흥");
            }
        }
        
        class Lion extends Animal implements Predator, Barkable {
            public String getFood() {
                return "banana";
            }
        
            public void bark() {
                System.out.println("으르렁");
            }
        }
        
        class ZooKeeper {
            (... 생략 ...)
        }
        
        class Bouncer {
            void barkAnimal(Barkable animal) {  // Animal 대신 Barkable을 사용
                animal.bark();
            }
        }
        
        public class Sample {
            (... 생략 ...)
        }
        ```
        
        - 인터페이스는 콤마(,)를 이용하여 여러 개 implements 가능
        - Tiger, Lion 클래스
            - Predator 인터페이스와 Barkable 인터페이스를 implements
        - Tiger, Lion 클래스에 bark 메소드 구현
            - Bouncer 클래스의 barkAnimal 메소드 수정 가능
    
    - barkAnimal 메소드의 바뀌기 전과 바뀐 후
        - 바뀌기 전
            
            ```java
            void barkAnimal(Animal animal) {
                if (animal instanceof Tiger) {
                    System.out.println("어흥");
                } else if (animal instanceof Lion) {
                    System.out.println("으르렁");
                }
            }
            ```
            
        - 바뀐 후
            
            ```java
            void barkAnimal(Barkable animal) {
                animal.bark();
            }
            ```
            
        
        - barkAnimal 메소드의 입력 자료형 → Animal에서 Barkable 로 변경됨
        - animal의 객체 타입을 체크해 "어흥" 또는 "으르렁"을 출력하던 부분
            - 그냥 bark 메소드를 호출하도록 변경
        
        - tiger, lion 객체
            - Tiger, Lion 클래스의 객체이면서,
            - Animal 클래스의 객체이기도 하고,
            - Barkable, Predator 인터페이스의 객체
            - barkAnimal 메소드의 입력 자료형을 Animal에서 Barkable 로 바꾸어 사용 가능 ⇒ 다형성
    
    - **다형성(Polymorphism)**
        - 하나의 객체가 여러개의 자료형 타입을 가질 수 있는 것
        - 복잡한 형태의 분기문을 간단하게 처리할 수 있음
    
    - Tiger 클래스의 객체 → 러가지 자료형으로 표현 가능
        
        ```java
        Tiger tiger = new Tiger();  // Tiger is a Tiger
        Animal animal = new Tiger();  // Tiger is a Animal
        Predator predator = new Tiger();  // Tiger is a Predator
        Barkable barkable = new Tiger();  // Tiger is a Barkable
        ```
        
        - Predator 로 선언된 predator 객체와 Barkable 로 선언된 barkable 객체
            - 사용할 수 있는 메소드가 서로 다름
            - predator 객체
                - `getFood()`메소드가 선언된 Predator 인터페이스의 객체
                - getFood 메소드만 호출 가능
            - Barkable 로 선언된 barkable 객체
                - bark 메소드만 호출 가능
        
    - 만약 getFood 메소드와 bark 메소드를 모두 사용하고 싶다면?
        - Predator, Barkable 인터페이스를 구현한 Tiger 로 선언된 tiger 객체 그대로 사용
        - 또는 getFood, bark 메소드를 모두 포함하는 새로운 인터페이스를 만들어 사용
            
            ```java
            interface Predator {
                (... 생략 ...)
            }
            
            interface Barkable {
                void bark();
            }
            
            interface BarkablePredator extends Predator, Barkable {
            }
            
            (... 생략 ...)
            ```
            
            - 기존의 인터페이스를 상속하여 BarkablePredator 만듦
                - BarkablePredator는 Predator의 getFood 메소드, Barkable의 bark 메소드 그대로 사용 가능
            - 인터페이스는 일반 클래스와는 달리 **extends**를 이용
                - 여러 개의 인터페이스(Predator, Barkable) 동시 상속 가능
                - 즉, 다중 상속이 지원됨
        
    - Lion 클래스를 BarkablePredator 인터페이스를 구현하도록 수정
        
        ```java
        (... 생략 ...)
        
        class Lion extends Animal implements BarkablePredator {
            public String getFood() {
                return "banana";
            }
        
            public void bark() {
                System.out.println("으르렁");
            }
        }
        
        (... 생략 ...)
        ```
        
        - Lion클래스를 수정하고 Bouncer 클래스를 실행하더라도 동일한 결과값 출력
            
            ```java
            어흥
            으르렁
            ```
            
        
        - Bouncer 클래스의 barkAnimal 메소드의 입력 자료형
            - Barkable이더라도 BarkablePredator를 구현한 lion객체 전달
                - arkablePredator
                    - Barkable 인터페이스를 상속받은 자식 인터페이스
    
    - 자식 인터페이스로 생성한 객체의 자료형
        - 부모 인터페이스로 사용 가능
    
    - 전체 소스코드
        - *Sample.java*
        
        ```java
        interface Predator {
            String getFood();
        
            default void printFood() {
                System.out.printf("my food is %s\n", getFood());
            }
        
            int LEG_COUNT = 4;  // 인터페이스 상수
        
            static int speed() {
                return LEG_COUNT * 30;
            }
        }
        
        interface Barkable {
            void bark();
        }
        
        interface BarkablePredator extends Predator, Barkable {
        }
        
        class Animal {
            String name;
        
            void setName(String name) {
                this.name = name;
            }
        }
        
        class Tiger extends Animal implements Predator, Barkable {
            public String getFood() {
                return "apple";
            }
        
            public void bark() {
                System.out.println("어흥");
            }
        }
        
        class Lion extends Animal implements BarkablePredator {
            public String getFood() {
                return "banana";
            }
        
            public void bark() {
                System.out.println("으르렁");
            }
        }
        
        class ZooKeeper {
            void feed(Predator predator) {
                System.out.println("feed " + predator.getFood());
            }
        }
        
        class Bouncer {
            void barkAnimal(Barkable animal) {
                animal.bark();
            }
        }
        
        public class Sample {
            public static void main(String[] args) {
                Tiger tiger = new Tiger();
                Lion lion = new Lion();
        
                Bouncer bouncer = new Bouncer();
                bouncer.barkAnimal(tiger);
                bouncer.barkAnimal(lion);
            }
        }
        ```
        

## ****09. 추상클래스****

- 인터페이스의 역할도 하면서 클래스의 기능도 가지고 있음
- Predator 인터페이스를 추상클래스로 변경
    
    ```java
    abstract class Predator extends Animal {
        abstract String getFood();
    
        ~~default~~ void printFood() {  // default 를 제거한다.
            System.out.printf("my food is %s\n", getFood());
        }
    
        static int LEG_COUNT = 4;  // 추상 클래스의 상수는 static 선언이 필요하다.
        static int speed() {
            return LEG_COUNT * 30;
        }
    }
    
    (... 생략 ...)
    ```
    

- 추상클래스 만들기
    - class 앞에 **abstract** 라고 표기
- 인터페이스의 메소드와 같은 역할을 하는 메소드(여기서는 getFood 메소드)에도 역시 abstract를 붙여야 함
- abstract 메소드
    - 인터페이스의 메소드와 마찬가지로 몸통 없음
        - abstract 클래스를 상속하는 클래스에서 해당 abstract 메소드를 구현해야만 함
    - Animal 클래스의 기능을 유지하기 위해 Animal 클래스를 상속
- 인터페이스의 디폴트 메서드
    - 더이상 사용할 수 없음
    - default 키워드를 삭제하여 일반 메소드로 변경
- LEG_COUNT 상수도 인터페이스
    - 자동으로 static으로 인식
    - But 추상 클래스는 static 이라고 명시해줘야 함
- **추상 클래스는 일반 클래스와는 달리 단독으로 객체를 생성할 수 X**
    - **반드시 추상 클래스를 상속한 실제 클래스를 통해서만 객체 생성**

- Predator 인터페이스를 추상 클래스로 변경 시
    - BarkablePredator 인터페이스는 사용 불가능 ⇒ 삭제
    - Tiger, Lion 클래스 → Predator 추상클래스를 상속하도록 변경
    
    ```java
    abstract class Predator extends Animal {
        (... 생략 ...)
    }
    
    interface Barkable {
        (... 생략 ...)
    }
    
    ~~interface BarkablePredator extends Predator, Barkable {
    }~~
    
    class Animal {
        (... 생략 ...)
    }
    
    class Tiger extends Predator implements Barkable {
        (... 생략 ...)
    }
    
    class Lion extends Predator implements Barkable {
        (... 생략 ...)
    }
    
    class ZooKeeper {
        (... 생략 ...)
    }
    
    class Bouncer {
        (... 생략 ...)
    }
    
    public class Sample {
        (... 생략 ...)
    }
    ```
    

- Predator 추상클래스에 선언된 getFood 메소드
    - Tiger, Lion 클래스에 이미 구현되어 있음
    - 추상클래스에 abstract로 선언된 메소드
        - 인터페이스의 메소드와 마찬가지로 반드시 구현해야 하는 메소드

- 추상 클래스에는 abstract 메소드 외에 실제 메소드도 사용 가능
- 추상 클래스에 실제 메소드를 추가?
    - Tiger, Lion 등으로 만들어진 객체에서 그 메소드들을 모두 사용 가능
- 원래 인터페이스에서 default 메소드로 사용했던 printFood
    - 추상 클래스의 실제 메소드에 해당

- **인터페이스와 추상 클래스의 차이**
    - 추상 클래스
        - 일반 클래스처럼 객체변수, 생성자, private 메서드 등 **가질 수 있음**
    - 인터페이스
        - 객체변수, 생성자, private 메서드 등 **가질 수 없음**