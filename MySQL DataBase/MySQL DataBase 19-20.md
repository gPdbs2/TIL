# MySQL DataBase

문서 유형: 학습 자료
작성일시: 2022년 8월 17일 오후 9:29
최종 편집일시: 2022년 8월 18일 오후 8:27

<aside>
💡 **MySQL 1회독 진행 중( 18 / 25 강)**

</aside>

# MySQL DataBase 19~20강

## 19강. 데이터 베이스 및 테이블 생성

- **데이터 베이스 만들기**
    - 데이터 베이스 생성은 create database 구문 사용
    - **create database 이름**
    - 생성한 데이터 베이스는 use 문을 이용해 선택
    - utf-8 인코딩 타입의 한글을 저장하려면 다음과 같은 언어 타입 지정
        - **create database 이름**
        - **character set = ‘utf8’**
        - **collate = ‘utf8_general_ci’;**
        
        ```sql
        create database test_db
        character set = ‘utf8’
        collate = ‘utf8_general_ci’;
        
        // DB 사용할 때
        use test_db;
        ```
        

- **테이블 만들기**
    - 데이터 베이스 선택 후 create table 명령문 통해 테이블 생성
        - **create table 이름 (**
        - **컬럼이름 자료형 제약조건, 컬럼이름 자료형 제약조건);**
        
        ```sql
        create table test_table(
        	data1 int,
        	data2 varchar(10)
        	data3 float(10, 2)
        );
        
        desc test_table1;
        select * from test_table1;
        ```
        

- **자료형**
    - [https://dev.mysql.com/doc/refman/5.7/en/data-types.html](https://dev.mysql.com/doc/refman/5.7/en/data-types.html)
    
    ![Untitled](MySQL%20DataBase%208cefd9b53b8842abb14ea34fdf2ebacc/Untitled.png)
    

- 서브 쿼리를 이용한 테이블 생성하기
    - select 문을 통해 가져온 결과를 이용해 테이블 생성 시 사용
        - **create table 테이블 명**
        - **as**
        - **select 문**
        
        ```sql
        // 사용할 DB 변경
        use employees;
        
        select * from departments;
        
        // 테이블 복제
        create table dept1
        as 
        select * from departments;
        
        desc dept1;
        select * from dept1;
        
        // 구조만 복제
        create table dept2
        as 
        select * from departments where 1=0;
        
        desc dept2;
        select * from dept2;
        
        // departments 테이블에서 dept_no 가져온 결과로 dept3 테이블 생성
        create table dept3
        as 
        select dept_no from departments;
        ```
        
- 학습 요약
    - create 문을 이용해 데이터 베이스와 테이블 생성 가능

## 20강. 저장, 수정, 삭제

- **데이터 저장하기**
    - insert 문 활용하면 데이터 저장 가능
    - 이 때, 로우 단위로 저장됨
        - **insert into 테이블명 (컬럼명) values (값)**
        - **insert into 테이블명  values (값)**
    - 컬럼에 저장될 값 지정하지 않을 경우 null 저장
    
    ```sql
    desc test_table1;
    insert into test_table1 (data1, data2, data3) values (100,'문자열1', 11.11);
    select * from test_table1;
    
    insert into test_table1 (data2, data3, data1) values ('문자열2', 22.22, 200);
    select * from test_table1;
    
    insert into test_table1 values (300, '문자열3', 33.33);
    select * from test_table1;
    
    // 데이터 갯수 일치하지 않을 경우 오류 발생
    insert into test_table1 (data1, data2) values (400, '문자열4', 44.44);
    
    // 타입 안 맞는 경우
    insert into test_table1 (data1, data2, data3) values ('문자열5', '문자열6', '문자열7');
    
    // 숫자로 구성된 문자 => 숫자로 변환 되어 들어감 => 정상적으로 작동
    insert into test_table1 (data1, data2, data3) values ('500', '문자열8', '55.55');
    select * from test_table1;
    
    // 서브 쿼리 활용해서 저장
    // 테이블 test_table1 의 구조만 복제해 테이블 test_table2 생성
    create table test_table2;
    as 
    select * from test_table1 where 1=0;
    
    // 구조 복제 확인
    desc test_table2;
    select * from test_table2;
    
    // 서브 쿼리 활용
    insert into test_table2
    select data1, data2, data3 from test_table1;
    
    select * from test_table2;
    
    // 만약 데이터에 컬럼 세팅을 하지 않았을 경우
    // 세팅 하지 않은 값에 null 들어감
    insert into test_table1 (data1, data2) values (600, '문자열9');
    select * from test_table1;
    ```
    

- **데이터 수정하기**
    - update 문을 활용하면 데이터 수정 가능
        - **Update 테이블명 set 컬럼명=값, 컬럼명=값 where 조건식**
        
        ```sql
        // 기존 데이터 확인
        select * from test_table1;
        
        // 데이터 수정
        update test_table1 set data2='새로운문자열', data3=66.66;
        select * from test_table1;
        
        // 데이터 수정 2
        select * from test_table2;
        update test_table2 set data2='새로운문자열', data3=66.66
        where data1=100;
        select * from test_table2;
        ```
        
        - 오류 발생할 경우
            - edit - preference - SQL Editor
                - Safe Updates ~~ 체크 해제
            - 그 후에 다시 재실행

- **데이터 삭제하기**
    - delete 문을 활용하면 데이터 삭제 가능
        - **Delete from 테이블명 where 조건식**
        
        ```sql
        delete from test_table1;
        select * from test_table1;
        
        // 특정 부분만 삭제하고자 할 때
        delete from test_table2 where data1=100;
        select * from test_table2;
        ```
        

- 학습 요약
    - insert 문 → 테이블에 로우 추가
    - Update 문 → 데이터 수정
    - Delete 문 → 로우 삭제