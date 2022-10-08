### Ajax & axios & fetch

> 토이 프로젝트를 진행하다 보면 클라이언트와 서버간에 데이터를 주고 받기 위해 비동기 HTTP 통신을 하게 되는데 
>
> 이러한 통신을 위해 사람들이 많이 사용하는 방법에 Ajax, axios, fetch 이다.

#### Ajax

- Asynchronous JavaScript And XML의 약자이며, 자바스크립트를 이용해 클라이언트와 서버간에 데이터를 주고받는 비동기 HTTP 통신이다.

  XMLHttpRequest(XHR) 객체를 이용해서 전체 페이지가 아닌 필요한 데이터만 불러올 수 있다.

- **장점**
  - Jquery를 통해 쉽게 구현 가능
  - Error, Success, Complete 상태를 통해 실행 흐름 조절 가능
- **단점**
  - Jquery를 이용해야 간편하고 호환성이 보장됨
  - Promise기반이 아님
- **XHR(XMLRequestHttp)를 사용한 코드**

```javascript
var xhr = new XMLHttpRequest();
xhr.onreadystatechange = function() { // 요청에 대한 콜백
  if (xhr.readyState === xhr.DONE) { // 요청이 완료되면
    if (xhr.status === 200 || xhr.status === 201) {
      console.log(xhr.responseText);
    } else {
      console.error(xhr.responseText);
    }
  }
};
xhr.open('GET', 'https://localhost:3000'); // 메소드와 주소 설정
xhr.send(); // 요청 전송 
// xhr.abort(); // 전송된 요청 취소
```

- Jquery를 사용한 코드

```javascript
var serverAddress = 'https://localhost:3000';

// jQuery의 .get 메소드 사용
$.ajax({
    url: serverAddress,
    type: 'GET',
    success: function onData (data) {
        console.log(data);
    },
    error: function onError (error) {
        console.error(error);
    }
});
```

#### axios

- axios는 Node.js와 브라우저를 위한 Promise API를 활용하는 HTTP통신 라이브러리 이다.

  비동기로 HTTP 통신을 할 수 있으며 return을 promise로 해주기 때문에 response데이터를 다루기 쉽다.

- **장점**
  - response timeout(fetch에 없는 기능) 처리방법이 존재
  - Promise 기반으로 만들어졌기 때문에 데이터 다루기 편리
  - 브라우저 호환성이 뛰어남
- **단점**
  - 사용을 위해 모듈 설치 필용(npm intall axios)

- **코드**

```javascript
axios({
  method: 'post',
  url: 'https://localhost:3000/user',
  data: {
    userName: 'rok',
    userId: '12345678'
  }
}).then((response) => console.log(response));
```

#### fetch

- ES6부터 들어온 JavaScript 내장 라이브러리이다.

  Promise 기반으로 만들어졌기 때문에 axios와 마찬가지로 데이터를 다루기 쉽고, 내장 라이브러리라는 장점으로 상당히 편리하다.

- **장점**
  - 자바스크립트의 내장라이브러리 이므로 별도로 import할 필요가 없음
  - Promise 기반으로 만들어졌기 때문에 데이터를 다루기 편리
  - 내장 라이브러리이기 때문에 업데이트에 따른 에러방지 가능
- **단점**
  - 지원하지 않는 브라우저가 존재(IE11..)
  - 네트워크 에러 발생시 response timeout이 없어서 기다려야 함
  - JSON으로 변환해주는 과정 필요
  - 상대적으로 axios에 비해 기능이 부족
- **코드**

```javascript
fetch("https://localhost:3000/user/post", {
  method: "POST",
  headers: {
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    id: "aaa123",
    description: "hello world",
  }),
}).then((response) => console.log(response));
```



