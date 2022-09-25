# Chapter ****06. 입출력****

## ****01. 콘솔 입출력****

- **콘솔 입출력**
    - 콘솔 **출력** : **사용자에게** 문자열을 **보여주는 것**
    - 콘솔 **입력** : **사용자가** 답변을 **입력하는 것**

- **콘솔이란**
    - 콘솔은 환경에 따라 변경될 수 있음
    - 인텔리제이에서 실행했다면 인텔리제이의 콘솔창이 콘솔
    - 윈도우 명령창에서 이 프로그램을 실행했다면 명령창이 콘솔
    - **사용자의 입력을 받거나 사용자에게 문자열을 출력해 주는 역할을 하는 것을 통칭**

- **콘솔 입력**
    - 사용자가 입력한 문자열
    - 이를 얻기 위해 자바의 `System.in` 사용
        
        ```java
        import java.io.IOException;
        import java.io.InputStream;
        
        public class Sample {
            public static void main(String[] args) throws IOException {
                InputStream in = System.in;
        
                int a;
                a = in.read();
        
                System.out.println(a);
            }
        }
        ```
        
        - `InputStream` → 자바의 내장 클래스
        - 내장 클래스중에 `java.lang`패키지에 속해 있지 않은 클래스
            - 필요할 때 항상 `import`해서 사용
        - `System.in` → InputStream의 객체임
            
            ```java
            InputStream in = System.in;
            ```
            
        - InputStream의 read메소드
            - 1 byte의 사용자의 입력을 받아들임
                
                ```java
                int a;
                a = in.read();
                ```
                
            - read 메소드로 읽은 1 byte의 데이터
                - byte 자료형으로 저장되는 것이 아니라 int 자료형으로 저장
            - 저장되는 int 값
                - 0-255 사이의 정수 값 ⇒ 아스키 코드값
                    - `0` 아스키코드값은 48
                    - `a` 아스키코드값은 97
            
        - 프로그램을 실행
            - 프로그램은 종료되지 않고 사용자의 입력을 대기
                - InputStream의 read()메소드가 호출되면 사용자의 입력을 받을 때까지 프로그램이 대기하기 때문
                - 엔터키를 입력해야 사용자의 입력이 종료되고 프로그램에 전달
        - 출력이 되고 프로그램은 종료될 것
            
            ```java
            97
            ```
            
        
        - **IOException**
            - main 메소드 → `throws IOException` 사용
            - InputStream으로 부터 값을 읽어들일 때는 IOException이 발생할 수 있음 ⇒ 예외처리 해야 함
            - throws로 그 예외처리를 뒤로 미루게 한 것
        
    - ****InputStream****
        - **입력 스트림(Stream)**
            - 사용자가 전달한 1 byte의 데이터 또는 3 byte의 데이터
        - **스트림(Stream)**
            - 이어져 있는 데이터(byte)의 형태
            - 파일 데이터 (파일은 그 시작과 끝이 있는 데이터의 스트림)
            - HTTP 송수신 데이터 (브라우저가 요청하고 서버가 응답하는 HTTP 형태의 데이터)
            - 키보드 입력 (사용자가 키보드로 입력하는 문자열)
        
        - 사용자가 3 byte를 입력했을 때 3 byte를 전부 읽고 싶다면
            
            ```java
            import java.io.IOException;
            import java.io.InputStream;
            
            public class Sample {
                public static void main(String[] args) throws IOException {
                    InputStream in = System.in;
            
                    int a;
                    int b;
                    int c;
            
                    a = in.read();
                    b = in.read();
                    c = in.read();
            
                    System.out.println(a);
                    System.out.println(b);
                    System.out.println(c);
                }
            }
            ```
            
            - read() 메소드를 3번 실행하도록 수정하고 프로그램을 다시 실행
                - "abc" 입력시 총 3 byte를 읽어들이는 것을 확인
                
                ```java
                abc (입력 + 엔터)
                97 (출력)
                98 (출력)
                99 (출력)
                ```
                
            
            - 좀 더 개선된 방법
                
                ```java
                import java.io.IOException;
                import java.io.InputStream;
                
                public class Sample {
                    public static void main(String[] args) throws IOException {
                        InputStream in = System.in;
                
                        byte[] a = new byte[3];
                        in.read(a);
                
                        System.out.println(a[0]);
                        System.out.println(a[1]);
                        System.out.println(a[2]);
                    }
                }
                ```
                
                - 길이 3 짜리 byte배열을 만든 후 read 메소드의 입력값으로 전달
                    - 콘솔 입력이 해당 배열에 저장
                    - 프로그램을 실행해 보면 이전과 동일한 결과가 출력
                
                ```java
                abc (입력)
                97 (출력)
                98 (출력)
                99 (출력)
                ```
                
    
    - ****InputStreamReader****
        - 읽어들인 값을 항상 아스키코드 값으로 해석해야 하는 방식 → 불편
        - 우리가 입력한 문자값을 그대로 출력?
            - 바이트 대신 문자로 입력 스트림 읽으려면 `InputStreamReader` 사용
            
            ```java
            import java.io.IOException;
            import java.io.InputStream;
            import java.io.InputStreamReader;
            
            public class Sample {
                public static void main(String[] args) throws IOException {
                    InputStream in = System.in;
                    InputStreamReader reader = new InputStreamReader(in);
                    char[] a = new char[3];
                    reader.read(a);
            
                    System.out.println(a);
                }
            }
            ```
            
            - InputStreamReader를 사용하기 위해 import 문이 하나 더 추가됨
            - InputStreamReader 객체를 생성할 때
                - 생성자의 입력으로 InputStream 객체가 필요
                
                ```java
                InputStreamReader reader = new InputStreamReader(in);
                ```
                
            - 이전에는 읽어들일 값을 byte배열로 선언
            - InputStreamReader를 이용하면 byte 대신 char 배열 사용
                
                ```java
                char[] a = new char[3];
                ```
                
            - 프로그램을 실행하고 "abc" 입력 후 엔터키로 사용자 입력을 전달
                - "abc"라는 문자열이 한꺼번에 출력되는 것을 확인
                
                ```java
                abc (입력)
                abc (출력)
                ```
                
    
    - ****BufferedReader****
        - 사용자가 엔터키를 입력할 때까지 사용자의 입력을 전부 받아들일 수는 없을까?
            - `BufferedReader` 이용하면 가능
            
            ```java
            import java.io.IOException;
            import java.io.BufferedReader;
            import java.io.InputStream;
            import java.io.InputStreamReader;
            
            public class Sample {
                public static void main(String[] args) throws IOException {
                    InputStream in = System.in;
                    InputStreamReader reader = new InputStreamReader(in);
                    BufferedReader br = new BufferedReader(reader);
            
                    String a = br.readLine();
                    System.out.println(a);
                }
            }
            ```
            
            - BufferedReader를 이용하기 위해 import 문이 추가
        - **BufferedReader**
            - 체 생성시 생성자의 입력값으로 InputStreamReader의 객체 필요
            - 이제 BufferedReader의 readLine메소드 이용 시
                - 사용자가 엔터키를 입력할 때까지 입력했던 문자열 전부 읽을 수 있게 됨
            
            ```java
            Hello World (입력)
            Hello World (출력)
            ```
            
        
    
    - **기억하면 좋을 것**
        - InputStream - byte
        - InputStreamReader - character
        - BufferedReader - String
    
    - ****Scanner****
        - J2SE 5.0 부터 Scanner 라는 `java.util.Scanner`클래스 새로 추가
        - Scanner 클래스를 이용 → 콘솔입력을 보다 쉽게 처리 가능
        
        ```java
        import java.util.Scanner;
        
        public class Sample {
            public static void main(String[] args) {
                Scanner sc = new Scanner(System.in);
                System.out.println(sc.next());
            }
        }
        ```
        
        - Scanner 를 사용하기 위해서는 먼저 java.util.Scanner 클래스 import
            
            ```java
            import java.util.Scanner;
            ```
            
        
        - **Scanner 클래스**
            - 생성자의 입력으로 `System.in`  ⇒ 콘솔입력인 InputStream을 필요로 함
        - **Scanner 객체의 `next()`메소드**
            - 단어 하나(Token)를 읽어들임
            - Scanner 클래스에는 단어 뿐만 아니라 숫자, 문자열등 다양하게 읽어 들일 수 있는 여러 메소드 존재
                - next - 단어
                - nextLine - 라인
                - nextInt - 정수

