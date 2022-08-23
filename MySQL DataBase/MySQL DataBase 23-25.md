# MySQL DataBase

문서 유형: 학습 자료
작성일시: 2022년 8월 19일 오후 11:17
최종 편집일시: 2022년 8월 20일 오후 7:00

<aside>
💡 **MySQL 1회독 完( 25 / 25 강)**

</aside>

# MySQL DataBase 23~25강

## 23강. 제약조건

- **제약조건**
    - 컬럼에 저장될 데이터의 조건을 설정하는 것
    - 제약 조건을 설정하면 조건에 위배되는 데이터는 저장할 수 X
        - 데이터의 무결성 보장
    - 데이터베이스 내 테이블들은 여러 개발자가 사용 가능
        - 테이블 생성 시 제약 조건 설정하는 것은 매우 중요
    - **primary key**
        - 컬럼에 **중복된 데이터 저장 X, null 값 허용하지 X**
        - 주로 각 로우르 구분하기 위한 유일한 값을 저장하는 컬럼에 사용
        - 기본키라고도 부름
    - **foreign key**
        - 특정 테이블의 primary key 컬럼에 저장되어 있는 값만 저장
        - 흔히 참조키, 외래키라고 부르며 지정된 테이블의 기본키 컬럼을 참조, 참조하는 기본키 컬럼에 저장되어 있는 값만 저장
        - **null 값 허용**
    - **not null**
        - 컬럼에 **null 값을 저장할 수 X**
        - 쿼리문을 통해 **반드시 값이 지정되어야 함**
    - **unique**
        - 컬럼에 **중복된 값 저장 가능**
        - **null 값 허용**
    - **check**
        - 값의 범위나 종류를 지정, 조건에 맞는 값만 저장할 수 있도록 함
        - check의 제약 조건은 MySQL에서 지원하지 않음
    - **default**
        - null이 들어올 경우 기본 설정되는 값을 지정
        - default를 설정할 경우 **컬럼에 null 값 저장할 수 X**
    
    ```sql
    create table tast_table10(
    	data1 int not null
    );
    
    insert into test_table10 (data1) values (1);
    insert into test_table10 (data1) values (2);
    insert into test_table10 (data1) values (3);
    
    select * from test_table10;
    
    // 중복된 값 넣어보자.
    // 결과 : 1 2 3 1
    insert into test_table10 (data1) values (1);
    select * from test_table10;
    
    // null 값 넣으면?
    // 오류 발생 -> cannot be bull (null 값 허용하지 않는다)
    insert into test_table10 (data1) values (null);
    select * from test_table10;
    
    // primary key
    create table tast_table20(
    	data1 int,
    	data2 int not null,
    	constraint pk1 primary key(data1)
    );
    
    insert into test_table20 (data1, data2) values (10, 100);
    insert into test_table20 (data1, data2) values (20, 200);
    insert into test_table20 (data1, data2) values (30, 300);
    select * from test_table20;
    
    // data1에 중복된 값 넣어보자.
    // 결과 : 오류 발생 -> primary key인 data1 컬럼에 중복된 10이라는 값을 넣었다.
    insert into test_table20 (data1, data2) values (10, 100);
    // null 값 넣으면?
    // 결과 : 오류 발생 -> cannot be null
    insert into test_table20 (data1, data2) values (null, 100);
    // 오류 발생 -> doesn't have a default value
    // 반드시 null 아닌 값 직접 세팅해줘야 함
    insert into test_table20 (data2) values (100);
    
    // foreign key
    create table tast_table30(
    	data1 int,
    	data2 int,
    	constraint pk2 primary key(data1)
    	constraint fk2 foreign key(data2) references tast_table20(data1)
    );
    
    select * from test_table20;
    insert into test_table30 (data1, data2) values (1, 10);
    insert into test_table30 (data1, data2) values (2, 20);
    insert into test_table30 (data1, data2) values (3, 30);
    select * from test_table30;
    
    // test_table20의 data1에 존재하지 않는 값을 넣으면?
    // 오류 발생 -> cannot add or update a child now : a foreign key ~
    insert into test_table30 (data1, data2) values (4, 40);
    
    // null 값 넣기, 값 지정 X -> null 값 잘 들어감
    insert into test_table30 (data1, data2) values (5, null);
    insert into test_table30 (data1) values (6);
    select * from test_table30;
    
    // unique
    create table tast_table40(
    	data1 int,
    	data2 int noit null,
    	constraint uk1 unique(data1),
    	constraint uk2 unique(data2)
    );
    
    insert into test_table40 (data1, data2) values (1, 10);
    insert into test_table40 (data1, data2) values (2, 20);
    select * from test_table40;
    
    // 중복된 값 집어 넣으면?
    // 오류 발생 -> 중복된 값 들어왔다는 메시지
    insert into test_table40 (data1, data2) values (1, 30);
    insert into test_table40 (data1, data2) values (3, 10);
    
    // null 값 넣으면?
    // null 값 중복해서 잘 들어감 
    // 단, null 아닌 값은 중복해서 들어갈 수 없다 -> not null
    insert into test_table40 (data1, data2) values (null, 40);
    insert into test_table40 (data1, data2) values (null, 50);
    
    // null 값 오류 발생 -> not null
    insert into test_table40 (data1, data2) values (10, null);
    
    // check
    create table tast_table50(
    	data1 int not null,
    	data2 int not null,
    	constraint chk1 check (data1 > 10),
    	// data2에는 10, 20, 30 중에 하나만 넣겠다
    	constraint chk2 check (data2 in(10, 20, 30))
    );
    
    insert into test_table50 (data1, data2) values (20, 30);
    select * from test_table50;
    
    // 조건 위배 시 -> 그래도 값 정상적으로 들어감
    insert into test_table50 (data1, data2) values (1, 100);
    select * from test_table50;
    
    // default
    create table tast_table50(
    	data1 int not null default 1, 
    	data2 int not null default 10,
    );
    
    insert into test_table60 (data1, data2) values (100, 200);
    select * from test_table60;
    
    // null 넣으면?
    // 결과 : 오류 발생 -> 진짜 null 집어 넣으려고 함 
    insert into test_table60 (data1, data2) values (null, null);
    select * from test_table60;
    
    // 컬럼 값 생략하고 넣으면?
    // 결과 : 설정해놓은 default 값 출력
    insert into test_table60 (data1) values (1000);
    insert into test_table60 (data2) values (2000);
    select * from test_table60;
    ```
    

