# JAVA Chapter 7. 자바 날개 달기

## 자바의 디렉토리

- **패키지**
    - 비슷한 성격의 자바 클래스들을 모아 놓은 것

## ****01. 패키지 (Package)****

- ****패키지 (Package)****
    - ex 1. 패키지 생성
        
        ![Untitled](JAVA%20Chapter%207%20%E1%84%8C%E1%85%A1%E1%84%87%E1%85%A1%20%E1%84%82%E1%85%A1%E1%86%AF%E1%84%80%E1%85%A2%20%E1%84%83%E1%85%A1%E1%86%AF%E1%84%80%E1%85%B5%2086d947abeb9a492e9685cafb38ec2409/Untitled.png)
        
        - 클래스 생성
            
            ![Untitled](JAVA%20Chapter%207%20%E1%84%8C%E1%85%A1%E1%84%87%E1%85%A1%20%E1%84%82%E1%85%A1%E1%86%AF%E1%84%80%E1%85%A2%20%E1%84%83%E1%85%A1%E1%86%AF%E1%84%80%E1%85%B5%2086d947abeb9a492e9685cafb38ec2409/Untitled%201.png)
            
            - house 패키지에서 클래스를 생성
                - `package house;`와 같은 문장이 자동 삽입
        
        - *house/HouseKim.java*
            
            ```java
            package house;
            
            public class HouseKim {
            }
            ```
            
        
        - *house/HousePark.java*
            
            ```java
            package house;
            
            public class HousePark {
            }
            ```
            
        
        - **package** 키워드 : 이 파일이 어떤 패키지의 파일인지를 알려주는 역할

- ****서브패키지 (Subpackage)****
    - ex 2.  house 패키지에서 다시 하위 패키지 생성
        
        ![Untitled](JAVA%20Chapter%207%20%E1%84%8C%E1%85%A1%E1%84%87%E1%85%A1%20%E1%84%82%E1%85%A1%E1%86%AF%E1%84%80%E1%85%A2%20%E1%84%83%E1%85%A1%E1%86%AF%E1%84%80%E1%85%B5%2086d947abeb9a492e9685cafb38ec2409/Untitled%202.png)
        
        - person 패키지로 이동하여 EungYongPark 클래스 생성
            - *house/person/EungYongPark.java*
            
            ```java
            package house.person;
            
            public class EungYongPark {
            }
            ```
            
            - `src/house/person`디렉토리에서 `New -> Java Class`를 선택
            - 자바 클래스명에 `EungYongPark`이라고 입력하면 생성됨
        
    - 패키지는 도트(`.`)를 이용하여 하위 패키지 표시
        - `house.person` → `house`패키지의 서브패키지

- ****패키지 사용하기****
    - 다른 클래스에서 HouseKim 클래스를 사용하려면 impor 해야 함
        
        ```java
        import house.HouseKim;
        ```
        
    
    - `*`기호를 이용할 수도 있음
        - house 패키지내의 모든 클래스 사용 가능
        
        ```java
        import house.*;
        ```
        
    
    - 같은 패키지 내에서는 import 없이 사용 가능

- ****패키지를 사용하는 이유****
    - 비슷한 성격의 클래스들끼리 묶을 수 있어 **클래스의 분류가 용이**
    - **패키지명이 다르면 클래스명이 동일해도 충돌없이 사용 가능**

## ****02. 접근제어자 (Access Modifier)****

