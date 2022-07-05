### 프레임워크 기반의 서비스 프로그래밍5(백엔드 프로그래밍)

> 웹 개념 - 웹 프로그래밍의 이해
>
> 서블릿
>
> JSP
>
> **스프링 프레임워크 : 자바 기반 웹 프레임워크**

- Spring MVC 패턴

  - **M : Model(DTO / DAO) / V : View(JSP) / C : Controller**

  - 웹 애플리케이션 개발

    - 화면 : 프론트엔드 개발자(디자이너)
    - 비즈니스 로직 : 백엔드 개발자
    - 처음부터 새로 개발하는 것이 아니라 기존의 웹 애플리케이션 개발 방법에 따라 개발
    - 많이 사용하는 표준화 소스 구조를 만들어 개발 진행

  - 웹 애플리케이션 모델

    - 표준화된 소스 구조

      - **모델1 방식**

        - 모든 클라이언트의 요청과 비즈니스 로직을 JSP가 담당

        - 클라이언트 요청 > JSP(화면 기능 / 로직처리) > DAO > 데이터베이스

        - 기능 구현이 쉽고 편리

        - 웹 사이트 화면 기능이 복잡해지고 화면 기능과 비즈니스 로직 기능이 섞이면서 유지보수 문제 발생

        - 코드 재사용성도 떨어짐

        - 비효율적

          ![image-20220705130809440](Back_end5.assets/image-20220705130809440.png)

      - **모델2 방식**

        - 모델1 방식의 단점을 보완

        - 웹 애플리케이션의 각 기능을 분리해서 구현

          - 클라이언트 요청처리
          - 응답처리
          - 비즈니스 로직처리

        - 각 기능이 분리되어 모듈화 되어 있으므로 모듈별 개발이 가능

        - 모듈을 비슷한 프로그램 개발에 사용할 수 있어 코드 재사용성도 높음

        - 응용프로그램 확장성 및 이식성이 좋아짐

        - 개발 후 서비스 제공시 유지보수 편리

        - 현재 모든 웹 프로그램은 모델2 방식으로 개발

          ![image-20220705131130155](Back_end5.assets/image-20220705131130155.png)

- **FrontController 패턴**
  - 모든 클라이언트 요청을 한 곳에서 처리하도록 하나의 대표 컨트롤러 사용
  - 단점 : 별도의 클래스를 추가하지 않고 FrontController가 다 처리(FrontController 내용이 길고 복잡해짐)
  - 장점 : 클라이언트의 요청을 한 곳으로 집중시켜서 효율적으로 개발 및 유지보수 가능



- **Command 패턴**

  - FrontController가 모든 클라이언트 요청을 직접 다 처리하지 않고 각 작업에 해당되는 클래스가 처리(분산)

  - FrontController가 수행하던 작업을 각 클래스로 분산처리

  - 각 클래스는 통일된 형식(규격)으로 처리하도록 interface로 구현

    ![image-20220705131519275](Back_end5.assets/image-20220705131519275.png)

- **Spring MVC 구조**

  - DIspatcherServlet

    - 컨트롤러 선택(HandlerMapping을 통해)해서 요청을 컨트롤러에게 전달

    - View 검색(ViewResolver)해서 해당되는 View로 서비스 응답

      ![image-20220705131906493](Back_end5.assets/image-20220705131906493.png)

- **Spring 디렉터리 구조**

  ![image-20220705140815881](Back_end5.assets/image-20220705140815881.png)

  - **url에서 context명 확인**
    - http:// localhost:8080/**project**/
    - server.xml에서 < Context path="/**project**"...../>
    - 프로젝트의 패키지명 : com.spring_mvc.**project**

- **View의 요청 경로(path) 설정**

  - 원하는 경로로 View 경로 설정
  - views 폴더 안에 원하는 폴더 생성하고 .jsp 페이지 저장

- **Spring Controller**

  - 스프링 컨트롤러는 빈으로 등록되어야 하며 비즈니스 로직이 실행되기 위해 빚니스 객체를 의존성 주입(DI) 해야함

  - @Controller 어노테이션 사용

  - @RequestMapping 어노테이션을 사용하여 url 맵핑

  - **요청 처리 메소드 구현**

    - @RequestMapping 아래에 작업을 처리할 메소드 추가
      - 필요한 클래스(객체)는 파라미터로 받아서 사용

  - 뷰 페이지 이름 반환

    - return "뷰페이지 이름만(확장자 없음)";

  - **Controller 클래스 작성**

    - 클래스 생성 후 @Controller 붙임
    - @RequestMapping 어노테이션을 사용하여 요청 경로 지정
    - 요청처리 메소드 구현
    - 뷰 페이지 이름 반환(return)

  - **Controller 클래스 작성 예제**

    - NewController 클래스 추가(@Controller 어노테이션 붙이고, @RequestMapping어노테이션 사용해서 요청 경로 지정)

    - 요청 처리 메소드 구현하고 뷰 페이지 이름 반환 : newView

      ```java
      package com.spring_mvc.project;
      
      import org.springframework.stereotype.Controller;
      import org.springframework.web.bind.annotation.RequestMapping;
      
      // (1) 컨트롤러 클래스 생성하고 @Controller 어노테이션 붙임
      @Controller
      public class NewController {
      	
      	// (2) @RequestMapping 어노테이션을 사용하여 요청 경로 지정
      	// 'newView' 요청처리
      	@RequestMapping("/newView")
      	public String newView() {	// (3) 요청처리 메소드 구현
      		return "newView";	// (4) 뷰페이지 이름 반환 : newView.jsp
      	}
      
      }
      ```

    - views 폴더에 newView.jsp 생성 후 프로젝트 실행

      ```jsp
      <%@ page language="java" contentType="text/html; charset=UTF-8"
          pageEncoding="UTF-8"%>
      <!DOCTYPE html>
      <html>
      <head>
      <meta charset="UTF-8">
      <title>newView</title>
      </head>
      <body>
      	newView.jsp입니다.
      </body>
      </html>
      ```

      

- **데이터 전달**

  - Controller => View페이지
    - 전달 방법 : Model, ModelAndView 사용
    - Model
      - Model 인터페이스
      - Model Attribute 추가하기 위해 고안
      - key/value 형태로 값을 임시 저장
      - Controller에서 Model에 데이터 저장하고 View이름을 return하면 View페이지로 Model이 전달
      - View 페이지에서 key를 사용해서 Model에 저장된 데이터 사용
  - **ModelAndView 사용형식**
    - ModelAndView 클래스 사용
    - 데이터와 뷰 둘 다 설정
    - 반환값으로 ModelAndVeiw 객체 반환
    - ModelAndView mv = new ModelAndView();
      - **파라미터로 받을 수 있음 : public String show(ModelAndView mv)의 형태**
    - **mv.addObject(“name”, “홍길동”);** // 데이터 설정
    - **mv.setViewName(“showInfo2”);** // 뷰 이름 설정
    - **return mv;** // ModelAndView 객체 반환
  - **Model사용형식**
    - 요청 처리 메소드에서 Model 객체를 파라미터로 받음
      - **public String home(Locale locale, Model model)**
    - addAttribute() 메소드로 key / value 설정
      - **model.addAttribute("serverTime", formattedDate );**
    - return 되는 뷰페이지로 전달 : data 추출
      - **${serveTime}**
  - **Model과 ModelAndView 같이 사용 가능**