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

- ****while문의 기본 구조****
    - while문의 기본 구조
        
        ```java
        while (조건문) {
            <수행할 문장1>;
            <수행할 문장2>;
            <수행할 문장3>;
            ...
        }
        ```
        
    - 조건문이 참인 동안 while문의 수행할 문장들을 반복하여 수행
    
    - *열 번 찍어 안 넘어 가는 나무 없다*
        
        ```java
        int treeHit = 0;
        while (treeHit < 10) {
            treeHit++;
            System.out.println("나무를  " + treeHit + "번 찍었습니다.");
            if (treeHit == 10) {
                System.out.println("나무 넘어갑니다.");
            }
        }
        ```
        
    - 출력 결과
        
        ```java
        나무를  1번 찍었습니다.
        나무를  2번 찍었습니다.
        나무를  3번 찍었습니다.
        나무를  4번 찍었습니다.
        나무를  5번 찍었습니다.
        나무를  6번 찍었습니다.
        나무를  7번 찍었습니다.
        나무를  8번 찍었습니다.
        나무를  9번 찍었습니다.
        나무를  10번 찍었습니다.
        나무 넘어갑니다.
        ```
        
        - 위의 예에서 while문의 조건문 → `treeHit < 10`
        - treeHit가 10보다 작은 동안에 while 문 안의 문장들을 계속 수행
        - 제일 먼저 `treeHit++`로 treeHit값이 계속 1씩 증가
        - 나무를 treeHit번 만큼 찍었음을 알리는 문장을 출력
        - treeHit가 10이 되면 “나무 넘어갑니다”라는 문장을 출력
        - `treeHit < 10`라는 조건문이 거짓이 되어 while문을 빠져 나감
    
    - `treeHit++`
        - 프로그래밍을 할 때 매우 자주 사용하는 기법
        - treeHit의 값을 1만큼씩 증가시킬 목적으로 쓰이는 것

- ****무한루프(Loop)****
    - 무한 루프 : 무한히 반복한다는 의미
    - 자바에서 무한루프 ⇒ while문으로 구현
    - 무한루프의 기본적인 형태
        
        ```java
        while (true) {    
            <수행할 문장1>;
            <수행할 문장2>;
            ...
        }
        ```
        
        - while의 조건문이 true 이므로 조건문은 항상 참
        - 조건문이 참인 동안 while에 속해 있는 문장들을 계속 수행
            - 무한하게 while문 내의 문장들을 수행할 것
    
    - 무한루프 예
        
        ```java
        while (true) {
            System.out.println("Ctrl-C를 눌러야 while문을 빠져 나갈 수 있습니다.");
        }
        ```
        
    - 출력결과
        
        ```java
        Ctrl-C를 눌러야 while문을 빠져 나갈 수 있습니다.
        Ctrl-C를 눌러야 while문을 빠져 나갈 수 있습니다.
        (... 생략 ...)
        ```
        
        - 위의 문장들이 영원히 출력될 것
        - 인텔리제이와 같은 IDE를 사용할 경우
            - 중지버튼("빨간색 버튼")을 눌러 프로세스 종료
    

- ****while문 빠져 나가기(break)****
    - while 문은 조건문이 참인 동안 계속해서 while문 안의 내용을 반복 수행
    - 강제로 while 문을 빠져나가야 할 때도 있음
    - 예) break의 사용
        
        ```java
        int coffee = 10;
        int money = 300;
        
        while (money > 0) {
            System.out.println("돈을 받았으니 커피를 줍니다.");
            coffee--;
            System.out.println("남은 커피의 양은 " + coffee + "입니다.");
            if (coffee == 0) {
                System.out.println("커피가 다 떨어졌습니다. 판매를 중지합니다.");
                break;
            }
        }
        ```
        
        - money가 300으로 고정
            - `while (money > 0)`에서 money는 항상 참
                - 따라서 무한 루프를 돌게 됨
        - while문이 수행되면 `coffee--`에 의해 coffee의 개수가 한 개씩 줄어듦
        - 만약 coffee가 0이 되면 `if (coffee == 0)`문장이 참
            - break가 호출되어 while문을 빠져 나감

- ****while문 조건문으로 돌아가기(continue)****
    - while문 안의 문장을 수행할 때 어떤 조건을 검사해서 조건에 맞지 않는 경우
        - while문을 빠져나가는 대신 while문의 맨 처음(조건문)으로 돌아가게 하고 싶은 경우
    - 예) continue의 사용
        - continue문
            - while문의 맨 처음(조건문: a<10)으로 돌아가게 하는 명령어
        
        ```java
        int a = 0;
        while (a < 10) {
            a++;
            if (a % 2 == 0) {
                continue;  // 짝수인 경우 조건문으로 돌아간다.
            }
            System.out.println(a);  // 홀수만 출력된다.
        }
        ```
        
        - 1부터 10까지의 수 중 홀수만을 출력하는 예
        - a가 10보다 작은 동안 a는 1만큼씩 계속 증가
        - `if (a % 2 == 0)`
            - (2로 나누었을 때 나머지가 0인 경우)이 참이 되는 경우
                - a가 짝수일 때
        - 즉, a가 짝수이면 continue 문장이 수행
        - 위의 예에서 a가 짝수
            - `System.out.println(a)`수행되지 않기 때문에 홀수만 출력

