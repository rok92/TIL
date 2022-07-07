### 프레임워크 기반의 서비스 프로그래밍6(백엔드 프로그래밍)

> 웹 개념 - 웹 프로그래밍의 이해
>
> 서블릿
>
> JSP
>
> **스프링 프레임워크 : MyBatis 사용**

- **스프링 데이터베이스 연동(MyBatis사용)**

  - **MyBatis (마이바티스)**

    - ORM(Object Relational Mapping : 객체 관계 맵핑) 프레임워크
    - 자바에서 JDBC를 이용할 경우 java 언어와 SQL 언어가 한 파일에 존재해서 재사용성이 좋지 않음
    - MyBatis가 JDBC의 이런 단점을 개선하여 SQL 명령어를 별도의 XML 파일에 분리하고 SQL 명령어와 자바 객체를 맵핑해주는 기능을 제공
    - SQL 재사용 효율적. 쉬움

  - **MyBatis 특징**

    - SQL 명령어를 자바 코드에서 분리하여 XML 파일에서 관리

      ![image-20220707155927628](Back_end6.assets/image-20220707155927628.png)

- **MyBatis 연동 스프링 프로젝트 작성 순서**

  - **1. MVC 프로젝트 생성**
  - **2. pom.xml 기본설정**
    - Java : 11
    - Spring : 5.2.22.RELEASE
    - Maven 1.8
  - **3. 프로젝트 설정**
    - Java Compiler
    - Java Build Path
    - Project Facets
    - web.xml 한글 인코딩 추가
  - **4. pom.xml에 데이터베이스 의존성 설정**
    - (라이브러리 추가 : < dependency> 추가)
    - Spring JDBC 의존성 : spring-jdbc
    - Connection Pool 의존성 : commons-dbcp
    - mysql 의존성
    - mybatis / mybatis-spring 의존성
  - **5. 데이터베이스 연결 정보설정**
    - **jdbc.properties 파일 생성**
      - jdbc.driverClassName
      - url / username / password
    - **스프링 설정 파일 생성 : application-config.xml**
      - DataSource / Mapper 지정
    - **web.xml에 변경된 내용 설정**
  - **6. 클래스 구성 : CRUD 기능 구현**
    - 컨트롤러
    - 서비스 인터페이스 / 클래스
    - VO
    - DAO / Mapper (XML)
    - 뷰 페이지 작성
    - 패키지 생성
      - controller
      - dao
      - model
      - service

  #### **< 예제>**

- **Sql에서 데이터베이스 생성**

  - 스키마 : springdb

  - 테이블 : product

    ```sql
    CREATE TABLE product(
    	prdNo CHAR(20) NOT NULL PRIMARY KEY,
        prdName VARCHAR(30) NOT NULL,
        prdPrice INT,
        prdCompany VARCHAR(30),
        prdStock INT
    );
    
    INSERT INTO product
    		VALUE('1001', '노트북', 1000000, '삼성', 10),
    			 ('1002', '냉장고', 1200000, 'LG', 5),
                 ('1003', '마우스', 30000, '로지텍', 12);
    
    SELECT * FROM product;
    ```

    

- **1. MVC 프로젝트 생성**

  - 프로젝트명 : spring_mvc_mybatis
  - 패키지명 : com.spring_mvc.mybatis

- **2. pom.xml 기본설정**

  - Java : 11
  - Spring : 5.2.22.RELEASE
  - Maven 1.8

- **3. 프로젝트 설정**

  - Java Compiler
  - Java Build Path
  - Project Facets
  - web.xml 한글 인코딩 추가

