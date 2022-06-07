### DML(데이터 조작어) 1

> INSERT / UPDATE / DELETE

- **INSERT 문**

  - 테이블에 새로운 행을 삽입하는 명령어

  - 기본 형식

    - INSERT INTO 테이블명(열이름 리스트) VALUES(값리스트);
    - 모든 열에 값 저장
    - EX>
      - INSERT INTO student(stdNo, stdName, stdYear, dptNo) VALUES('2022001', '홍길동', 4, '1');

  - **INSERT문 연습**

    - INSERT 문을 사용하여 학과 / 학생 테이블에 각 3개씩 데이터 입력

      ```mysql
      -- 학과 테이블에 데이터 입력
      insert into department
      		values('1', '컴퓨터 학과'), ('2', '알고리즘 학과'), ('3', '웹프로그래밍 학과');
      ```

      ```MYSQL
      -- 학생 테이블에 데이터 입력
      insert into  student
      	values('1', '홍길동', 1, '서울시 동작구', '1999-01-01', '1'),
      		('2', '이몽룡', 3, '서울시 강남구', '1993-05-01', '1'),
              ('3', '성춘향', 2, '서울시 종로구', '1996-07-01', '1');
      ```

      

- **UPDATE 문**

  - 특정 열의 값을 수정하는 명령어

  - 조건에 맞는 행을 찾아서 열의 값 수정

  - 기본 형식

    - UPDATE 테이블명 SET 열 = 값 WHERE 조건;
    - EX>
      - UPDATE product SET prdName = 'UHD TV' WHERE prdNo = '5';

  - **UPDATE문 연습**

    ```MYSQL
    -- 상품 번호가 5인 행의 상품명을 'UHD TV'로 수정
    update product set prdName = 'UHD TV' where prdNo = '5';
    select * from product;
    ```

- DELETE 문

  - 테이블에 있는 기존 행을 삭제하는 명령어

  - 기본형식

    - DELETE FROM 테이블명 WHERE 조건;
    - 테이블의 모든 행 삭제
      - DELETE FROM 테이블명;
    - EX>
      - DELETE FROM product WHERE prdName = '그늘막 텐트';
      - DELETE FROM product;

    ```mysql
    -- 그늘막 텐트가 있는 행 삭제
    delete from product where prdName = '그늘막 텐트';
    -- 테이블 모든 행 삭제
    delete from product;
    
    ```

  