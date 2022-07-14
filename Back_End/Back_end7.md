### 프레임워크 기반의 서비스 프로그래밍7(백엔드 프로그래밍)

> 스프링부트(Spring Boot) 프레임워크
>
> - 스프링 프레임워크를 사용하는 프로젝트를 아주 간편하게 설정할 수 있는 스프링 프레임워크의 서브 프로젝트

#### 스프링 부트

- **특징**
  - XML 기반 설정 과정 없이 간단히 프로젝트를 시작할 수 있음.
  - 메이븐의 pom.xml 파일에 의존성 라이브러리의 버전을 일일이 지정하지 않아도 됨(스프링 부트가 권장버전 관리)
  - 단독 실행되는 스프링 애플리케이션 구현 가능
  - 프로젝트 환경 구축에 필요한 서버 외적인 툴들이 내장되어 있어 별도의 설치 필요 없음(톰캣이 내장되어 있음)
  
- **프로젝트 생성 과정**
  1. **스프링 부트 프로젝트 생성**
     - 프로젝트명 / Group / Artifact / 패키지명 설정
     - **Java Version : 11로 바꾸기**
     - **Packaging : War**
     - **Dependencies 선택**
       - SQL : JDBC API / MyBatis Framework / MySQL Driver 체크
       - Web : Spring Web 체크
     
  2. **프로젝트 생성 후 확인**
     - pom.xml 확인
       - java.version / jdbc / mysql-connector / tomcat
     - 자동 생성된 클래스 파일 확인
       - ServletInitializer.java
         - 스프링 부트 애플리케이션을 web.xml 없이 톰캣에서 실행하게 해주는 클래스
         - 스프링 부트에는 web.xml, context.xml 설정 파일 없음
       - ......Application.java
         - @SpringBootApplication 어노테이션 붙어있음
         - 스프링 부트 애플리케이션으로 설정하는 어노테이션
         - main()메소드 포함
           - 스프링 부트 생성시 자동으로 생성
           - 스프링 부트 프로젝트는 반드시 main() 이 있어야 함
           - 스프링 부트 프로젝트 main()메소드를 시적점으로 실행
           - main() 메소드를 포함하는 java파일이 있어야 함
           - 이유 : 스프링 부트 웹 애플리케이션을 일반 자바 애플리케이션처럼 개발하려는 의도 때문
     
  3. **스프링 설정 파일**
     
     - application.properties 파일 자동 생성
     - 내용이 없는 빈 파일로 생성
     - 추가할 내용
       - 포트번호 : **server.port=8080**
       - 데이터베이스 연결정보
         - **spring.datasource.driver-class-name =** 
         - **spring.datasource.url =** 
         - **spring.datasource.username =**
         - **spring.datasiurce.password =** 
       - **mapper.xml 위치 지정(src/main/resources 파일에서 생성할 것임)**
         - DAO와 mapper파일 추가한 후에 설정
     - 컨트롤러 추가하고 ("/") 실행시킨 후 오류있는지 확인
     
  4. **JSP 뷰 설정**
     - 스프링 부트는 JSP 뷰가 기본이 아니기 때문에 JSP 뷰 사용할 경우 추가 설정 필요
       - application.properties 파일에 JSP 설정 추가
         - **spring.mvc.view.prefix=/WEB-INF/views/**
         - **spring.mvc.view.suffix=.jsp**
       - pom.xml 의존성 라이브러리 추가**(jstl / tomcat)**
       - src/main/webapp 폴더에 WEB-INF/views 폴더 추가
       - hello.jsp 생성하고 controller애소 @RequestMapping 추가해서 실행되는지 확인
       - 스프링 부트에서 리소스 파일 경로 확인(이미지 추가)
         - src/main/resources/static
     
  5. **DB 연동 CRUD 기능 구현**
     
     - spring_mvc_mybatis 에서 product 코드는 그대로 사용(일부 경로 수정)
       - **패키지 생성** 
         - controller / dao / model / service
         - 클래스 / 인터페이스 파일 (mapper 제외)
           - VO / service / DAO / Controller
         - 복사 시 주의! - 이전 패키지 import 삭제할 것
       
       - **mapper 파일 폴더 생성**
         - src/main/resources 폴더에 mappers 폴더 생성하고, 그 안에 product 폴더 생성
       
         - product 폴더 안에 ProductMapper.xml 파일 생성
           - DAO/VO 경로 설정
           
         - application.properties에 mapper 위치 설정
           - mybatis.mapper-locations=classpath:mappers/\**/\*.xml
           
         - …Application.java 클래스에 추가
           - 컴포넌트 클래스(Controller와 Service)에 대해 추가
           
           - @ComponentScan(basePackageClasses=ProductController.class)
             @ComponentScan(basePackageClasses=ProductService.class)
             @MapperScan(basePackageClasses=IProductDAO.class) 이렇게 사용하거나 
             
           - @ComponentScan(basePackages{com.spring_boot_mybatis.project})
           
             @MapperScan(basePackages{com.spring_boot_mybatis.project}) 이렇게 사용할 수 있음(간편)
       
       - **view페이지 생성**
       
         - product폴더 생성하고 관련 페이지들 생성
         - index.jsp는 views폴더안에 생성
       
       - **js폴더 생성(css파일도 같은 경로로 지정)**
       
         - src/main/resources/static 안에 폴더 생성하고 파일생성
       
       - **외부 경로 설정 : 상품 이미지 출력**
       
         - WebConfig 클래스 생성
         - WebMvcConfigurer 인터페이스 구현 후 @Configuration어노테이션 추가
           - 맵핑 이름과 이미지 위치 설정
           - Ex> **registry.addResourceHandler("images/")**
             		      **.addResourceLocations("file:///C:/springWorkspace/productImages/" );****
       
       - **파일 위치 주의!!!!**