- **4. pom.xml에 데이터베이스 의존성 설정**

  - (라이브러리 추가 : < dependency> 추가)

  - Spring JDBC 의존성 : spring-jdbc

    ![image-20220707173220450](Back_end6.assets/image-20220707173220450.png)

  - Connection Pool 의존성 : commons-dbcp

    ![image-20220707173239511](Back_end6.assets/image-20220707173239511.png)

  - mysql 의존성

    ![image-20220707173259987](Back_end6.assets/image-20220707173259987.png)

  - mybatis 의존성

    ![image-20220707173335821](Back_end6.assets/image-20220707173335821.png)

  - mybatis-spring 의존성

    ![image-20220707173350184](Back_end6.assets/image-20220707173350184.png)

- **5. 데이터베이스 연결 정보설정**

  - **5.1> src/main/resources 폴더에 database 폴더 생성하고 그 안에 jdbc.properties 파일 생성**

    - 데이터베이스 연결하기 위한 정보 설정

    - jdbc.driverClassName

    - url / username / password

      ```properties
      jdbc.driverClassName=com.mysql.cj.jdbc.Driver
      jdbc.url=jdbc:mysql://localhost:3306/springdb?serverTimezone-UTC
      jdbc.username=root
      jdbc.password=1234
      ```

  - **5.2 >스프링 설정 파일 생성**

    - src/main/resources 폴더에spring 폴더 생성하고그 안에 application-config.xml 생성

      - [Namespaces]에서beans / context / mybatis-spring체크

      - DataSource / Mapper지정

        ![image-20220707174005173](Back_end6.assets/image-20220707174005173.png)

      ```xml
      <?xml version="1.0" encoding="UTF-8"?>
      <beans xmlns="http://www.springframework.org/schema/beans"
      	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      	xmlns:context="http://www.springframework.org/schema/context"
      	xmlns:mybatis-spring="http://mybatis.org/schema/mybatis-spring"
      	xsi:schemaLocation="http://mybatis.org/schema/mybatis-spring http://mybatis.org/schema/mybatis-spring-1.2.xsd
      		http://www.springframework.org/schema/beans http://www.springframework.org/schema/beans/spring-beans.xsd
      		http://www.springframework.org/schema/context http://www.springframework.org/schema/context/spring-context-4.3.xsd">
      ```
    
  - **web.xml에 변경된 내용 설정**
  
    - **application-config.xml 사용한다고 설정**
  
      ```xml
      <!-- The definition of the Root Spring Container shared by all Servlets and Filters -->
      	<context-param>
      		<param-name>contextConfigLocation</param-name>
      		<param-value>classpath:/spring/application-config.xml</param-value>		<!--이부분 설정 변경-->
      	</context-param>
      ```
  
      
  
- **6. 클래스 구성 : CRUD 기능 구현**

  - **6.1 패키지 생성**

    - controller

    - dao

    - model

    - service

      ![image-20220707174752078](Back_end6.assets/image-20220707174752078.png)

  - **6.2 클래스 및 인터페이스 생성 : 해당 패키지 안에 생성**

    - ProductVO 클래스

    - IProductService 인터페이스 / Product 클래스(인터페이스를 오버라이딩) => import org.springframework.stereotype.Service;
    
    - IProductDAO 인터페이스
    
      - MyBatis에서는 DAO 인터페이스 필수
    
    - ProductMapper.xml 생성
      - application-config.xml에 dao 패키지 추가
      - <mybatis-spring:scan base-package="com.spring_mvc.mybatis.dao"/>
    - ProductController 클래스 생성
    
    - views 폴더에 index.jsp 생성
    

#### CRUD 기능 구현

1. **전체 상품 조회 (SELECT)**
   - ProductController에서 요청 받아서ProductService 클래스의 listAllProduct() 메소드 호출 
   - IProductDAO의 listAllProduct() 메소드 호출
     - ProductMapper에서 SQL 처리하고 결과 반환
   - ProductService에서 받아서 ProductController에게 반환
   - ProductController에서 View 페이지로 전달
   - 화면에 결과 출력
   - 예제순서 : **ProductController => ProductService(dao설정) => ProductMapper(select문 작성) => productAllListView.jsp만들고 테이블형태로 출력**