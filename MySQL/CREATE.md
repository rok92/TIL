### 데이터 정의어(DDL) => CREATE 문

- CREATE / ALTER / DROP 문

- CREATE문

  - 테이블, 도메인, 뷰, 인덱스, 스키마 구조 정의

  - **CREATE TABLE**

    - 테이블 구성

    - 속성(열)과 속성(열) 사이의 제약 정의

    - 기본키 : PRIMARY KEY

    - 외래키 : FOREIGN KEY

    - 기본형식(테이블생성)

      - CREATE TABLE 테이블명 ()

        ​	열이름 데이터타입 [제약조건]

        ​	PRIMARY KEY(열이름),

        ​	FOREIGN KEY(열이름) REFERENCES 테이블(기본키)

        ​	CONSTRAINTS 명

        );

    - **PRIMARY KEY(기본키) 제약조건**

      - 열에 지정
      - 중복 안됨
      - NULL값 안됨(기본키로 설정하면 NOT NULL 자동으로 붙음)

      ```MYSQL
      create table product(
      	prdNo char(10) not null primary key,
          prdName varchar(30) not null,
          prdPrice int,
          prdCompany varchar(30)
      );
      ```

    - **FOREIGN KEY(외래키) 제약조건**

      - 반드시 기본키가 설정되어 있는 키를 외래키로 사용할 수 있다
      - 출판사(<u>출판사 번호</u>, 출판사 명, 전화,......) 기본키 : <u>출판사 번호</u>
      - 도서(<u>도서번호</u>, 도서명, 가격, 발행일, **출판사 번호**) 기본키 : <u>도서번호</u> / 외래키 : **출판사 번호**

      ```mysql
      create table publisher(			-- 항상 참조되는 테이블 먼저 생성
      	pubNo char(10) not null primary key, 	-- 기본키 설정
          pubName varchar(30) not null
      
      
      create table book(			-- 참조하는 테이블 생성
      	bookNo char(10) not null primary key, 	-- 참조하는 테이블의 기본키 값
          bookName varchar(30) not null,
          bookPrice int default 10000 check(bookPrice > 1000),
          bookDate date,
          pubNo char(10) not null,
          constraint FK_book_publisher foreign key(pubNo) references publisher(pubNo) -- 외래키 설정
      );
      ```

      

    - **테이블 생성시 주의사항**

      - 항상 참조되는 테이블을 먼저 생성 후 참조하는 테이블을 생성해야 한다.

    - **테이블 생성후 입력값 입력시 주의사항**

      - 외래키 값을 입력할 때에는 반드시 참조되는 테이블의 기본키값을 먼저 입력 후 외래키 값을 입력할 때 참조되는 기본키의 값과 동일하기 때문에 오류가 발생하지 않는다.

    - **테이블 삭제시 주의**

      - 반대로 테이블 삭제할 때는 참조하는 테이블 먼저 삭제 후 참조되는 테이블을 삭제해야 한다
      - 참조되는 테이블의 기본값이 참조하는 테이블의 외래키값으로 쓰이고 있기 때문에 먼저 삭제 할 수 없다.

  - **CREATE SCHEMA**

    - 기본 스키마 설정

      (1) Set as a Default Schema

      (2) SQL : sqldb

      ```mysql
      CREATE SCHEMA sqldb DEFAULT CHARACTER SET UTF8;
      CREATE SCHEMA sqldb2 DEFAULT CHARACTER SET UTF8MB4;
      ```

  - **CHAR(10) : 고정길이 문자 / VARCHAR(20) : 가변길이 문자**

  - **자동증가**

    - AUTO_INCREMENT
      - 속성값을 자동으로 증가

    - AUTO_INCREMENT = 100

      - 기본값 100 부터 증가

    - SET

      @@AUTO-INCREMENT_INCREMENT = 3	=> 3씩 증가

  - **자동증가 수정**

    - SET @COUNT = 0;
      - UPDATE board SET boardNo = @COUNT:=@COUNT+1;

  - CREATE DOMAIN

  - CREATE INDEX

  - CREATE VIEW