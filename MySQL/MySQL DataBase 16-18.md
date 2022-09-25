# MySQL DataBase

문서 유형: 학습 자료
작성일시: 2022년 8월 16일 오후 6:40
최종 편집일시: 2022년 8월 17일 오후 11:10

<aside>
💡 **MySQL 1회독 진행 중( 18 / 25 강)**

</aside>

# MySQL DataBase 16~18강

## 16강. 조인

- 데이터 중복의 최소화
    - 데이터 베이스에서 가장 중요한 부분 
    → **데이터를 가져오는 데 걸리는 시간의 최소화**
    - 데이터 베이스는 저장된 데이터의 총량이 크면 클수록 
    데이터를 가져오는 데 시간이 오래 걸리게 됨
    - 이 때문에 **데이터의 중복을 최소화**하여 **데이터를 빠르게 가져올 수 있도록 테이블을 구성**하게 됨
    - 이 과정에서 테이블은 2개 이상으로 분리될 수 밖에 없음
    
    - ex) 고객의 구매 정보를 저장하는 테이블이 있고, 이 테이블은
        - 고객 이름, 고객 전화번호, 상품 이름, 상품 가격으로 구성되어 있다 가정
        - 고객 한 명이 여러 상품을 구매할 수도 있고 같은 상품을 여러 사람이 구매할 수도 있기 때문에 데이터는 상당히 중복될 수 밖에 없음
            
            ![Untitled](MySQL%20DataBase%20423c69412b2e41aca940febe1c6d5e1a/Untitled.png)
            
        
        - 앞서 살펴본 테이블을 다음과 같이 나눠 데이터의 중복 최소화 가능
            
            ![Untitled](MySQL%20DataBase%20423c69412b2e41aca940febe1c6d5e1a/Untitled%201.png)
            

- **Join**
    - **데이터의 중복을 최소화** 하기 위해 테이블을 분리 시킨 후 데이터를 가져올 때 **여러 테이블을 하나의 결과로 가져와야 할 때** 사용
    - 여러 테이블의 데이터를 한 번에 가져올 수 있음
    - 여러 테이블을 join 할 때는 테이블의 이름을 , 로 구분하여 작성해주고 각 테이블의 컬럼명을 기술해주면 원하는 데이터를 가져올 수 있음
    
    - **Select 컬럼명 1, 컬럼명 2, 컬럼명 3
    From 테이블 1, 테이블 2**
    
    - 각 사원들의 사원 번호, 근무 부서 번호, 근무 부서 이름을 가져온다.
        - 사원 번호를 기준으로 오름차순 정렬
        
        ```sql
        select dept_emp.emp_no, dept_emp.dept_no, departments.dept_name
        from departments, dept_emp;
        
        ---------------------------------------------------------------
        
        select a2.emp_no, a2.dept_no, a1.dept_name
        from departments a1, dept_emp a2
        order by a2.dept_emp;
        ```
        

- **기본 join**
    - **join 문을 사용하게 되면 n:n 관계로 가져오게 되기 때문에 잘못된 데이터가 구성될 수 있음**
    - 이를 위해 join 조건문을 작성해야 함
        - 위의 예제 수정하면
        
        ```sql
        select a2.emp_no, a2.dept_no, a1.dept_name
        from departments a1, dept_emp a2
        where a1.dept_no = a2.dept_no
        order by a2.dept_emp;
        ```
        
    
    - 각 사원들의 사원 번호, first_name, 근무 부서 번호를 가져온다
        
        ```sql
        select a1.emp_no, a1.first_name, a2.dept_no
        from employees a1, dept_emp a2
        where a1.emp_no = a2.emp_no;
        ```
        
    
    - 각 사원들의 사원 번호, first_name, 현재 받고 있는 급여액을 가져온다
        
        ```sql
        select a1.emp_no, a1.first_name, a2.salary
        from employees a1, salaries a2
        where a1.emp_no = a2.emp_no
              and a2.to_date='9999-01-01';
        ```
        
    
    - 각 사원들의 사원 번호, first_name, 근무 부서 이름을 가져온다
        
        ```sql
        select a1.emp_no, a1.first_name, a3.dept_name
        from employees a1, dept_emp a2, department a3
        where a1.emp_no = a2.emp_no and a2.dept_no = a3.dept_no;
        ```
        
    
