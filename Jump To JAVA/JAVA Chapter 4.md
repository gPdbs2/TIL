# JAVA Chapter 4

문서 유형: 학습 자료
이해관계자: 익명
작성일시: 2022년 8월 31일 오후 4:41
최종 편집일시: 2022년 8월 31일 오후 7:31

# Chapter ****04. 제어문****

## ****01. if 문****

- 프로그래밍도 위처럼 조건을 판단해서 그 상황에 맞게 처리해야 할 경우
    - if문을 통해 조건을 판단하여 해당 조건에 맞는 상황을 수행
    
    ```java
    boolean money = true;
    if (money) {
        System.out.println("택시를 타고 가라");
    }else {
        System.out.println("걸어가라");
    }
    ```
    

- **if 문의 기본 구조**
    - if와 else를 사용하는 기본 구조
        
        ```java
        if (조건문) {
            <수행할 문장1>;
            <수행할 문장2>;
            ...
        } else {
            <수행할 문장A>;
            <수행할 문장B>;
            ...
        }
        ```
        
        - 조건문을 테스트 해서 참이면 if문에 속한 문장 수행
        - 조건문이 거짓이면 else문에 속한 문장 수행

- **조건문이란 무엇인가?**
    - `if (조건문)`에 사용한 조건문
        - 참과 거짓을 판단하는 문장
        
        ```java
        boolean money = true;
        if (money) {
        ...
        ```
        
        - money는 true
            - if문에 속한 문장들이 수행됨

- **비교연산자**
    - 비교 연산자(`<`, `>`, `==`, `!=`, `>=`, `<=`)
        - 조건판단에 사용됨
    - Java의 비교 연산자
        
        
        | 비교연산자 | 설명 |
        | --- | --- |
        | x < y | x가 y보다 작다 |
        | x > y | x가 y보다 크다 |
        | x == y | x와 y가 같다 |
        | x != y | x와 y가 같지 않다 |
        | x >= y | x가 y보다 크거나 같다 |
        | x <= y | x가 y보다 작거나 같다 |
    - 예제
        
        ```java
        int x = 3;
        int y = 2;
        System.out.println(x > y);  // true 출력
        System.out.println(x < y);  // false  출력
        System.out.println(x == y);  // false 출력
        System.out.println(x != y);  // true 출력
        ```
        
    
    - *만약 3000원 이상의 돈을 가지고 있으면 택시를 타고 그렇지 않으면 걸어가라*
        
        ```java
        int money = 2000;
        if (money >= 3000) {
            System.out.println("택시를 타고 가라");
        }else {
            System.out.println("걸어가라");
        }
        ```
        
        - `money >= 3000`이란 조건문이 거짓
            - else문의 문장이 수행되어 "걸어가라"가 출력

- **and(&&), or(||), not(!)**
    - `x || y`
        - x와 y 둘 중 적어도 하나가 참이면 참이다
    - `x && y`
        - x와 y 모두 참이어야 참이다
    - `!x`
        - x가 거짓이면 참이다
    
    - *돈이 3000원 이상 있거나 카드가 있다면 택시를 타고 그렇지 않으면 걸어가라*
        
        ```java
        int money = 2000;
        boolean hasCard = true;
        
        if (money>=3000 || hasCard) {
            System.out.println("택시를 타고 가라");
        } else {
            System.out.println("걸어가라");
        }
        ```
        
        - money는 2000으로 3000보다 작지만 hasCard가 true
            - `money >= 3000 || hasCard`조건문이 참
                - "택시를 타고 가라"가 출력

- **contains**
    - contains 메소드
        - 해당 아이템이 있는지 조사
    
    - *만약 주머니에 돈이 있으면 택시를 타고, 없으면 걸어가라*
        
        ```java
        ArrayList<String> pocket = new ArrayList<String>();
        pocket.add("paper");
        pocket.add("handphone");
        pocket.add("money");
        
        if (pocket.contains("money")) {
            System.out.println("택시를 타고 가라");
        }else {
            System.out.println("걸어가라");
        }
        ```
        
        - pocket 리스트에 안에 'money’
            - `pocket.contains("money")`가 참
                - "택시를 타고 가라"가 출력