- **학습 요약**
    - 제약 조건을 사용하면 데이터의 무결성 보장
    - **primary key** : 중복, null 허용 X
    - **foreign key** : 지정된 primary key 값만 저장, null 허용
    - **not null** : 컬럼에 null 허용 X
    - **unique** : null 허용, 중복 값 허용 X
    - **default :** 기본값 설정

## 24강. 시퀀스

- **시퀀스**
    - 로우를 추가할 떄 자동으로 증가하는 값이 저장되는 것
    - **데이터베이스마다 사용하는 방법 다름**
        - **반드시 파악할 필요 있음**
    - MySQL은 auto_increment 키워드 설정해주면 됨
    - 데이터를 insert 할 때 auto_increment 설정한 컬럼 제외
    
    ```sql
    create table tast_table100(
    	data1 int auto_increment,
    	data2 int not null,
    	data3 int not null,
    	constraint pk1 primary key(data1)
    );
    
    insert into test_table100 (data2, data3) values (100, 200);
    insert into test_table100 (data2, data3) values (101, 201);
    insert into test_table100 (data2, data3) values (102, 202);
    select * from test_table100;
    ```
    
- **limit**
    - select 해서 가져온 로우에서 원하는 범위의 로우만 가지고 올 때 사용
    - 게시판 등에서 사용하는 페이징 기법 구현할 때 사용
    - **데이터 베이스마다 구현하는 방법 다름**
        - **반드시 파악할 필요 있음**
    - **select 문 limit 시작인덱스, 갯수**
    
    ```sql
    use employees;
    
    select * from employees order by emp_no;
    select * from employees order by emp_no limit 0, 10;
    select * from employees order by emp_no limit 10, 10;
    ```
    
- **학습 요약**
    - **시퀀스** : 자동으로 증가되어 저장되는 컬럼 만들 수 있음
    - **limit** : 정해진 범위에 해당하는 로우 가져올 수 있음

## 25강. 뷰

- **뷰**
    - **뷰는 가상의 테이블**을 의미
    - 2개 이상의 테이블을 join 하거나 서브쿼리를 사용하는 select 문은 쿼리문이 복잡해지게 되는데 이를 매번 사용 시 개발자의 불편함이 따르게 됨
    - 이 때 join이나 서브쿼리를 사용해 얻어진 결과를 뷰로 만들어 놓으면 개발자는 뷰를 통해 결과를 얻어올 수 있음
    - 사실 뷰는 select 문 통해 얻어진 결과를 가지고 있는 것이 아니라 **select 문 자체를 가지고 있어 뷰를 select 하면 이전에 사용한 쿼리문이 실행되어 결과 가져오게 됨**
    
    ```sql
    create table tast_table1000(
    	data1 int,
    	data2 int not null,
    	constraint pk1 primary key (data1)
    );
    
    create table tast_table2000(
    	data1 int not null,
    	data3 int not null,
    	constraint fk1 foreign key(data1) references tast_table1000(data1)
    );
    
    insert into test_table1000 (data1, data2) values (1, 10);
    insert into test_table1000 (data1, data2) values (2, 20);
    insert into test_table1000 (data1, data2) values (3, 30);
    
    select * from test_table1000;
    
    insert into test_table2000 (data1, data2) values (1, 100);
    insert into test_table2000 (data1, data2) values (2, 200);
    insert into test_table2000 (data1, data2) values (3, 300);
    
    select * from test_table2000;
    ```
    
    - **Create view 뷰이름 as select 쿼리문**
    - **Drop view 뷰이름**
    
    ```sql
    // 두 table join
    select a1.data1, a1.data2, a2.data3
    from test_table1000 a1, test_table2000 a2
    where a1.data1 = a2.data1;
    
    // view 생성
    create view test_view1
    as
    select a1.data1, a1.data2, a2.data3
    from test_table1000 a1, test_table2000 a2
    where a1.data1 = a2.data1;
    // view 조회
    select * from test_view1;
    
    insert into test_table1000 (data1, data2) values (4, 40);
    insert into test_table2000 (data1, data2) values (4, 400);
    
    select * from test_view1;
    
    // view 삭제
    drop view test_view1;
    
    select * from test_view1;
    ```
    
- **학습 요약**
    - 복잡한 select 쿼리문을 이용해 뷰를 만들면 이후부터는 편하게 데이터 조회 가능