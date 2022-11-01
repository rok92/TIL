### SQL 활용

<hr>

#### 1. JOIN(조인)

- 조인 : 여러 테이블을 연결 또는 결합하여 데이터를 출력하는 것, 일반적으로 PK나 FK의 연관성에 의해 성립

- 등가 조인 : 두 테이블의 칼럼 값이 정확히 일치하는 경우, 대부분 PK와 FK 관계를 기반으로 함

  **SQL >> SELECT 칼럼s FROM 테이블1 A, 테이블2 B WHERE A.칼럼명 = B.칼럼명;**

  - SELECT 대상 칼럼이 두 테이블 모두에 있는 경우 앨리어스(AS)를 지정해야 함(양쪽 앨리어스 모두 무관)

- 비등가 조인 : 두 테이블의 칼럼 값이 정확하게 일치하지 않는 경우, 부등화나 BETWEEM연산자를 통해 조인

#### 2. 표준조인

- SQL에서의 연산

  - 집합연산

    |      UNION       |                  UNION                  |                  합집합                   |
    | :--------------: | :-------------------------------------: | :---------------------------------------: |
    | **INTERSECTION** |              **INTERSECT**              |                **교집합**                 |
    |  **DIFFERENCE**  | **MINUS(오라클)<BR>EXCEPT(SQL Server)** |                **차집합**                 |
    |   **PRODUCT**    |             **CROSS JOIN**              | **곱집합(생길 수 있는 모든 데이터 조합)** |

  - 관계연산

    |   SELECT    |    WHERE절    |                     조건에 맞는 행 조회                      |
    | :---------: | :-----------: | :----------------------------------------------------------: |
    | **PROJECT** | **SELECT절**  |                  **조건에 맞는 칼럼 조회**                   |
    |  **JOIN**   | **여러 JOIN** |                                                              |
    | **DIVIDE**  |   **없음**    | **공통요소를 추출하고 분모 릴레이션의 속성을 삭제한 후 중복된 행 제거** |

- ANSI/ISO SQL의 조인형태 : INNER JOIN, NATURAL JOIN, CROSS JOIN, OUTER JOIN

- **NATURAL JOIN** : 같은 이름을 가진 칼럼 전체에 대한 등가 조인, USING 조건절이나 ON 조건절 사용 불가, 같은 데이터 유형 칼러만 조인 가능, 앨리어스나 테이블명 사용 불가

  **SQL >> SELECT 칼럼s FROM 테이블1 NATURAL JOIN 테이블2;**

- **INNER JOIN** : 행에 동일한 값이 있는 칼럼 조인, JOIN의 디폴트 옵션, USING 조건절이나 ON 조건절 필수, CROSS JOIN이나 OUTER JOIN과 동시 사용 불가, 두 테이블에 동일 이름 칼럼이 있을 경우 SELECT절에 앨리어스 필수

  **SQL >> SELECT 칼럼s FROM 테이블1 A INNER JOIN 테이블2 B ON A.칼럼 = B.칼럼; (ANSI/ISO 표준)**

  **SQL >> SELECT 칼럼s FROM 테이블1 A, 테이블2 B WHERE A.칼럼 = B.칼럼;**

  - **USING 조건절** : 같은 이름을 가진 칼럼중 증가 조인 대상 칼럼 선택, SQL Server에서는 지원하지 않음, 조건절에 앨리어스나 테이블명 불가

    **SQL >> SELECT 칼럼s FROM 테이블1 A JOIN 테이블2 B USING(칼럼명);**

  - ON 조건절 : 다른 이름을 가진 칼럼 간 조인 가능(앨리어스나 테이블명 필수), 괄호는 의무사항 아님

    **SQL >> SELECT 칼럼s FROM 테이블1 A JOIN 테이블2 B ON (A.칼럼 = B.칼럼);**

- **CROSS JOIN** : 가능한 모든 조합으로 조인(카테시안 곱 발생)

  **SQL >> SELECT 칼럼 FROM 테이블1, 테이블2;(조인 조건이 없을 때 발생 <-> NATURAL JOIN은 명시해야 함)**

- **OUTER JOIN** : 조인 조건에서 행에 동일한 값이 없는 칼럼 조인, USING 조건절이나 ON 조건절 필수

  - **LEFT OUTER JOIN** : 좌측 테이블 데이터 조회 후 우측 테이블 조인 대상 데이터 조회

    **SQL >> SELECT 칼럼s FROM 테이블1 A LEFT OUTER JOIN 테이블2 B ON (A.칼럼 = B.칼럼);**

    **SQL >>  SELECT 칼럼s FROM 테이블1 A, 테이블2 B WHERE A.칼럼(+) = B.칼럼;**

  - **RIGHT OUTER JOIN** : 우측 테이블 데이터 조회 후 좌측 테이블 조인 대상 데이터 조회

  - **FULL OUTER JOIN** : LEFT와 RIGHT OUTER JOIN 포함

    **SQL >> SELECT 칼럼s FROM 테이블1 A FULL OUTER JOIN 테이블2 B ON (A.칼럼 = B.칼럼);**