## ****04. for 문****

- ****for 문의 구조****
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

- ****for 문의 예제****
    - *총 5명의 학생이 시험을 보았는데 시험점수가 60점이 넘으면 합격이고 그렇지 않으면 불합격이다. 합격인지 불합격인지에 대한 결과를 보여준다*
        - 5명의 학생의 시험성적
            
            ```java
            int[] marks = {90, 25, 67, 45, 80};
            ```
            
        
        - 점수를 차례로 검사하여 합격여부를 알려주는 프로그램
            
            ```java
            int[] marks = {90, 25, 67, 45, 80};
            for(int i=0; i<marks.length; i++) {
                if (marks[i] >= 60) {
                    System.out.println((i+1)+"번 학생은 합격입니다.");
                }else {
                    System.out.println((i+1)+"번 학생은 불합격입니다.");
                }
            }
            ```
            
            - i값이 1씩 증가하며 for문 안의 문장들이 수행
                - marks[i]는 차례로 90, 25, 67, 45, 80의 값을 갖게 됨
            - marks[i]가 60 이상이면 합격 메시지를 출력, 60을 넘지 않으면 불합격 메시지를 출력
            - i가 marks의 갯수인 5보다 크게되면 for문이 중지됨

- ****for와 continue****
    - while 문에서 알아보았던 continue가 for 문에도 동일하게 적용
    - for문 안의 문장을 수행하는 도중에 continue문을 만나면?
        - for 문의 처음으로 돌아감
    - 60점 이상인 사람에게는 축하 메시지를 보내고 나머지 사람에게는 아무런 메시지도 전하지 않는 프로그램
        
        ```java
        int[] marks = {90, 25, 67, 45, 80};
        for(int i=0; i<marks.length; i++) {
            if (marks[i] < 60) {
                continue;
            }
            System.out.println((i+1)+"번 학생 축하합니다. 합격입니다.");
        }
        ```
        
        - 점수가 60점 미만인 학생일 경우에는 `marks[i] < 60`
        이 참이 되어 continue문이 수행
            - 축하 메시지를 출력하는 부분을 수행하지 않고, for문의 첫부분으로 돌아가게 됨
            - while 문과 마찬가지로 for 문안에서 break 문장을 만나면 for 문을 벗어남

- ****이중 for 문****
    - for 문을 두 번 이용하면 아주 간단하게 구구단 출력 가능
        
        ```java
        for(int i=2; i<10; i++) {
            for(int j=1; j<10; j++) {
                System.out.print(i*j+" ");
            }
            System.out.println("");
        }
        ```
        
        - 먼저 2부터 9까지의 숫자가 차례로 i에 대입
        - i가 처음 2일 때 다시 for 문 만남
        - 이제 1부터 9까지의 숫자가 j에 대입
        - 그 다음 문장인 `System.out.print(i*j+" ");` 수행
        - i가 2일 때 2*1*, 2*2*, 2*3*, , , ,2**9 까지 차례로 수행되며 그 값을 출력
        - 그 다음에는 i가 3일 때 역시 2일 때와 마찬가지로 수행될 것
        - 그렇게 i가 9일 때까지 계속 반복
    
    - 위에서 `System.out.print`와 `System.out.println`을 구분해 사용
    - `System.out.print`은 줄바꿈문자(`\n`)을 포함하지 않고 출력
    - `System.out.println`은 마지막에 줄바꿈문자(`\n`)을 포함하여 출력
        - 2단, 3단 처럼 한 단이 끝날때만 줄바꿈 문자를 출력하기 위해 구분하여 사용

## ****05. for each 문****

- for each 라는 키워드가 따로 있는 게 아니라 동일한 for를 이용
    - 평범한 for 문
        
        ```java
        String[] numbers = {"one", "two", "three"};
        for(int i=0; i<numbers.length; i++) {
            System.out.println(numbers[i]);
        }
        ```
        
    
    - for each 구조로 변경
        
        ```java
        String[] numbers = {"one", "two", "three"};
        for(String number: numbers) {
            System.out.println(number);
        }
        ```
        
        - for each 문은 보기에 매우 직관적
        
    - for each 문의 구조
        
        ```java
        for (type var: iterate) {
            body-of-loop
        }
        ```
        
        - iterate : 루프 돌릴 객체
        - iterate 객체에서 한개씩 순차적으로 var에 대입되어 for문이 수행됨
        - iterate로 사용할 수 있는 자료형
            - 루프를 돌릴 수 있는 자료형(배열 및 ArrayList 등)만 가능
    
    - ArrayList로 구현
        - for문의 사용법은 String[] 배열을 사용했을 때와 완전히 동일
        
        ```java
        import java.util.ArrayList;
        import java.util.Arrays;
        
        public class Sample {
            public static void main(String[] args) {
                ArrayList<String> numbers = new ArrayList<>(Arrays.asList("one", "two", "three"));
                for (String number : numbers) {
                    System.out.println(number);
                }
            }
        }
        ```
        
        - for each 문은 따로 반복회수를 명시적으로 주는 게 불가능
        - 1스텝씩 순차적으로 반복될 때만 사용 가능하다는 제약 있음
