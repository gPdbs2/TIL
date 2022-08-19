# MySQL DataBase

문서 유형: 학습 자료
작성일시: 2022년 8월 19일 오후 9:26
최종 편집일시: 2022년 8월 19일 오후 11:00

<aside>
💡 **MySQL 1회독 진행 중( 22 / 25 강)**

</aside>

# MySQL DataBase 21~22강

## 21강. 트랜젝션 관리

- **트렌젝션**
    - 데이터 베이스에서 데이터 처리의 한 단위
    - 대부분의 데이터 베이스는 데이터를 저장, 수정, 삭제하는 작업을 바로 물리적인 하드디스크에 저장된 데이터에 반영하지 X
        - 이는 개발자의 실수로 잘못된 명령문을 입력했을 경우 다시 원래 상태로 되돌리기 위한 안전 장치
    - 따라서 개발자가 commit이라는 작업을 하기 전까지 입력한 명령문은 메모리에서만 동작하고 물리적인 하드디스크에 반영하지 X
        - commit 작업 발생 시 그 때 하드디스크에 반영
    - 개발자가 데이터에 대한 작업을 하기 위해 입력하는 명령문들의 시작부터 commit까지를 하나의 트렌젝션이라고 부름

- **RollBack**
    - 데이터의 저장, 수정, 삭제 등의 작업을 하고 난 후 원래의 형태로 되돌리는 작업
    - **commit 라는 작업을 하고 난 이후에는 RollBack 작업 해도 원래의 형태로 되돌릴 수 없음**
    - workbench 등의 프로그램에서는 자동으로 commit 작업 발생
        - RollBack 해도 원래 형태로 되돌릴 수 X
        - RollBack 작업 할 수 있게 하려면 설정에서 Auto Commit 해제해야 함
    
    ```sql
    select * from test_table2;
    
    delete from test_table2;
    select * from test_table2;
    
    rollback;
    select * from test_table2;
    ```
    
- **Commit**
    - 하나의 트렌젝션을 물리적인 데이터 베이스에 적용하는 작업
    - 이 작업을 하게 되면 RollBack 해도 원래 형태로 되돌릴 수 X
    - 일반적으로 개발자가 만드는 프로그램들은 자동으로 commit 발생
    
    ```sql
    // rollback 작업
    delete from test_table2;
    select * from test_table2;
    rollback;
    select * from test_table2;
    
    // commit 실행 후 rollback 작업 -> rollback 실행 안 됨
    delete from test_table2;
    commit;
    select * from test_table2;
    rollback;
    select * from test_table2;
    ```
    

- SavePoint
    - RollBack 시 지정된 위치로 복원할 수 있음
    - ㅊ 명령어로 지점을 지정, rollback 명령어로 복원
    
    ```sql
    insert into test_table2 (data1, data2, data3) values (100, '문자열1', 11.11);
    insert into test_table2 (data1, data2, data3) values (200, '문자열2', 22.22);
    insert into test_table2 (data1, data2, data3) values (300, '문자열3', 33.33);
    
    // commit 시 현재까지의 작업 하드디스크에 반영, 새로운 트렌젝션 시작
    // commit 부터 rollback 전까지의 작업이 하나의 트렌젝션
    commit;
    select * from test_table2;
    
    update test_table2 set data2='새로운문자열', data3=44.44 where data1=100;
    savepoint aa;
    select * from test_table2;
    delete from test_table2 where data1=100;
    select * from test_table2;
    rollback to aa;
    select * from test_table2;
    ```
    

- **truncate**
    - 지정된 테이블의 모든 로우 삭제
    - **delete 문과의 차이점**
        - **delete 문** : 데이터베이스에 바로 반영하지 X → **rollback 가능**
        - **truncate 문** : 데이터베이스에 바로 반영 → **rollback 불가능**
    
    ```sql
    // savepoint 예제 이어서
    commit;
    
    select * from test_table2;
    
    delete from test_table2;
    select * from test_table2;
    rollback;
    select * from test_table2;
    
    // 실행 시 데이터 복원되지 않음 확인
    truncate test_table2;
    rollback;
    select * from test_table2;
    ```
    

- **학습 요약**
    - **rollback** : 데이터 복원
    - **commit** : 데이터베이스에 반영
    - **savepoint** : 복원 지점 설정
    - **truncate** : 테이블의 모든 로우 삭제, 복원 불가능

## 22강. 테이블 변경하기

- **테이블 변경하기**
    - 존재하는 테이블의 이름, 속성 등을 변경할 수 있음
    - rename table old_name to new_name
    - alter table table_name modify coulmn type (제약조건)
    - alter table table_name change old_coulmn new_coulmn type
    - alter table table_name add new_coulmn type
    - alter table table_name drop coulmn_name
    - drop table 테이블명
    
    ```sql
    show tables;
    
    // 테이블명 변경
    rename table test_table1 to test_table3;
    show tables;
    
    // 컬럼명, 타입 변경 1
    desc test_table3;
    alter table test_table3 modify data1 int(100);
    desc test_table3;
    
    // 컬럼명, 타입 변경 2
    alter table test_table3 change data1 data10 int(200);
    desc test_table3;
    
    // 컬럼명만 바꾸겠다
    alter table test_table3 change data10 data5 int(200);
    desc test_table3;
    
    // 컬럼 추가
    alter table test_table3 add data4 int(20);
    desc test_table3;
    
    // 컬럼 삭제
    // 삭제 시 주의할 점 : 안에 들어 있는 데이터까지 다 날아간다
    alter table test_table3 drop data4;
    desc test_table3;
    
    // 테이블 삭제
    show tables;
    drop table test_table3;
    show tables;
    ```
    

- **학습 요약**
    - **rename** : 테이블 이름 변경
    - **alter** : 테이블의 컬럼을 변경, 추가, 삭제
    - **drop table** : 테이블 삭제