#### 3. 집합 연산자

- 집합 연산자 : 조인 없이 여러 테이블의 관련 데이터를 조회하는 연산자

- UNION : 합집합, 칼럼 수와 데이터 타입이 모두 동일한 테이블 간 연산만 가능

  **SQL >> SELECT 칼럼명 FROM 테이블명 A WHERE 조건절 UNION SELECT 테이블명 WHERE  조건절;**

  - UNION ALL : 중복된 행도 모두 출력하는 합집합, 정렬 안함(<->UNION은 정렬 유발함), 집합 연산자에 속함

    **SQL >> SELECT 칼럼명 FROM 테이블A WHERE 조건절 UNION ALL SELECT 테이블명 WHERE 조건절;**

- INTERSECT : 교집합

  **SQL >> SELECT 칼럼명  FROM 테이블명 A WHERE 조건절 INTERSECT SELECT 테이블명 WHERE 조건절;**

- MINUS(Oracle), EXCEPT(SQL Server) : 차집합

  **SQL >> SELECT 칼럼명 FROM 테이블명 A WHERE 조건절 MINUS SELECT 테이블명 WHERE 조건절;**

#### 4. 계층형 질의와 셀프조인

- **계층형 질의(Hierarchical Query) : 계층형 데이터를 조회하기 위해 사용함, Oracle에서 지원함**

  - 계층형 데이터 : 엔터티를 순환관계 데이터 모델로 설계할 때 발생함

  - **CONNECT BY** : 트리 형태의 구조로 쿼리 수행(루트 노드 부터 하위 노드의 쿼리를 실행함)

    EX> 상사 이름과 사람 이름을 조인하여 상사 밑에 넣기

    - **START WITH : 시작 조건 지정**
    - **CONNECT BY PRIOR : 조인 조건 지정**
      - **LEVEL : 검색 항목의 깊이, 최상위 계층의 레벨은 1**
      - **CONNECT_BY_ROOT : 최상위 계층 값 표시**
      - **CONNECT_BY_ISLEAF : 최하위 계층 값 표시**
      - **SYS_CONNECT_BY_PATH : 계층 구조의 전개 경로 표시**
    - **CONNECT BY 절의 루프 알고리즘 키워드**
      - **NOCYCLE : 순환구조의 발생지점까지만 전개**
      - **CONNECT_BY_ISCYCLE : 순환구조 발생지점 표시(부모노드와 자식노드가 같을 때 1 아니면 0 출력)**
    - **LPAD : 계층형 조회 결과를 명확히 하기 위해 사용(LEVEL 값을 이용하여 결과 데이터 정렬)**

- SQL Server 계층형 질의 : CTE(Common Table Expression)로 재귀 호출

- **셀프 조인 : 한 테이블 내에서 두 칼럼이 연관 관계가 있는 경우, 앨리어스 필수**

#### 5. 서브쿼리

- 서브쿼리 : 하나의 SQL문 안의 SQL문

- 종류

  - **동작 방식에 따른 분류**
    - 비연관 서브쿼리 : 메인쿼리 칼럼을 가지고 있지 않는 서브쿼리, 메인쿼리에 값을 제공하기 위한 목적으로 주로 사용함
      - **Access Subquery : 제공자 역할**
      - **Filter Subquery : 확인자 역할**
      - **Early Filter Subquery : 데이터 필터링 역할**
    - 연관 서브쿼리 : 메인쿼리의 결과를 조건이 맞는지 확인하기 위한 목적으로 주로 사용함
  - **반환 데이터 형태에 따른 분류**
    - 단일 행 서브쿼리 : 실행 결과가 1건 이하인 서브쿼리, 단일 행 비교 연산자와 함께 사용
    - 다중 행 서브쿼리 : 실행결과가 여러 건인 서브쿼리, 다중 행 비교 연산자와 함께 사용
    - **다중 행 비교 연산자**
      - **IN : 서브쿼리의 결과중 하나의 값이라도 동일하다는 조건**
      - **ANY : 서브쿼리의 결과 중 하나의 값이라도 만족한다는 조건**
      - **ALL : 서브쿼리의 모든 결과값을 만족한다는 조건**
      - **EXISTS: 서브쿼리의 결과를 만족하는 값이 존재하는지 여부를 확읺는 조건, "WHERE EXISTS (SELECT)" (항상 연관 서브쿼리로 사용)**
    - 다중 칼럼 서브쿼리 : 실행 결과로 여러 칼럼 반환, 주로 메인쿼리의 조건과 비교하기 위해 사용(비교하고자 하는 칼럼의 개수와 위치가 동일해야 함)