- ****접근 제어자****
    - 변수나 메소드의 사용 권한은 접근 제어자를 사용하여 설정 가능
        1. private
        2. default
        3. protected
        4. public
    - `private -> default -> protected -> public`순으로 보다 많은 접근을 허용
    
    - ****private****
        - private 이 붙은 변수, 메소드
            - 해당 클래스에서만 접근 가능
            
            ```java
            public class Sample {
                private String secret;
                private String getSecret() {
                    return this.secret;
                }
            }
            ```
            
            - secret 변수와 getSecret 메소드
                - 오직 Sample 클래스에서만 접근 가능
                - 다른 클래스에서는 접근 불가
    
    - ****default****
        - 접근 제어자가 없는 변수, 메소드
            - default 접근 제어자가 되어 해당 패키지 내에서만 접근 가능
            - *house/HouseKim.java*
                
                ```java
                package house;  // 패키지가 동일하다.
                
                public class HouseKim {
                    String lastname = "kim";  // lastname은 default 접근제어자로 설정된다.
                }
                ```
                
            
            - *house/HousePark.java*
                
                ```java
                package house;  // 패키지가 동일하다.
                
                public class HousePark {
                    String lastname = "park";
                
                    public static void main(String[] args) {
                        HouseKim kim = new HouseKim();
                        System.out.println(kim.lastname);  // HouseKim 클래스의 lastname 변수를 사용할 수 있다.
                    }
                }
                ```
                
            
            - HouseKim과 HousePark의 패키지는 **house**로 동일
                - HousePark 클래스에서 HouseKim의 lastname 변수에 접근 가능
    
    - ****protected****
        - protected가 붙은 변수, 메소드
            - 동일 패키지의 클래스, 해당 클래스를 상속받은 다른 패키지의 클래스에서만 접근 가능
            - *house/HousePark.java*
                
                ```java
                package house;  // 패키지가 서로 다르다.
                
                public class HousePark {
                    protected String lastname = "park";
                }
                ```
                
            
            - *house/person/EungYongPark.java*
                
                ```java
                package house.person;  // 패키지가 서로 다르다.
                
                import house.HousePark;
                
                public class EungYongPark extends HousePark {  // HousePark을 상속했다.
                    public static void main(String[] args) {
                        EungYongPark eyp = new EungYongPark();
                        System.out.println(eyp.lastname);  // 상속한 클래스의 protected 변수는 접근이 가능하다.
                    }
                }
                ```
                
            
            - HousePark 클래스를 상속한 EungYongPark 클래스의 패키지 `house.person`
                - HousePark의 패키지인 `house`와 다르지만 HousePark의 lastname 변수가 protected
                    - `eyp.lastname`과 같은 접근 가능
                - 만약 lastname의 접근제어자가 protected 가 아닌 default 접근제어자?
                    - eyp.lastname 문장은 컴파일 오류 발생
            
    
    - ****public****
        - public 접근제어자가 붙은 변수, 메소드
            - 어떤 클래스에서라도 접근 가능
                
                ```java
                package house;
                
                public class HousePark {
                    protected String lastname = "park";
                    public String info = "this is public message.";
                }
                ```
                
            - HousePark의 info 변수 → public 접근 제어자 붙어 있음
                - 어떤 클래스라도 접근 가능

- ****클래스, 메소드의 접근 제어자****
    - 접근제어자를 모두 public으로 설정해도 프로그램은 잘 동작할 것
    - 접근제어자 이용 시 장점
        - 프로그래머의 코딩 실수를 방지
        - 기타 위험요소 제거 가능

## 03. ****정적(static) 변수와 메소드****

- ****static 변수****
    - *Sample.java*
        
        ```java
        class HouseLee {
            String lastname = "이";
        }
        
        public class Sample {
            public static void main(String[] args) {
                HouseLee lee1 = new HouseLee();
                HouseLee lee2 = new HouseLee();
            }
        }
        ```
        
        - 클래스를 만들고 객체를 생성하면 객체마다 객체변수를 저장하기 위한 메모리가 별도로 할당
        - 항상 값이 변하지 않는 경우라면 static 사용시 효율적
    - 예제 변경
        
        ```java
        class HouseLee {
            static String lastname = "이";
        }
        
        public class Sample {
            public static void main(String[] args) {
                HouseLee lee1 = new HouseLee();
                HouseLee lee2 = new HouseLee();
            }
        }
        ```
        
        - lastname 변수에 static 키워드
            - 자바는 메모리 할당을 딱 1번만 하게 됨 → 메모리 사용에 이점
        - 만약 HouseLee 클래스의 lastname 값이 변경되지 않기를 바란다면?
            - static 키워드 앞에 `final`이라는 키워드 붙이면 됨
            - final 키워드 → 한 번 설정되면 그 값을 변경할 수 없음
                - 변경하려고 하면 오류 발생
        
    - static을 사용하는 또 한 가지 이유 ⇒ **공유** 개념
        - static 으로 설정하면 같은 곳의 메모리 주소만을 바라봄
            - static 변수의 값을 공유하게 되는 것
        - 웹 사이트 방문시마다 조회수를 증가시키는 Counter 클래스
            
            ```java
            class Counter  {
                int count = 0;
                Counter() {
                    this.count++;
                    System.out.println(this.count);
                }
            }
            
            public class Sample {
                public static void main(String[] args) {
                    Counter c1 = new Counter();
                    Counter c2 = new Counter();
                }
            }
            ```
            
            - 결과값
                
                ```java
                1
                1
                ```
                
            
            - c1, c2 객체 생성시 생성자에서 객체변수인 count의 값을 1씩 증가
            - But c1과 c2의 count는 서로 다른 메모리를 가리킴
                - 원하던 결과(카운트가 증가된 결과)가 나오지 않음
            - 객체변수는 항상 독립적인 값을 갖기 때문에 당연한 결과
            
            ```java
            class Counter  {
                static int count = 0;
                Counter() {
                    count++;  // count는 더이상 객체변수가 아니므로 this를 제거하는 것이 좋다.
                    System.out.println(count);  // this 제거
                }
            }
            
            public class Sample {
                public static void main(String[] args) {
                    Counter c1 = new Counter();
                    Counter c2 = new Counter();
                }
            }
            ```
            
            - `int count = 0`앞에 static 키워드를 붙였더니 count 값이 공유
                - count가 증가되어 출력
                
                ```java
                1
                2
                ```
                
        
        - 보통 변수의 static 키워드
            - 프로그래밍시 메모리의 효율보다는 공유의 목적으로 훨씬 더 많이 사용

