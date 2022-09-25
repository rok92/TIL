### API JSON 파싱

> **API**란, **Application Programming Interface**의 약자로, 응용 프로그램에서 사용할 수 있도록, 운영 체제나 프로그래밍 언어가 제공하는 기능을 제어할 수 있게 만든 인터페이스를 뜻한다
>
> **OPEN API**란, 사용자가 제공되는 데이터를 자유롭게 활용할 수 있도록 만들어놓은 인터페이스이다.

##### API로 제공되어지는 형태는 대부분 `JSON`이나 `XML`로 제공이 된다.

- **XML**

  ```xml
  <response>
  	<header>
      	<resultCode>00</resultCode>
          <resultMsg>NOMAL_SERVICE</resultMsg>
      </header>
      <body>
      	<dataType>XML</dataType>
          <items>
          	<item>
              	<other>o 없음</other>
                  <t6>o 강풍주의보: 부산, 포항....</t6>
                  <t7>o 없음</t7>
                  <tmEf>202209130300</tmEf>
                  <tmFc>202209130000</tmFc>
                  <tmSeq>57</tmSeq>
              </item>
          </items>
          <numOfRows>10</numOfRows>
          <pageNo>1</pageNo>
          <totalCount>1</totalCount>
      </body>
  </response>
  ```

- **JSON**

  ```json
  {"bubbles":[{"data":{"description":"반려동물"},"type":"text"}],"event":"send","version":"v2","userId":"U47b00b58c90f8e47428af8b7bddc1231heo2","timestamp":1664104620182}
  ```

  - JSON이란 Javascript Object Notation의 약자로, key와 value로 이루어진 형태의 object이다.
  - 위의 코드 `"description":"반려동물"`에서 description는 key에 해당하고 반려동물은 value에 해당한다.