### RESTful API

<hr>

#### RESTful API 란?

- REpresentational State Transfer의 약어로 웹을 이용할 때 제약조건들을 정의하는 소프트웨어 아키텍쳐 스타일이다.HTTP URL을 통해서 자원(Resource)을 명시하고 HTTP Method(GET, POST, PUT DELETE)를 통해서 해당 자원(URL)에 대한 CRUD(Create, Read, Update, Delete)를 적용하는 것을 의미한다. 즉, HTTP의 장점을 살리고자 하는 통신규약이라 할 수 있다. 로이 필딩(Roy Fielding)의 2000년 박사학위에서 소개되었으며 RESTful API는 이러한 규약을 바탕으로 리소스 중심으로 설계가 가능하고 기능에 맞게 HTTP Method 사용하여 설계된 API이다.
  - **GET : 지정된 url에서 리소스의 표현을 조회**
  - **POST : 지정된 url에 신규 리소스를 생성**
  - **PUT : 지정된 url에 리소스를 생성하거나 업데이트**
  - **PATCH : 리소스의 부분 업데이트**
  - **DELETE : 지정된 url의 리소스를 제거**

#### RESTful API의 특징

- REST 아키텍쳐에 적용되는 6가지 제한조건
  - 인터페이스 일관성 : 일관적인 인터페이스로 분리되어야 한다.
  - 무상태 : 각 요청간 클라이언트의 context, 세션과 같은 상태 정보를 서버에 저장하지 않는다.
  - 캐시 처리 가능 : 클라이언트는 응답을 캐싱할 수 있어야 한다. 캐싱을 통해 대량의 요청을 효율적으로 처리할 수 있다.
  - 계층화 : 클라이언트는 대상 서버에 직접 연결되어 있는지, proxy를 통해 연결되어 있는지 알 수 없다.
  - Code on demand : 자바 애플릿이나 자바스트립트의 제공을 통해 서버가 클라이언트를 실행시킬 수 있는 로직을 전송하여 기능을 확장시킬 수 있다.
  - 클라이언트/서버구조 : 아키텍쳐를 단순화 시키고 작은 단위로 분리함으로써 클라이언트-서버의 각 파트가 독립적으로 구분하고 서로 간의 의존성을 줄인다.

#### REST 구성요소

- 자원(Resources) : HTTP URL
- 자원에 대한 행위 : HTTP Method
- 자원에 대한 표현(Representations)

#### **REST API 설계 Rulse 및 예시**

- 소문자를 사용한다.

  ```http
   http://cocoon1787.tistory.com/users/Post-Comments => 잘 못된 표현
  ```

  ```http
   http://cocoon1787.tistory.com/users/post-comments => 올바른 표현
  ```

- 언더바(_)대신 하이픈(-)을 사용한다.

  ```http
  http://cocoon1787.tistory.com/users/post_comments => 잘 못된 표현
  ```

  ```http
   http://cocoon1787.tistory.com/users/post-comments => 올바른 표현
  ```

  - **정확한 의미나 단어 결합이 불가피한 경우 하이픈("-")을 사용하며 하이픈("-") 사용도 최소한으로 설계한다.**

- 마지막에 슬래시(/)를 포함하지 않는다.

  ```http
  http://cocoon1787.tistory.com/users/ => 잘 못된 표현
  ```

  ```http
   http://cocoon1787.tistory.com/users => 올바른 표현
  ```

  - **슬래시(/)는 계층관계를 나타낼 때 사용한다**.

- 행위를 포함하지 않는다

  ```http
   POST http://cocoon1787.tistory.com/users/post/1 => 잘 못된 표현
  ```

  ```http
  DELETE http://cocoon1787.tistory.com/users/1 => 올바른 표현
  ```

  - **자원에 대한 행위는 HTTP Method(GET, POST, PUT, DELETE)로 표현한다.**

- 파일 확장자는 URL에 포함하지 않는다

  ```http
  http://cocoon1787.tistory.com/users/photo.jpg => 잘 못된 표현
  ```

  ```http
  GET http://cocoon1787.tistory.com/users/photo
     HTTP/1.1 Host: cocoon1787.tistory.com Accept: image/jp => 올바른 표현
  ```

  - **URL에 메시지 body 내용의 포맷을 나타내기 위한 파일 확장자를 적지 않는다. 대신 Accept header를 사용한다.**

- 자원에는 형용사, 동사가 아닌 명사를 사용하며 컨트롤 자원을 의미하는 경우 예외적으로 동사를 사용한다.

  ```http
  http://cocoon1787.tistory.com/duplicating => 잘 못된 표현
  ```

  ```http
  http://cocoon1787.tistory.com/duplicate
  ```

  - **URL은 자원을 표현하는데 중점을 두기 때문에 동사, 형용사보다는 명사를 사용하여야 한다.**