- **학습 요약**
    - 여러 테이블에서 데이터를 동시에 가져올 때 join 문을 사용
    - Join 문은 N:N 의 관계로 가져오기 때문에 잘못된 데이터를 포함함
        - 이를 제거하기 위해 조건문을 설정해야 함

## 17강. 서브쿼리

- **서브 쿼리**
    - 쿼리문 안에 쿼리문이 있는 것
    - 조건문 등을 만들 때 **값을 직접 지정하지 못하고 쿼리문을 통해 구해와야 할 경우 서브 쿼리를 통해 값을 구해**와 조건문 완성
    
    - 현재 받는 급여의 평균보다 많이 받는 사원들의 사원 번호, 급여액을 가져온다
        
        ```sql
        select avg(salary) from salaries and to_date = '9999-01-01'
        
        select emp_no, salary
        from salaries
        where salary > (select avg(salary) from salaries and to_date = '9999-01-01')
              and to_date = '9999-01-01';
        ```
        
    
    - d001 부서에서 근무하고 있는 사원들의 사원 번호와 first_name 을 가져온다
        
        ```sql
        select a1.emp_no, a2.first_name
        from employees a1, dept_emp a2
        where a1.emp_no = a2.emp_no and a2.dept_no = 'd001';
        
        // 서브 쿼리 이용했을 때
        select emp_no from dept_emp where dept_no='d001';
        
        select a1.emp_no, a2.first_name
        from employees
        where emp_no in(select emp_no from dept_emp where dept_no='d001';);
        ```
        
    
    - 1960년 이후에 태어난 사원들이 근무하고 있는 사원들의 사원 번호, 근무 부서 번호를 가져온다
        
        ```sql
        select emp_no from employees where birthAdate >= '1960-01-01';
        
        select emp_no, dept_no
        from dept_emp
        where emp_no in(select emp_no from employees where birthAdate >= '1960-01-01');
        ```
        
    
    - 쿼리문 완성을 위해 필요한 값을 정할 수 없다면 서브 쿼리 이용해 값을 구해와 적용

## 18강. set

- **set**
    - 두 select 문을 통해 얻어 온 결과를 **집합 연산을 통해 하나의 결과로 만드는 것**
    - 합집합, 교집합, 차집합 등의 집합 연산 가능
    - 집합 연산을 하기 위해서는 **두 select 문을 통해 가져오는 컬럼 같아야 함**
    
    - **합집합**
        - **두 select 문의 결과를 모두 포함하는 최종 결과**를 반환
        - **UNION** : **중복**되는 데이터를 **하나만** 가져온다
        
        ```sql
        select emp_no from titles where title = 'Senior Staff'
        union
        select emp_no from titles where title = 'Staff';
        ```
        
        - **UNION ALL** : **중복**되는 데이터도 **모두** 가져온다
        
        ```sql
        select emp_no from titles where title = 'Senior Staff'
        union all
        select emp_no from titles where title = 'Staff';
        ```
        
    
    - **교집합**
        - **두 select 문의 결과 중 중복되는 부분만** 가져온다
        - **교집합은 join 문** 사용
        - MySQL의 경우 교집합을 구하는 연산자 따로 없음
        
        ```sql
        select a1.emp_no
        from titles a1, titles a2
        where a1.emp_no = a2.emp_no and a1.title = 'Senior Staff' and
              a2.title = 'Staff';
        ```
        
    
    - **차집합**
        - 두 select 문에서 중복되는 부분을 제거하고 첫 번째 select 문 결과만 반환
        - 차집합은 서브 쿼리 이용
        
        ```sql
        select emp_no
        from titles
        where title = 'Staff' and 
              emp_no not in(select emp_no from titles where title = 'Senior Staff');
        ```
        

- 학습 요약
    - 집합 연산을 통하면 합집합, 차집합, 교집합 연산 가능