### JavaScript2

- 함수

  - 특정 기능을 수행하고 결과를 돌려주는 독립적인 코드집합

  - 독립적인 모듈{}

  - 메소드, 모듈, 기능, 프로시저 등으로 불림

  - 함수를 사용하기 위해서는 반드시 호출해야 함

    - 함수는 호출하지 않으면 일 안함

    - 함수 호출 : 함수명();

      <img src="C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20220617194947512.png" alt="image-20220617194947512" style="zoom:80%;" />

    - 다른 함수내에서 호출 가능

      <img src="C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20220617195020311.png" alt="image-20220617195020311" style="zoom:80%;" />

- **함수 선언 형식**

  - function 함수명(){

    **// 함수 body : 수행 문장**

    }

- **스스로 동작하는 함수**

  - (function() {….})();
  - 함수 호출 없이도 자동 실행

- **함수 반환값**

  - 함수 실행이 끝난 후 호출한 곳으로 돌려주는 결과값

  - 함수 내에서 return 문 사용

    <img src="C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20220617195058362.png" alt="image-20220617195058362" style="zoom:80%;" />

  - 소수점 자리수 표시 함수 : toFixed(자릿수)

    - avg.toFixed(2) : 소수점 이하 두 자리 출력

    - 천단위 구분 기호 표시 : toLocaleString()
      - amount.toLocaleString() : 1,000,000 표시

- 함수의 매개변수

  - 함수를 호출 시 전달된 값을 받기 위해 사용되는 변수

    <img src="C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20220617195140232.png" alt="image-20220617195140232" style="zoom:80%;" />

- 함수 호이스팅

  - 함수 선언 보다 먼저 함수 호출해서 실행되는 기능
    - **function 키워드 사용해서 생성한 함수는 호이스팅 가능**
    - **show(); // 먼저 호출 : 함수 호이스팅 가능**

- **function show() { … } // 나중에 함수 선언(정의)**

- 선언적 함수 (일반 함수 : function() { })

- 익명 함수

  - **함수명 대신 변수명에 함수 코드를 저장하는 구현 방식**
  - **var 변수명 = function(매개변수) { };**
  - **익명 함수의 호이스팅 불**

- 콜백 함수

  - 콜백 함수 (Callback Function)

    - 매개변수로 함수를 전달받아서, 함수의 내부에서 실행하는 함수
    - 인자로 넘겨지는 함수를 콜백 함수라고 부름
    - 콜백 함수로는 주로 이름이 없는 익명 함수 사용(일반 함수도 콜백함수로 사용 가능)

  - 콜백 함수를 사용하는 이유

    - 자바스크립트에서 비동기 처리 방식의 문제점을 해결하기 위해 사용
    - 자바스크립트는 단일 스레드
      - 하나의 작업이 끝나고 다른 작업을 수행
      - 동시에 여러 개의 작업을 수행하지 않음
    - 콜백 함수를 사용해서 다른 작업이 끝나기 전에 비동기적으로 작업을 수행하는 것이 가능

  - 콜백함수 주의점

    - 콜백 지옥 발생
      - 콜백함수를 함수로 전달하는 과정이 반복적으로 이루어져 계속 들여쓰기 형식으로 콜백함수를 하다보면 감당하기 어려울 정도로 수준이 깊어짐
    - 지옥 해결 방법
      - Promise : ES6도입
      - async-await : ES8추가

  - 콜백 함수에서 지역변수를 매개변수로 전달

    - 함수 내의 지역변수를 콜백함수 호출하면 전달 가능

    - function call(callback){

      var localVar = 1;

      callback(localVar);

      }

    - **동기적 / 비동기적 콜백 함수 예제**

      - 동기적 : 순서대로 수행
        - **예제 : function_callback_sync.html**
      - 비동기적 콜백 함수 사용
        - **동시에 여러 작업 수행**
      - **function_callback_async.html**

- 화살표 함수

  - function 키워드 대신 화살표 ( ⇒)사용하여 간결한 방법으로 함수를 선언하는 함수
  - () ⇒ {,,,,,}  // 매개변수가 없는 경우
  - x ⇒ {,,,,,,}  // 매개변수가 한 개인 경우, () 생략 가능
  - (x, y) ⇒ {,,,,,,}  // 매개변수가 여러 개인 경우, 괄호 생략 불가
  - x ⇒ {return x*x}  //리턴값이 있는 경우
  - x ⇒ x*x  // 1줄인 경우 return 생략 가능

- 디폴트 매개변수(Default Parameter)

  - 매개변수를 디폴트로 설정해 놓으면 전달되는 값이 없을 경우 디폴트 매개값으로 적용
  - !순서주의!!
    - 디폴트 매개변수와 일반 매개변수를 섞어서 사용할 경우 디폴트 매개변수를 맨 뒤에 위치 시켜야 함