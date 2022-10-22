### SQL 기본

<hr>
#### 1. 관계형 DB 개요

- **DB : 데이터를 일정한 형태로 저장해 놓은 것, DBMS를 이용하여 효율적인 데이터 관리와 데이터 손상 복구 가능**
  - 종류
    - 계층형 DB : 트리 형태의 자료 구조에 데이터 저장, 1:N 관계 표현
    - 네트워크형 DB : 오너와 멤버 형태로 데이터 저장, M:N 관계 표현
    - 관계형 DB : 릴레이션에 데이터 저장, 집합 연산과 관계 연산 가능
- **관계형 DB(RDB; Relational Database) : 1) 정규화를 통해 이상현상 및 중복 데이터 제거** 2) 동시성 관리와 병행 제어를 통해 데이터 동시 조작 가능
  - 집합연산
    - 합집합(Union)
    - 차집합(Difference)
    - 교집합(Intersection)
    - 곱집합(Cartesian Product) : 각 릴레이션에 존재하는 모든 데이터를 조합
  - 관계연산
    - 선택 연산(Selection) : 조건에 맞는 행(튜플) 조회
    - 투영 연산(Projection) : 조건에 맞는 칼럽(속성) 조회
    - 결합 연산(Join) : 공통 속성을 사용하여 새로운 릴레이션 생성
    - 나누기 연산(Division) : 공통 요소를 추출하고 분모 릴레이션의 속성을 삭제한 후 중복된 행 제거ㅓ
- **SQL(Structured Query Language) : RDB에서 사용하는 언어, 데이터 조회 및 신규 데이터 입력/수정/삭제 기능 제공**
  - 종류
    - DML(Data Manipulation Language) : 데이터 조작어
      - SELECT : 데이터 조회 명령어
      - INSERT, DELETE, UPDATE : 데이터 변형 명령어
    - DDL(Data Definition Language) : 데이터 정의어, 데이터 구조 관련 명령어
      - CREATE, ALTER, DROP
    - DCL(Date Control Language) : 데이터 제어어, DB 접근 권한 부여 및 회수 명령어
      - GRANT, REVOKE
    - TCL(Transaction Control Language) : 트랜잭션 제어어, DML로 저작한 결과를 논리적인 작업단위 별로 제어
      - COMMIT, ROLLBACK, SAVEPOINT
- **테이블(Table) : RDB의 기본 단위, 데이터를 저장하는 객체, 칼럼과 행의 2차원 구조**