- ****콘솔 출력****
    - `System.out` : PrintStream 클래스의 객체
    - PrintStream : 콘솔에 값을 출력할 때 사용되는 클래스
    - `System.out.println`
        - 콘솔에 문자열을 출력할 경우나 디버깅 시 많이 사용
    - `System.err`
        - `System.out`과 동일한 역할
        - 오류메시지를 출력할 경우에 사용
    
    - **Unix 콘솔의 System.out과 System.err**
        - Unix의 경우 콘솔 프로그램 실행시 출력 옵션을 지정하면 System.out으로 출력한 내용과 System.err로 출력한 내용을 별도의 파일로 저장 가능
        
        ```java
        public class Sample {
            public static void main(String[] args) {
                System.out.println("일반 출력");
                System.err.println("에러 출력");
            }
        }
        ```
        
        - Sample.java 소스를 컴파일하여 Sample.class 파일을 생성한 후 유닉스에서 실행
            - out.txt 파일 → "일반 출력" 이라는 문자열 저장
            - error.txt 파일 → "에러 출력"이라는 문자열 저장
            
            ```java
            $ java Sample > out.txt 2> error.txt
            ```
            
            - 유닉스에서
                - `>`는 일반 출력
                - `2>`는 오류 출력

## ****02. 파일 입출력****