#### **스프링 부트 프로젝트에 파일 업로드**

- **MultipartFile 클래스 사용**

  - 스프링 부트에서는 의존성 라이브러리 추가 필요 없음

  - 자동으로 MultipartConfigElement 클래스를 빈으로 등록

- **HTML**

  - < form enctype="multipart/form-data">
  - < input type="file">

- **업로드되는 파일 크기 제한 변경 가능**

  - application.properties 파일에서

  - maxFileSize
    - 업로드하는 파일 1개의 크기 : **디폴트 1M**

  - maxRequestSize 

    - 요청 크기 제한

    - 모든 파일의 크기를 합한 크기 값 제한

- **파일 업로드 방법 1(UUID : 식별자 표준**)

  - 파일명이 중복되지 않게 해서 업로드 하는 방법(같은 파일이라도 다 다르게 업로드 함)
  - 동일한 파일명으로 업로드 되는 경우 앞의 파일 덮어쓰게 되는 문제
  - 총 36개의 문자 (32개 문자와 4개의 하이픈)
  - 파일 업로드할 폴더 생성
    - springWorkspace 안에 upload 폴더 생성
  - 파일 업로드 폼 생성
    - views 폴더 안에 upload 폴더 만들고 fileUploadForm.jsp 생성
  - 파일 업로드 결과 출력 페이지 생성
    - fileUploadResult.jsp
  - 패키지 생성
    - com.spring_boot_mybatis.project 아래에 file 패키지 생성
  - 컨트롤러 생성
    - FileUploadController
  - index에 추가

- **파일 업로드 방법 2(여러개의 파일 업로드**)

  - fileUploadForm.jsp에 추가

    - < input type="file" multiple="multiple">

  - 컨트롤러에 추가 : /fileUploadMultiple

    - ArrayList< MultipartFile> files로 받음

    - Model 반환 ArrayList< String>로 반환

  - fileUploadMultipleResult.jsp 생성

    - < c:forEach> 사용

- **파일 업로드 방법 3(파일명 그대로 업로드)**

  - 원본 파일명을 그대로 사용하는 경우

    - 상품 사진 등록하게 하는 경우

    - 상품번호.jpg 업로드하도록

  - fileUploadForm.jsp에 추가

  - UUID 사용하지 않음

#### 파일 다운로드

- 폴더 내 모든 파일 목록 출력하고

- 목록에서 파일 선택해서 다운로드

- 파일명에 한글 들어 있는 경우 한글 출력 안 됨
  - 다운로드 컨트롤러에서 인코딩 처리
- 예제
  - FileDownloadController 생성
  - fileDownloadListView.jsp 생성
  - index에 추가
  - FileCopyUtils 클래스
    - 파일 및 스트림 복사를 위한 유틸리티 클래스
  - FileCopyUtils.copy()
    - 스프링 프레임워크에 내장된 파일 다운로드 기능
    - InputStream의 내용을 지정한 OutputStream에 복사하고 스트림을 닫음
    - InputStream/OutputStream
      - 바이트 기반 입/출력 스트림 클래스
    - 스트림을 열고, 복사, flush, close 기능 수행
  - **다운로드 컨트롤러에서 인코딩 처리**
    - **String encodedFileName = new String (file.getBytes("UTF-8"), "ISO-8859-1");**



