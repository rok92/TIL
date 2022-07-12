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
     - 프로젝트명 / Group / Artifact / 패키지명
     - Dependencies 선택
       - SQL : JDBC API / MyBatis Framework / MySQL Driver
       - Web : Spring Web
  2. **프로젝트 생성 후 확인**
     - pom.xml 확인
       - java.version / jdbc / mysql-connector / tomcat
     - 자동 생성된 클래스 파일 확인
       - ServletInitializer.java
         - 스프링 부트 애플리케이션을 web.xml 없이 톰캣에서 실행하게 해주는 클래스
         - 스프링 부트에는 web.xml, context.xml 설정 파일 없음
       - ......Application.java
         - @SpringBootApplication 붙어있음
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
       - mapper.xml 위치 지정(src/main/resources 파일에서 생성할 것임)
         - DAO와 mapper파일 추가한 후에 설정
     - 컨트롤러 추가하고 ("/") 실행시켸소 오류있는지 확인
  4. **JSP 뷰 설정**
     - 스프링 부트는 JSP 뷰가 기본이 아니기 때문에 JSP 뷰 사용할 경우 추가 설정 필요
       - application.properties 파일에 JSP 설정 추가
         - **spring.mvc.view.prefix=/WEB-INF/views/**
         - **spring.mvc.view.suffix=.jsp**
       - pom.xml 의존성 라이브러리 추가
       - src/main/webapp 폴더에 WEB-INF/views 폴더 추가
       - hello.jsp 생성하고 controller애소 @RequestMapping 추가해서 실행되는지 확인
       - 스프링 부트에서 리소스 파일 경로 확인
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
         - product 폴더 안에 ProductMapper.xml 파일 복사
           - DAO/VO 경로 수정
         - application.properties에 mapper 위치 설정
           - mybatis.mapper-locations=classpath:mappers/\**/\*.xml
         - …Application.java 클래스에 추가
           - 컴포넌트 클래스(Controller와 Service)에 대해 추가
           - @ComponentScan(basePackageClasses=ProductController.class)
             @ComponentScan(basePackageClasses=ProductService.class)
             @MapperScan(basePackageClasses=IProductDAO.class)
     - 파일 위치 주의