- ****파일 쓰기****
    
    ```java
    import java.io.FileOutputStream;
    import java.io.IOException;
    
    public class Sample {
        public static void main(String[] args) throws IOException {
            FileOutputStream output = new FileOutputStream("c:/out.txt");
            output.close();
        }
    }
    ```
    
    - 예제 실행
        - `c:/`디렉토리 바로 밑에 새로운 파일(out.txt)이 하나 생성되는 것을 확인 가능
    - 파일을 생성하기 위해 FileOutputStream 클래스 사용
    - FileOutputStream 객체 생성
        - 생성자의 입력으로 파일명을 넘겨줘야 함
        - 위 예제는 경로를 포함하여 `c:/out.txt`라는 파일명을 생성자의 입력으로 전달
    - `output.close()`
        - 사용한 파일 객체를 닫아주는 것
        - 생략 가능
            - 자바 프로그램이 종료할 때 사용한 파일 객체를 자동으로 닫아줌
        - 직접 사용한 파일을 닫아주는 것이 좋음
            - 사용했던 파일을 닫지 않고 다시 사용하려고 할 경우에는 오류 발생
    
    - ****FileOutputStream****
        - 생성하는 파일에 내용 기재
            
            ```java
            import java.io.FileOutputStream;
            import java.io.IOException;
            
            public class Sample {
                public static void main(String[] args) throws IOException {
                    FileOutputStream output = new FileOutputStream("c:/out.txt");
                    for(int i=1; i<11; i++) {
                        String data = i+" 번째 줄입니다.\r\n";
                        output.write(data.getBytes());
                    }
                    output.close();
                }
            }
            ```
            
        - OutputStream
            - 역시 바이트 단위로 데이터를 처리하는 클래스
        - FileOutputStream
            - OutputStream클래스를 상속받아 만든 클래스
            - 바이트 단위로 데이터 처리하게끔 되어 있음
        - FileOutputStream에 값을 쓸 때는 byte배열로 써야 함
            - `getBytes()`메소드 이용
                - String을 byte배열로 바꾸어 줌
            - `\r\n` : 줄바꿈 문자
    
    - ****FileWriter****
        - 문자열을 파일에 쓸 때에는 FileOutputStream이 불편
            - String을 byte배열로 변환해야 하기 때문
            
            ```java
            import java.io.FileWriter;
            import java.io.IOException;
            
            public class Sample {
                public static void main(String[] args) throws IOException {
                    FileWriter fw = new FileWriter("c:/out.txt");
                    for(int i=1; i<11; i++) {
                        String data = i+" 번째 줄입니다.\r\n";
                        fw.write(data);
                    }
                    fw.close();
                }
            }
            ```
            
            - FileOutputStream 대신에 FileWriter를 이용
                - byte 배열 대신 문자열 사용할 수 있어 편리
    
    - ****PrintWriter****
        - FileWriter를 사용하더라도 `\r\n`을 문자열 뒤에 덧 붙여야 하는 불편함은 여전히 남아있음
        - 이런 불편함을 해소하려면 FileWriter대신 PrintWriter를 사용
        - PrintWriter를 이용
            - `\r\n`을 덧붙이는 대신 `println`이라는 메소드 사용
        - PrintWriter를 이용하여 파일을 작성하는 예제
            
            ```java
            import java.io.IOException;
            import java.io.PrintWriter;
            
            // 콘솔 대신 파일로 출력하는 방법
            public class Sample {
                public static void main(String[] args) throws IOException {
                    PrintWriter pw = new PrintWriter("c:/out.txt");
                    for(int i=1; i<11; i++) {
                        String data = i+" 번째 줄입니다.";
                        pw.println(data);
                    }
                    pw.close();
                }
            }
            ```
            
        
        - 프로그램 비교
        
        ```java
        // 콘솔 출력 방법
        for(int i=1; i<11; i++) {
            String data = i+" 번째 줄입니다.";
            System.out.println(data);
        }
        ```
        
        - 두 프로그램의 차이점 → data를 출력시키는 방법
            - 첫 번째 방법 : 콘솔 대신 파일로 출력하는 방법
            - 두 번째 방법 : 콘솔 출력 방법
            - `System.out`대신 PrintWriter의 객체를 사용한 차이가 있을 뿐
        
        - 프로그램을 실행 → `c:/out.txt`파일 생성
            
            *[out.txt의 내용]*
            
            ```java
            1 번째 줄입니다.
            2 번째 줄입니다.
            3 번째 줄입니다.
            4 번째 줄입니다.
            5 번째 줄입니다.
            6 번째 줄입니다.
            7 번째 줄입니다.
            8 번째 줄입니다.
            9 번째 줄입니다.
            10 번째 줄입니다.
            ```
            
            - 두 번째 방법을 사용했을 때
                - 콘솔에 출력될 내용이 파일에 고스란히 들어가 있음
            
    - ****파일에 내용 추가하기****
        - 파일에 내용을 쓰고 난 후에 또 새로운 내용을 추가하고 싶을 때
            - 이미 작성된 파일을 다시 **추가모드**로 열어서 추가내용 작성
            
            ```java
            import java.io.FileWriter;
            import java.io.IOException;
            
            public class Sample {
                public static void main(String[] args) throws IOException {
                    FileWriter fw = new FileWriter("c:/out.txt");
                    for(int i=1; i<11; i++) {
                        String data = i+" 번째 줄입니다.\r\n";
                        fw.write(data);
                    }
                    fw.close();
            
                    FileWriter fw2 = new FileWriter("c:/out.txt", true);  // 파일을 추가 모드로 연다.
                    for(int i=11; i<21; i++) {
                        String data = i+" 번째 줄입니다.\r\n";
                        fw2.write(data);
                    }
                    fw2.close();
                }
            }
            ```
            
            - fw2 객체
                - `FileWriter("c:/out.txt", true)` 와 같이 두번째 파라미터를 추가로 전달하여 생성
            - 두번째 boolean 입력 파라미터
                - 파일을 추가모드(append)로 열 것인지에 대한 구분값
                - 파일을 추가모드로 열면 기존파일의 내용을 덮어쓰지 않고 이후부터 파일이 쓰여짐
                - 예제를 실행하면 out.txt 파일에 내용이 추가되는 것 확인
        
        - FileWriter대신 PrintWriter를 이용하고 싶은 경우
            
            ```java
            import java.io.FileWriter;
            import java.io.IOException;
            import java.io.PrintWriter;
            
            public class Sample {
                public static void main(String[] args) throws IOException {
                    PrintWriter pw = new PrintWriter("c:/out.txt");
                    for(int i=1; i<11; i++) {
                        String data = i+" 번째 줄입니다.";
                        pw.println(data);
                    }
                    pw.close();
            
                    PrintWriter pw2 = new PrintWriter(new FileWriter("c:/out.txt", true));
                    for(int i=11; i<21; i++) {
                        String data = i+" 번째 줄입니다.";
                        pw2.println(data);
                    }
                    pw2.close();
                }
            }
            ```
            
            - PrintWriter를 사용할 경우
                - 생성자의 파라미터로 파일명 대신 추가모드로 열린 FileWriter의 객체 전달

