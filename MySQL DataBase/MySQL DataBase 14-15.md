# MySQL DataBase

문서 유형: 학습 자료
작성일시: 2022년 8월 14일 오후 10:06
최종 편집일시: 2022년 8월 16일 오후 7:21

<aside>
💡 **MySQL 1회독 진행 중( 15 / 25 강)**

</aside>

# MySQL DataBase 14~15강

## 14강. 그룹 함수

- **그룹 함수**
    - 조건에 맞는 로우의 컬럼에 대해 집계 값 가져오는 함수
    - **COUNT(컬럼명)** : 가져온 로우 개수 반환
    - **SUM(컬럼명)** : 가져온 해당 로우 컬럼에 저장된 값의 총합
    - **AVG(컬럼명)** : 가져온 해당 로우 컬럼에 저장된 값의 평균
    - **MAX(컬럼명)** : 가져온 해당 로우 컬럼에 저장된 값 중 최댓값
    - **MIN(컬럼명)** : 가져온 해당 로우 컬럼에 저장된 값 중 최솟값
    
    - 사원의 수
        
        ```sql
        select count (*) from employees;
        ```
        
    
    - 남자 사원의 수
        
        ```sql
        select count (*)
        from employees
        where gender='M';
        ```
        
    
    - 현재 d005 부서에 근무하고 있는 사원들의 수
    to_date 컬럼이 9999-01-01인 사원들이 현재 근무하고 있는 사원이다.
        
        ```sql
        select count (*)
        from dept_emp
        where dept_no='d005' and to_date='9999-01-01';
        ```
        
    
    - 현재 받고 있는 급여의 총합
        
        ```sql
        select sum(salary)
        from salaries
        where to_date='9999-01-01';
        ```
        
    
    - 현재 받고 있는 급여의 평균
        
        ```sql
        select avg(salary)
        from salaries
        where to_date='9999-01-01';
        ```
        
    
    - 현재 받고 있는 급여의 최대 급여액
        
        ```sql
        select max(salary)
        from salaries
        where to_date='9999-01-01';
        ```
        
    
    - 현재 받고 있는 급여의 최저 급여액
        
        ```sql
        select min(salary)
        from salaries
        where to_date='9999-01-01';
        ```
        
    
    - 그룹 함수를 구하면
    → 로우의 수, 총합, 평균, 최대, 최소 값 구할 수 있음
    

## 15강. group by, having

- 앞서 살펴본 그룹 함수
    - 로우의 수, 총합, 평균, 최대, 최저 값 가져올 수 있음
    
- 앞서 살펴본 예제들
    - select 문을 통해 가져온 모든 로우를 하나의 그룹으로 묶고,
    그 안에서 로우의 수, 총합, 평균, 최대, 최저 값 구하게 됨
    
- **Group by**
    - select 문을 통해 가져온 모든 로우를 **개발자가 정한 기준에 따라
    그룹으로 나눌 수 있음**
    - 그룹으로 나눈 후 그룹 함수 사용하면 **각 그룹 내에서 
    로우의 수, 총합, 평균, 최대, 최저 값 구할 수 있음**
    
    - 사원의 수를 성별로 가져온다
        
        ```sql
        select gender, count(*) from employees;
        group by gender;
        ```
        
    
    - 각 부서에 근무하고 있는 사원들의 수를 가져온다
        
        ```sql
        select dept_no, count(*)
        from dept_emp
        where to_date='9999-01-01'
        group by dept_no;
        ```
        
    
    - 각 부서 별 과거의 매니저의 수를 구한다
        
        ```sql
        select dept_no, count(*)
        from dept_manager
        where to_date <> '9999-01-01'
        group by dept_no; 
        ```
        
    
    - 급여 수령 시작일별 급여 총합을 구한다
        
        ```sql
        select from_date, sum(salary)
        from salaries
        group by from_date;
        ```
        
    
    - 급여 수령 시작일별 급여 평균을 구한다
        
        ```sql
        select from_date, avg(salary)
        from salaries
        group by from_date;
        ```
        
    
    - 급여 수령 시작일별 급여 최고액을 구한다
        
        ```sql
        select from_date, max(salary)
        from salaries
        group by from_date;
        ```
        
    
    - 급여 수령 시작일별 급여 최저액을 구한다
        
        ```sql
        select from_date, min(salary)
        from salaries
        group by from_date;
        ```
        
    
- **Having**
    - Group by 절을 이용, 개발자가 정한 기준으로 그룹을 나눈 후
    ****having 절로 만든 **조건에 맞는 그룹의 데이터만 가져올 수 있음**
    
    - 10만 명 이상이 사용하고 있는 직함의 이름과 직원의 수를 갖고 온다
        
        ```sql
        select title, count(*)
        from titles
        group by title
        having count(*) >= 100000;
        ```
        
    
    - 5만 명 이상 근무하고 있는 부서의 부서 번호와 부서 소속 사원의 수를
    갖고 온다
        
        ```sql
        select dept_no, count(*)
        from dept_emp
        group by dept_no
        having count(*) >= 50000;
        ```
        
    
- **Group by 절을 이용**
    
    → 데이터를 그룹별로 나눠 가져 올 수 있음
    
- **Having 절을 이용**
    
    → 원하는 그룹의 데이터만 가져올 수 있음