- ****static 메소드****
    - static이라는 키워드가 메소드 앞에 붙으면 스태틱 메소드(static method)가 됨
        
        ```java
        class Counter  {
            static int count = 0;
            Counter() {
                count++;
                System.out.println(count);
            }
        
            public static int getCount() {
                return count;
            }
        }
        
        public class Sample {
            public static void main(String[] args) {
                Counter c1 = new Counter();
                Counter c2 = new Counter();
        
                System.out.println(Counter.getCount());  // 스태틱 메서드는 클래스를 이용하여 호출
            }
        }
        ```
        
        - Counter 클래스에 `getCount()`라는 static 메소드 추가
    
    - 메소드 앞에 static 키워드
        - 객체 생성없이 클래스를 통해 메서드를 직접 호출 가능 (`Counter.getCount()`)
    - 스태틱 메소드 안에서는 객체변수 접근 불가능
        - 위 예제는 count 변수가 static 변수이기 때문에 스태틱 메소드(static method)에서 접근 가능
    
    - 보통 스태틱 메소드는 유틸리티성 메소드를 작성할 때 많이 사용
        - ex. "오늘의 날짜 구하기", "숫자에 콤마 추가하기" 등 ⇒ 클래스 메소드 사용하는 게 유리
        - "날짜"를 구하는 Util 클래스의 예
            
            ```java
            import java.text.SimpleDateFormat;
            import java.util.Date;
            
            class Util {
                public static String getCurrentDate(String fmt) {
                    SimpleDateFormat sdf = new SimpleDateFormat(fmt);
                    return sdf.format(new Date());
                }
            }
            
            public class Sample {
                public static void main(String[] args) {
                    System.out.println(Util.getCurrentDate("yyyyMMdd"));  // 오늘 날짜 출력
                }
            }
            ```
            

- ****싱글톤 패턴 (singleton pattern)****
    - 싱글톤
        - 단 하나의 객체만을 생성하게 강제하는 패턴
        - 클래스를 통해 생성할 수 있는 객체는 Only One, 즉, 한 개만 되도록 만드는 것
        
        - *Sample.java*
            
            ```java
            class Singleton {
                private Singleton() {
                }
            }
            
            public class Sample {
                public static void main(String[] args) {
                    Singleton singleton = new Singleton();  // 컴파일 오류가 발생한다.
                }
            }
            ```
            
            - 위와 같은 코드를 작성하면 컴파일 에러가 발생
                - Singleton 클래스의 생성자에 private 키워드
                    - 다른 클래스에서 Singleton 클래스의 생성자로의 접근을 막음
            - 생성자를 private 으로 만들어 버리면?
                - 다른 클래스에서 Singleton 클래스를 `new`를 이용하여 생성할 수 X
            - `new`를 이용하여 무수히 많은 객체를 생성한다면?
                - 싱글톤의 정의에 어긋남
                - 일단 `new`로 객체를 생성할 수 없도록 막은 것
            
        - Singletone 클래스의 객체 생성
            
            ```java
            class Singleton {
                private Singleton() {
                }
            
                public static Singleton getInstance() {
                    return new Singleton();  // 같은 클래스이므로 생성자 호출이 가능하다.
                }
            }
            
            public class Sample {
                public static void main(String[] args) {
                    Singleton singleton = Singleton.getInstance();
                }
            }
            ```
            
            - 이제 getInstance라는 static 메소드를 이용하여 Singleton 클래스의 객체 생성 가능
            - getInstance를 호출 할 때마다 새로운 객체 생성됨
        
        - 코드 추가 작성
            
            ```java
            class Singleton {
                private static Singleton one;
                private Singleton() {
                }
            
                public static Singleton getInstance() {
                    if(one==null) {
                        one = new Singleton();
                    }
                    return one;
                }
            }
            
            public class Sample {
                public static void main(String[] args) {
                    Singleton singleton1 = Singleton.getInstance();
                    Singleton singleton2 = Singleton.getInstance();
                    System.out.println(singleton1 == singleton2);  // true 출력
                }
            }
            ```
            
            - Singleton 클래스에 one 이라는 static 변수를 둠
            - getInstance 메소드에서 one 값이 null 인 경우에만 객체를 생성하도록 함
                - one 객체가 딱 한 번만 만들어지도록 함
        
        - getInstance 메소드의 동작원리
            - 최초 getInstance가 호출되면 one이 null ⇒ `new`에 의해서 객체가 생성됨
            - 한 번 생성이 되면 one은 static 변수이므로 그 이후로는 null 아니게 됨
            - 그런 후에 다시 getInstance 메소드가 호출
                - 이제 one은 null이 아니므로 이미 만들어진 싱글톤 객체인 one을 항상 리턴
            - main 메소드에서 getInstance를 두 번 호출
                - 각각 얻은 객체가 같은 객체인가?
                    - "true"가 출력 ⇒ 같은 객체임을 확인

## 04. ****예외처리 (Exception)****

## 05. ****쓰레드(Thread)****

## 06. ****함수형 프로그래밍****