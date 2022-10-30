### MVC Pattern

<hr>

#### MVC 패턴이란?

> Model-View-Controller의 약자로 애플리케이션을 세 가지 역할로 구분한 개발 방법론이다. 사용자가 Controller를 조작하면 Controller는 Model을 통해 데이터를 가져오고 그 데이터를 바탕으로 View를 통해 시각적 표현을 제어하여 사용자에게 전달하게 된다.
>
> 이러한 패턴을 성공적으로 사용하면 사용자 인터페이스로부터 비즈니스 로직을 분리하여 애플리케이션의 시작적 요소나 그 이면에서 실행되는 비즈니스 로직을 서로 영향 없이 쉽게 고칠 수 있는 애플리케이션을 만들 수 있게 된다.

![img](https://blog.kakaocdn.net/dn/bDpdks/btrjV9EuRJ3/egwkkBELr5i0oYOv4t9Qy1/img.png)

1.  **사용자가 웹사이트에 접속(USER)**
2.  **Controller는 사용자가 요청한 웹페이지를 서비스 하기 위해 모델을 호출(MAINPULATES)**
3.  **Model은 데이터베이스나 파일과 같은 데이터 소스를 제어한 후 그 결과를 Return**
4.  **Controller는 Model이 리턴한 결과를 View에 반영(UPDATES)**
5.  **데이터가 반영된 View는 사용자에게 보여짐(SEES)**

#### MVC 패턴 방식

- MVC패턴에는 모델1과 모델2 방식이 있다.

- 모델1

  - 모델 1 방식은 Controller 영역에 View 영역을 같이 구현하는 방식이며, 사용자의 요청을 JSP가 전부 처리한다. 요청을 받은 JSP는 JavaBean Service Class를 사용하여 웹브라우저 사용자가 요청한 작업을 처리하고 그 결과를 출력한다.

    ![img](https://blog.kakaocdn.net/dn/w08Lw/btrlbKqhWKO/qUYnM7xziHIQUE28L6WBZ1/img.png)

- 모델2

  - 모델 2 방식은 웹브라우저 사용자의 요청을 서블릿이 받고 서블릿은 해당 요청으로 View로 보여줄 것인지 Model로 보낼 것인지를 판단하여 전송한다. 또한 모델 2 방식의 경우 HTML 소스와 JAVA소스를 분리해놓았기 때문에 모델 1 방식에 비해 확장시키기도 쉽고 유지보수 또한 쉽다.

    ![img](https://blog.kakaocdn.net/dn/bGZKd4/btrleqFoykC/kXkFFucLJdHJ4hNvfcmav0/img.png)

|      |                            모델 1                            |                           모델 2                            |
| :--: | :----------------------------------------------------------: | :---------------------------------------------------------: |
| 장점 |                    빠르고 쉽게 개발 가능                     | 디자이너와 개발자의 분업이 가능하며 유지보수 및 확장이 쉬움 |
| 단점 | JSP파일이 너무 비대해지며 Controller와 View가 혼재하므로 <br />향후 유지보수가 어려움 |             설계가 어려우며 개발 난이도가 높음              |

#### Model

> 데이터를 가진 객체를 모델이라고 지정한다. 데이터는 내부 상태에 대한 정보를 가질 수도 있고, 모델을 표현하는 이름 속성으로 가질 수 있다. 모델의 상태에 변화가 있을 때 컨트롤러와 뷰에 이를 통보한다. 통보를 통해서 뷰는 최신결과를 보여줄 수 있고, 컨트롤러는 모델의 변화에 따른 적용 가능한 명령을 추가, 제거, 수정 할 수 있다.

- **모델의 규칙**
  - 사용자가 편집하기를 원하는 모든 데이터를 가지고 있어야 한다.
  - 뷰나 컨트롤러에 대해서 어떠한 정보도 알지 말아야 한다.
  - 변경이 일어나면 변경 통지에 대한 처리방법을 구현해야 한다.

#### View

> view는 클라이언트 측 기술 HTML/CSS/Javascript들을 모아둔 컨테이너이다. 사용자가 볼 결과물을 생성하기 위해 모델로부터 정보를 얻어온다.

- **뷰의 규칙**
  - 모델이 가지고 있는 정보를 따로 저장해서는 안된다.
  - 모델이나 컨트롤러와 같이 다른 구성 요소를 몰라야 한다.
  - 변경이 일어나면 변경 통지에 대한 처리방법을 구현해야 한다.

#### Controller

> 사용자가 접근한 URL에 따라 사용자의 요청사항을 파악한 후 그 요청에 맞는 데이터를 Model에 의뢰하고, 데이터를 View에 반영하여 사용자에게 알려준다.
>
> 모델에 명령을 보냄으로써 뷰의 상태를 변경할 수 있다 =>(워드에서 문서 편집)
>
> 컨트롤러가 관련된 모델이 명령을 보냄으로써 뷰의 표시방법을 바꿀 수 있다. =>(문서를 스크롤 하는 것)

- **컨트롤러의 규칙**
  - 모델이나 뷰에 대해서 알고 있어야 한다.
  - 모델이나 뷰의 변경을 모니터링 해야 한다.

#### MVC 패턴을 사용해야 하는 이유

- 비즈니스 로직과 UI로직을 분리하여 유지보수를 독립적으로 수행가능하다.
- Model과 View가 다른 컴포넌트들에 종속되지 않아 애플리케이션의 확장성, 유연성에 유리하다.
- 중복 코딩의 문제점이 제거 가능하다.

#### MVC 패턴의 한계

- MVC패턴에서 View는 Controller에 연결되어 화면을 구성하는 단위 요소이므로 다수의 View를 가질 수 있다. 그리고 Model은 Controller를 통해서 View와 연결되지만, Controller에 의해서 하나의 View에 연결될 수 있는 Model도 여러 개가 될 수 있어 View와 Model이 서로 의존성을 띄게 된다. 즉, Controller에 다수의 Model과 View가 복잡하게 연결되어 있는 상황이 발생할 수 도 있다.

#### In Summary

- Model - 백그라운드에서 동작하는 비즈니스 로직(데이터) 처리
- View - 정보를 화면으로 보여주는 역할
- Controller - 사용자의 입력 처리와 흐름 제어 담당, 화면과 Model과 View를 연결시켜주는 역할