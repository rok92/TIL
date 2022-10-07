### Web Server VS WAS

<hr>

#### 웹 서버

> 사전적 정의로는 웹 브라우저 클라이언트로 부터 HTTP 요청을 받아들이고 HTML문서와 같은 웹 페이지를 반환하는 컴퓨터 프로그램이다.

- 웹 서버란 클라이언트(사용자)가 웹 브라우저에 어떠한 페이지 요청을 하면 웹 서버에 그 요청을 받아 **정적 컨텐츠를 제공하는 서버**이다. 여기서 정적 컨텐츠란 **단순 HTML, CSS, Javascript, 이미지, 파일 등 즉시 응답 가능한 컨텐츠** 이다. 그렇다고 웹 서버는 정적 컨텐츠만 제공하는 것이 아니라 동적 컨텐츠 요청을 받으면 WAS에게 해당 요청을 넘겨주고 WAS에서 처리한 결과를 클라이언트(사용자)에게 전달해 주는 역할도 한다.

  ![image-20221008010415655](C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20221008010415655.png)

#### WAS

> 사전적 정의로는 인터넷상에서 HTTP 프로토콜을 통해 사용자 컴퓨터나 장치에 애플리케이션을 수행해주는 미들웨어로써 주로 동적 서버 컨텐츠를 수행하는 것으로 웹 서버와 구별이 되며, 주로 데이터베이스 서버와 함께 수행한다.

- WAS는 웹 서버와 웹 컨테이너가 합쳐진 형태로서 웹 서버 단독으로는 처리할 수 없는 **데이터베이스의 조회나 다양한 로직 처리가 필요한 동적 컨텐츠를 제공**한다. WAS는 JSP, Servlet구동환경을 제공해주기 때문에 <u>웹 컨테이너</u> 혹은 <u>서블릿 컨테이너</u>라 불린다.

  ![image-20221008010953671](C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20221008010953671.png)

#### Web Service Architecture

웹 어플리케이션은 요청처리 방식에 따라 다양한 구조를 가질 수 있다.

- 클라이언트(사용자) -> Web Server -> DB

- 클라이언트(사용자) -> WAS -> DB

- 클라이언트(사용자) -> Web Server -> WAS -> DB

  ![image-20221008011341252](C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20221008011341252.png)

#### 클라이언트 => Web Server => WAS => DB  구조의 동작과정

1. Web Server는 웹 브라우저 클라이언트로 부터 HTTP 요청을 받는다.
2. Web Server는 클라이언트의 요청(Request)를 WAS로 보낸다.
3. WAS는 관련된 Servlet을 메모리에 올린다.
4. WAS는 web.xml을 참조하여 해당 Servlet에 대한 Thread를 생성한다.(Thread pool이용)
5. HttpServletRequest와 HttpServletResponse 객체를 생성하여 Servlet에 전달한다.
6. Thread는 Servlet의 service() 메소드를 호출한다.
7. service()메소드는 요청에 맞게 doGet() 또는 doPost() 메소드를 호출한다.
8. protected doGet(HttpServletRequest request, HttpServletResponse response)
9. doGet 또는 doPost 메소드는 인자에 맞게 생성된 적절한 동적 페이지를 Response객체에 담아 WAS에 전달한다.
10. WAS는 Response객체를 HttpResponse형태로 바꾸어 Web Server에 전달한다.
11. 생성된 Thread를 종료하고 HttpServletRequest와 HttpServletResponse 객체를 제거한다.

#### WAS만 사용해도 될까?(정답은 X)

- WAS는 DB조회 및 다양한 로직을 처리하는데 집중해야 한다. 따라서 단순한 정적 컨텐츠는 웹 서버에게 맡기며 기능을 분리시켜서 **서버 부하를 방지**한다. 만약 WAS가 정적 컨텐츠 요청까지 처리를 한다면 부하가 커지고 동적 컨텐츠 처리가 지연되면서 수행 속도가 늦어지고 이로 인해 페이지 노출 시간이 늘어나는 문제가 발생하여 **효율성이 크게 저하**된다.