- ****파일 읽기****
    - 파일을 읽는 방법
        
        ```java
        import java.io.FileInputStream;
        import java.io.IOException;
        
        public class Sample {
            public static void main(String[] args) throws IOException {
                byte[] b = new byte[1024];
                FileInputStream input = new FileInputStream("c:/out.txt");
                input.read(b);
                System.out.println(new String(b));  // byte 배열을 문자열로 변경하여 출력
                input.close();
            }
        }
        ```
        
        - 파일을 읽기 위해서는 FileInputStream 클래스 이용
        - 다만 byte 배열을 이용하여 파일을 읽어야 함
            - 읽어야 하는 정확한 길이를 모를 경우에는 좀 불편한 방법
        - 바이트 배열을 문자열로 변경할 때
            - `new String(바이트배열)`처럼 사용하여 변경
            
    - 파일을 라인단위로 읽을 수 있다면
        
        ```java
        import java.io.BufferedReader;
        import java.io.FileReader;
        import java.io.IOException;
        
        public class Sample {
            public static void main(String[] args) throws IOException {
                BufferedReader br = new BufferedReader(new FileReader("c:/out.txt"));
                while(true) {
                    String line = br.readLine();
                    if (line==null) break;  // 더 이상 읽을 라인이 없을 경우 while 문을 빠져나간다.
                    System.out.println(line);
                }
                br.close();
            }
        }
        ```
        
        - FileInputStream 대신 FileReader와 BufferedReader의 조합 사용
            - 라인단위로 파일을 읽을 수 있음
        - BufferedReader의 readLine 메소드
            - 더이상 읽을 라인이 없을 경우 null 리턴