- **스칼라 서브쿼리** : 값 하나를 반환하는 서브쿼리, SELECT 절에 사용하는 서브쿼리

- **뷰** : 가상의 테이블, FROM절에 사용하는 뷰는 인라인 뷰(Inline View)라고 함

  - 장점
    - 독립성 : 테이블 구조 변경 자동 반영
    - 편리성 : 쿼리를 단순하게 작성할 수 있음, 자주 사용하는 SQL문의 형태를 뷰로 생성하여 사용할 수 있음
    - 보안성 : 뷰를 생성할 때 칼럼을 제외할 수 있음

- **WITH** : 서브쿼리를 이용하여 뷰로 사용할 수 있는 구문

  SQL >> WITH 뷰명 AS (SELECT ~)

#### 6. 그룹 함수

- ANSI / ISO 표준 데이터 분석 함수 : 집계 함수, 그룹 함수, 윈도우 함수

- 그룹 함수 : 합계 합산 함수, NULL을 빼고 집계함(~ 집계함수), 결과값 없는 행은 출력 안함

  - **ROLLUP** : GROUP BY로 묶인 칼럼의 소계 계산, 계층 구조로 GROUP BY의 칼럼 순서가 바뀌면 결과 값 바뀜

  - **CUBE** : 조합 가능한 모든 값에 대해 다차원 집계

  - **GROUPING SETS** : 특정 항목에 대한 소계 계산, GROUP BY의 칼럼 순서와 무관하게 개별적으로 처리함

    |             표현식             |                      출력값                      |
    | :----------------------------: | :----------------------------------------------: |
    |    GROUP BY ROLLUP(E1, E2)     |             E1과 E2별 소계 / 총 합계             |
    |     GROUP BY CUBE(E1, E2)      | E1과 E2별 소계 / E1별 소계 / E2별 소계 / 총 합계 |
    | GROUP BY GROUPING SETS(E1, E2) |              E1별 소계 / E2별 소계               |

    - 'GROUP BY CUBE(E1, E2)'와 'GROUPING SETS(E1, E2, (E1, E2), ())'는 동일한 결과 출력

- GROUPING : 그룹 함수에서 생성되는 합계를 구분해주는 함수, 소계나 합계가 계산되면 1 아니면 0 반환

#### 7. 윈도우 함수

- 윈도우 함수(Window Function) : 여러 행 간의 관계 정의 함수, 중첩 불가

  - 순위 함수
    - RANK : 중복 순위 포함
    - DENSE_RANK : 중복 순위 무시(중간 순위를 비우지 않음)
    - ROW_NUMBER : 단순히 행 번호 표시, 값에 무관하게 고유한 순위 부여
  - 일반집계 함수 : SUM, MAX, MIN, AVG, COUNT
  - 행 순서 함수
    - FIRST_VALUE, LAST_VALUE : 첫 값, 끝 값
    - LAG, LEAD : 이전 행 이후 행(Oracle)
      - LEAD(E, A)는 E에서 A번째 행의 값을 호출하는 형태로도 쓰임(A의 기본값은 1)
  - 비율 관련 함수
    - PERCENT_RANK() : 백분율 순서
    - CUBE_DIST() : 현재 행 이하 값을 포함한 누적 백분율
    - NTILE(A) : 전체 데이터 A등분
    - RATIO_TO_REPORT : 총합계에 대한 값의 백분율

- 윈도우 함수 문법

  **SQL >> SELECT 윈도우함수(A) OVER (PARTITION BY 칼럼 윈도잉절) FROM 테이블명;**

  - PARTION BY : 그룹핑 기준
  - ORDER BY : 순위 지정 기준
  - 윈도잉절 : 함수의 대상이 되는 행 범위 지정
    - BETWEEN A AND B : 구간 지정
      - N PRECEDING, N FOLLOWING : N번째 앞 행, N번째 뒤 행
      - UNBOUNDED PRECEDING, UNBOUNDED FOLLOWING : 첫 행, 끝 행
      - CURRENT ROW : 현재 행
    - ROWS, RANGE : 행 지정, 범위 지정

#### 8. DCL

- DCL : 유저를 생성하거나 권한을 제어하는 명령어, 보안을 위해 필요

  - GRANT : 권한 부여

    SQL >> GRANT CREATE 테이블 TO PJS

  - REVOKE : 권한 수거(제거)

    SQL >> REVOKE CREATE 테이블 FROM PJS