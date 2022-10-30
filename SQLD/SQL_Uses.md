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