### ALTER문

- 테이블에 대한 정의 변경

- 새로운 열 추가, 특정 열의 디폴트 값 변경, 특정 열 삭제 등 수행

- 기본 형식

  - ALTER TABLE

    - **ADD : 열추가**

      ```mysql
      alter table student add stuTel varchar(13);
      ```

    - **RENAME COLUMN : 열 이름 변경**

      ```mysql
      alter table student rename column stuTel to stuHP;
      ```

    - **MODIFY : 열의 데이터 형식 변경**

      ```mysql
      alter table student modify stuName varchar(20) null;
      ```

    - **CHANGE : 열의 이름과 데이터 형식변경**

      ```mysql
      alter table student change stuAddress stuAddress1 varchar(50);
      ```

    - **DROP : 여러 개의 열 삭제**

      ```mysql
      alter table student drop stuAge,
      					drop stuAddress,
                          drop stuAddress2;
      ```

    - **DROP COLUMN : 열 삭제**

      ```mysql
      alter table student drop column  stuHP;
      ```

    - **DROP CONSTRAINT : 제약 조건 삭제**

      - 기본키 / 외래키 삭제
        - 기본키 / 외래키 추가
            - on delete cascade
              - 기준 테이블(기본키를 갖고 있는 테이블)의 데이터가 삭제되었을 때 이 값을 사용하고 있는 테이브르이 외래키 데이터도 자동으로 삭제되도록 설정
            - check 제약조건 추가 / 삭제
            - default 제약조건 추가 / 삭제

  - **기본키 / 외래키 삭제**

    - 기본키 삭제전에 먼저 외래키 제약조건을 삭제하고 삭제 해야함.

    - (1) 외래키 삭제 

      ```MYSQL
      alter table student
      	drop constraint FK_department_student;
      ```

    - (2) 기본키 삭제

      ```MYSQL
      alter table department drop primary key;
      ```

  - **기본키 제약조건 추가**

    ```MYSQL
    alter table department 
    	add constraint PK_department_depCode
        primary key(depCode);
        
    -- 또는
    
    alter table department 
    	add 
        primary key(depCode);
    ```

  - **테이블에 설정된 제약조건 확인**

    ```MYSQL
    select * from information_schema.table_constraints
    where table_schema = "sqldb" and table_name = "department";
    ```

    