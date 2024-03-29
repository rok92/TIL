### Ajax 정리

> AJAX는 XML에 기반한 종합 기술로 Asychronous Javascript XML(비동기 자바스크립트 XML)을 줄인 말로 자바스크립트로 HTTP 요청을 보내 XML 응답을 받아 사용하는 기술

##### Ajax란??

- AJAX는 **하나의 독립된 기술이 아니다**. 화면은 표준 HTML + CSS 로 구성 및 작성하고 화면에 대한 조작과 상호작용은 문서 객체 모델(Document Object Model, DOM)로 처리하고 데이터 교환은 XML 형식으로 처리한다. 그리고 데이터의 변환과 검색은 XML 기술인 XSL과 XPath를 사용하며, 비동기 통신에는 웹 브라우저 안에 내장되어 있는 XMLHttpRequest 객체를 사용한다. 이 모든 것을 하나로 묶는 언어로 자바스크립트를 사용한다. 이것을 AJAX라고 한다

- **웹**
  
  - 동기통신, 턴 방식
  
  - 클라이언트와 서버 간의 데이터 교환을 턴 방식으로 운영한다.
  
  - 클라이언트가 서버에 요청을 보내고, 응답이 돌아올 때 까지 **클라이언트는 대기**. 응답이 돌아오면, 기존의 결과는 모두 삭제되고, 새 응답을 가지고 다시 전체 출력을 하게 된다.

- **Ajax**
  
  - 비동기 통신
  
  - 클라이언트가 서버에 요청을 보내고, 응답이 돌아올 때 까지 백그라운드에서 처리된다. 사용자는 AJAX 요청, 응답 과정에서 **영향을 받지 않는다**. 응답이 돌아오면, 기존의 결과에 응답을 추가하는 형태로 결과를 보여준다.

- **처리과정**
  
  - HTTP 요청을 보냄 -> XML문서를 응답으로 받음 -> 자동으로 XML 개체가 생성됨 -> 자바스크립트는 XML 개체에 접근하여 다양한 작업을 진행하게 됨
  
  - 자바스크립트로 HTTP 요청을 보내서 XML 응답을 받아 사용하는 기술

- **장점**
  
  - **웹 페이지 전체를 다시 로딩하지 않고도, 웹 페이지의 일부분만을 갱신할 수 있다.**
  
  - 웹 페이지가 로드된 후에 서버로 데이터 요청을 보낼 수 있다. (Post를 통해 값을 서버쪽으로 전달해 처리되고 받아올수 있음)
  
  - **비동기 통신**을 사용함으로써 데이터를 보내고 나서도 사용자는 다른 작업을 할 수 있게 된다.
  
  - **데이터만 들어가 있는 형식**으로 응답을 받게 되기 때문에 전통적인 웹 어플리케이션 방식에 비해서 서버 측의 처리 속도도 빠르고 전송 데이터의 양도 훨씬 적다.
  
  - 응답으로 받은 XML 문서를 XML 개체로 접근하여 스크립트로 조작하고 XPath를 사용하여 XML 문서를 검색하거나 XSL을 사용하여 변환하거나 하는 것들이 가능하다. 즉, **실행 속도가 빠르다**.

- **단점**
  
  - 외부 검색 엔진이 웹 페이지를 검색할 수 없는 문제가 있다
  
  - **AJAX는 클라이언트 풀링 방식(사용자가 직접 원하는 정보를 서버에게 요청하여 얻는 방식)으로 실시간 서비스를 제공할 수 없다.**
  
  - AJAX가 포함된 HTML 페이지가 속해있는 서버가 아닌 다른 서버로 요청을 보낼 수 없고, 클라이언트 PC 파일에 접근할 수도 없다.

- **요청절차**
  
  1. XMLHttpRequest 객체 생성
  
  2. AJAX 객체 정보 설정 (서버 주소, 데이터 첨부, 방식-비동기, 콜백함수)
  
  3. AJAX 요청 (send)
  
  4. AJAX 상태 이벤트 확인 콜백 함수 호출
  
  5. 서버로부터 응답이 도착하면(이벤트) 결과 출력. DOM 기술.

- **작동방식**
  
  1. 웹 페이지에서 이벤트 발생. (페이지가 로드된 이후 버튼 클릭)
  
  2. 요청 이벤트가 발생하면 이벤트 핸들러에 의해 자바스크립트가 호출
  
  3. **자바스크립트는 XMLHttpRequest 객체를 사용하여 서버로 요청을 보냄**(이때 웹 브라우저는 요청을 보내고 나서, **서버의 응답을 기다릴 필요 없이** 다른 작업을 처리할 수 있다.)
  
  4. 서버는 전달받은 XMLHttpRequest 객체를 가지고 Ajax 요청을 처리합니다.
  
  5. 서버는 처리한 결과를 HTML, XML 또는 JSON 형태의 데이터로 웹 브라우저에 전달
     
     (이때 전달되는 응답은 새로운 페이지를 전부 보내는 것이 아니라 필요한 데이터만을 전달)
  
  6. 서버로부터 전달받은 데이터를 가지고 웹 페이지의 일부분만을 갱신하는 자바스크립트를 호출
  
  7. 결과적으로 웹 페이지의 일부분만이 다시 로딩되어 표시
     
     ![](C:\Users\kyeon\AppData\Roaming\marktext\images\2022-07-27-00-06-07-image.png)