- **else if (다중 조건 판단)**
    - if와 else만으로는 다양한 조건 판단을 하기가 어려움
    - *지갑에 돈이 있으면 택시를 타고, 지갑엔 돈이 없지만 카드가 있으면 택시를 타고, 돈도 없고 카드도 없으면 걸어가라*
        - 먼저 지갑에 돈이 있는지를 판단
        - 지갑에 돈이 없으면 다시 카드가 있는지를 판단
        
        ```java
        boolean hasCard = true;
        ArrayList<String> pocket = new ArrayList<String>();
        pocket.add("paper");
        pocket.add("handphone");
        
        if (pocket.contains("money")) {
            System.out.println("택시를 타고 가라");
        }else {
            if (hasCard) {
                System.out.println("택시를 타고 가라");
            }else {         
                System.out.println("걸어가라");
            }
        }
        ```
        
    - if와 else가 여러번 사용되어 이해하기가 쉽지 않고 산만한 느낌
        - 보완하기 위해서 자바는 다중 조건 판단을 가능하게 하는 `else if` 있음

- `else if`를 적용한 코드
    
    ```java
    boolean hasCard = true;
    ArrayList<String> pocket = new ArrayList<String>();
    pocket.add("paper");
    pocket.add("handphone");
    
    if (pocket.contains("money")) {
        System.out.println("택시를 타고 가라");
    }else if(hasCard) {
        System.out.println("택시를 타고 가라");
    }else {         
        System.out.println("걸어가라");
    }
    ```
    
    - `else if`는 이전 조건문이 거짓일 때 수행
    - `pocket.contains("money")` 문장이 거짓
        - `else if`문이 수행됨, hasCard가 true이므로 "택시를 타고 가라" 출력
    
- if, else if, else의 기본 구조
    
    ```java
    if (조건문) {
        <수행할 문장1> 
        <수행할 문장2>
        ...
    }else if (조건문) {
        <수행할 문장1>
        <수행할 문장2>
        ...
    }else if (조건문) {
        <수행할 문장1>
        <수행할 문장2>
        ...
    ...
    } else {
       <수행할 문장1>
       <수행할 문장2>
       ... 
    }
    ```
    
- else if는 개수에 제한 없이 사용 가능

## ****02. switch / case 문****

- **switch/case 문**
    - if 문과 비슷하지만 좀 더 정형화된 조건 판단문

- **switch/case 문 구조**
    
    ```java
    switch(입력변수) {
        case 입력값1: ...
             break;
        case 입력값2: ...
             break;
        ...
        default: ...
             break;
    }
    ```
    
    - 입력변수의 값과 일치하는 case 입력값(입력값1, 입력값2, ...)이 있다면?
        - 해당 case문에 속한 문장들이 실행
    - case문마다 break 라는 문장이 있음
        - 해당 case문을 실행 한 뒤 switch문을 빠져나가기 위한 것
    - 만약 break 문이 빠져 있다면 그 다음의 case 문이 실행
    
    - switch/case 문을 가장 잘 설명하는 예
        
        ```java
        public class Sample {
            public static void main(String[] args) {
                int month = 8;
                String monthString = "";
                switch (month) {
                    case 1:  monthString = "January";
                             break;
                    case 2:  monthString = "February";
                             break;
                    case 3:  monthString = "March";
                             break;
                    case 4:  monthString = "April";
                             break;
                    case 5:  monthString = "May";
                             break;
                    case 6:  monthString = "June";
                             break;
                    case 7:  monthString = "July";
                             break;
                    case 8:  monthString = "August";
                             break;
                    case 9:  monthString = "September";
                             break;
                    case 10: monthString = "October";
                             break;
                    case 11: monthString = "November";
                             break;
                    case 12: monthString = "December";
                             break;
                    default: monthString = "Invalid month";
                             break;
                }
                System.out.println(monthString);
            }
        }
        ```
        
        - switch문의 입력이 1이면 "January"라는 문자열이, 12면 "December"라는 문자열이 출력되는 예제
            - month가 8로 고정되어 있기 때문에 "August"라는 문자열이 출력
            - 위 switch문은 month의 값이 1이면 case 1: 문장이 실행
            - 2이면 case 2: 문장이, 3이면 case 3: ... 이런식으로 수행
            - month에 1에서 12사이의 숫자가 아닌 다른 값이 저장되어 있을 경우
                - default: 문장이 수행
    - 입력값이 정형화되어 있는 경우 if문보다는 switch/case문을 쓰는 것이 가독성에서 좀 더 유리
    - switch/case문은 if else 구조로 변경이 가능
    - if else 구조로 작성된 모든 코드를 switch 문으로 변경할 수는 없음

## ****03. while 문****

- 

## ****04. for 문****

- 

## ****05. for each 문****