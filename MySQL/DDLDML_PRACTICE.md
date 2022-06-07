### DDL/DML PRACTICE

1. 고객 테이블(customer)생성(CREATE)

   ```mysql
   -- 1. 고객 테이블 생성
   create table customer(
   	cusNo char(20) primary key,
       cusName varchar(30),
       cusTel varchar(20)
   );
   ```

2. 고객 테이블의 전화번호 열을 not null로 변경

   ```mysql
   -- 2. 고객 테이블의 전화번호 열을 not null로 변경
   alter table customer modify cusTel varchar(20) not null;
   ```

3. 고객 테이블에 '성별', '나이' 열 추가

   ```mysql
   -- 3. 고객 테이블에 '성별', '나이' 열 추가
   alter table customer add(cusGender varchar(10), cusAge int);
   ```

4. 고객 테이블에 데이터 삽입 3개

   ```mysql
   insert into customer
   		values('1', '홍길동', '02-111-1111', '남', 30),
   			  ('2', '성춘향', '02-222-2222', '여', 20),
   			  ('3', '이몽룡', '02-333-3333', '남', 25);
               
   ```

5. 고객명이 '홍길동'인 고객의 전화번호 값 수정

   ```mysql
   -- 5. 고객명이 '홍길동'인 고객의 전화번호 값 수정
   update customer set  cusTel = '010-1111-1111' where cusNo = '1';
   ```

6. 나이가 20살 미만인 고객 삭제

   ```mysql
   insert into customer
   	   values('4', '이순신', '02-444-4444', '남', 11);
   	   
   elete from customer where cusAge < 20;
   ```

   