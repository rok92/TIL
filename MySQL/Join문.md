### Join문

> 여러개의 테이블을 결합하여 조건에 맞는 행 검색

- 종류

  - **INNER JOIN(내부조인)**

    - 공통의 열이 있을 때 공통 속성의 속성값이 동일한 튜플(행)만 반환

      ```MYSQL
       조인문 표기 방식(1)
       SELECT client.clientNo, clientName, bsQty FROM client, booksale 
       WHERE client.clientNo = booksale.clientNo;
      
       조인문 표기 방식(2)
       SELECT client.clientNo, client.clientName, booksale.bsQty FROM client, booksale 
       WHERE client.clientNo = booksale.clientNo;
       
       조인문 표기방식(3)
       SELECT C.clientNo, C.clientName, BS.bsQty FROM client C, booksale BS 
       WHERE C.clientNo = BS.clientNo;
       
       조인문 표기방식(4)
       SELECT C.clientNo, C.clientName, BS.bsQty FROM booksale BS 
       JOIN client C ON C.clientNo = BS.clientNo;
       
       조인문 표기방식(5)	-- 가장 흔하게 쓰이는 방법
       SELECT C.clientNo, C.clientName, BS.bsQty FROM booksale BS 
       INNER JOIN client C ON C.clientNo = BS.clientNo;		
      
      ```

      

  - **OUTER JOIN(외부조인)**

    - 공통되는 열이 없을 때 공통된 속성을 매개로 하는 정보가 없더라도 버리지 않고 연산의 결과를 릴레이션에 표시

    - 값이 없는 대응 속성에는 NULL값을 채워서 반환

    - 좌측 외부조인(LEFT OUTER JOIN)

      - 좌측 릴레이션의 정보 유지

    - 우측 외부조인(RIGHT OUTER JOIN)

      - 우측 릴레이션의 정보 유지

    - 완전 외부조인(FULL OUTER JOIN)

      - 두 릴레이션의 모든 정보 유지

        ```MYSQL
        (1) 왼쪽 (LEFT) 테이블 기준
        SELECT * FROM client C 
        LEFT OUTER JOIN booksale BS on C.clientNo = BS.clientNo ORDER BY C.clientNo;
        
        (2) 오른쪽(RIGHT) 테이블 기준
        SELECT * FROM client C 
        RIGHT OUTER JOIN booksale BS on C.clientNo = BS.clientNo ORDER BY C.clientNo;
        
        (3) 완전 외부 조인(MYSQL에서는 지원하지 않음)
        SELECT * FROM client C 
        LEFT JOIN booksale BS on C.clientNo = BS.clientNo 
        
        UNION			-- UNION으로 결합
        
        SELECT * FROM client C 
        RIGHT JOIN booksale BS on C.clientNo = BS.clientNo;
        ```

        

- **JOIN의 기본 형식**

  - SELECT 열리스트 FROM 테이블명1

    ​							   INNER JOIN 테이블명2

    ON 조인조건(기본키 = 외래키);

  - 3개 테이블 결합
    - 조인 조건 2개
    - 외래키를 가지고 있어야 함