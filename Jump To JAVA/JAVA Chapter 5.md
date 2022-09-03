# JAVA Chapter 5

문서 유형: 학습 자료
이해관계자: 익명
작성일시: 2022년 9월 3일 오후 4:44
최종 편집일시: 2022년 9월 3일 오후 11:35

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

- 

## ****04. Call by value****

- 
    - 예 1) 전형적인 for문
        
        ```java
        String[] numbers = {"one", "two", "three"};
        for(int i=0; i<numbers.length; i++) {
            System.out.println(numbers[i]);
        }
        ```
        
    - 출력결과
        
        ```java
        one
        two
        three
        ```
        
        - numbers 배열의 첫번째 요소부터 마지막 요소까지 출력하는 예
    
    - for 문의 조건문
        - 세미콜론(;)을 구분자로 세 부분으로 나뉘어 짐
        
        ```java
        for (초기치; 조건문; 증가치) {
            ...
        }
        ```
        
        - 초기치는 `int i=0`이 되고 조건문은 `i<numbers.length`, 증가치는 `i++`이 됨
            - 즉 i값이 numbers의 갯수보다 작은 동안 계속 i값을 1씩 증가시킨다는 의미

## ****05. 상속자****

## ****06. 생성자****

## ****07. 인터페이스****

## ****08. 다형성****

## ****09. 추상클래스****