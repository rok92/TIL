### JavaScript3

- **Object**

  - **내장객체**

    - 미리 정의되어 있는 객체

    - 선언 과정을 통해 객체 변수를 정의해서 사용

    - 특별한 경우에는 사용자 정의 객체를 정의하여 사용

    - 대부분의 경우에는 내장 객체 사용

    - 대표적 내장 객체

      - **Date** 

        - 날짜와 시간을 처리하기 위한 객체

        - 웹 페이지에 오늘 날짜와 시간, 요일 등을 표시

        - **Date객체의 시간/날짜 정보를 반환하는 메소드**

          <img src="JavaScript3.assets/image-20220619220341415.png" alt="image-20220619220341415" style="zoom:80%;" />

        - **Date객체의 시간/날짜 정보를 설정하는 메소드**

          <img src="JavaScript3.assets/image-20220619220424926.png" alt="image-20220619220424926" style="zoom:80%;" />

        - **날짜/시간 정보의 포맷을 변경한는데 사용되는 메소드**

          - parse(날짜 문자열) : 문자열을 시간으로 변경
          - toGMTString() : 문자열을 GMT날짜로 복귀
          - toLocalString() : 날짜를 문자열로 반환

      - **Array** 

        - 배열을 만들기 위한 객체

        - Ex> 

          - var arr = new Array(3); // 생성
          - arr.push("홍길동");  // 데이터 삽입(사용법 : 객체.메소드();)

        - **주요 메소드들**

          <img src="JavaScript3.assets/image-20220619220831156.png" alt="image-20220619220831156" style="zoom:80%;" />

      - **String** 

        - 문자열을 다루기 위한 객체 

          - var name = new String();
          - name.fontsize(5);

        - new를 이용해서 객체를 생성하지 않고 상수형태("문자열")로 문자열을 만들어도 객체의 특징 모두 사용

          - var name = "홍길동";

          - name.fontsize(5);

          - 객체로 자동 변환(일시적)

          - **주요 메소드들**

            <img src="JavaScript3.assets/image-20220619221908177.png" alt="image-20220619221908177" style="zoom:80%;" />

          - **charAt(인덱스)**

            - 인덱스로 지정된 위치의 문자 반환
            - 인덱스는 0부터 시작
            - charAt(3); =>문자열 str에서 4번째 문자 반환

          - **substring(start, end)**

            - 문자열의 일부분을 추출
            - start ~ end-1까지의 문자열
            - 인덱스는 0부터 시작

          - **indexOf("문자")**

            - 문자열에서 지정된 문자의 위치를 인덱스 값으로 반환
            - 인덱스는 0부터 시작
            - **검색할 때 왼쪽부터 찾아서 처음 발견한 문자의 위치를 알려주는 것**
            - 찾고자 하는 문자가 없으면 **-1 반환**

          - **split("구분자")**

            - 구분자로 문자열 분리
              - str = "1998-09-09";
              - var bitth = str.split("-"); =>문자열이 "-"를 기준으로 분리되어 배열에 순서대로 저장
              - birth[0] : 1998 / birth[1] : 09 / birth[2] : 09 가 각각 저장됨  

      - **Math** 

        - 수학적 계산을 위한 객체

        - 상수값은 속성으로, 수학은 메소드로 제공

        - Math객체는 속성이나 메소드로 접근하기 위해 따로 객체변수 선언하지 않음

        - 형태 : Math.속성  /  Math.메소드()

        - **주요 메소드들**

          <img src="JavaScript3.assets/image-20220619221028544.png" alt="image-20220619221028544" style="zoom:80%;" />

      - **Math.random()**

        - 1~10 사이의 수중에 랜덤 숫자 생성
        - var num = 1 + Math.floor(Math.random()*10);
          - 0.01223454 ~ 0.999999999 : 0과 1사이의 실수
          - floor() : 소수점 이하를 버리게 함
          - 1 + : 1부터 시작하도록 베이스를 1
          - *10 : 0.xxx, 1.xxx

      - **Screen** : 화면의 해상도, 색상, 크기에 관한 정보를 제공하는 객체

    - Ex> 

      - 생성 : var today = new Date();  /  var arr = new Array(3);
      - 사용(객체.메소드()) : today.getMonth();  /  arr.sort();

  - 브라우저 객체

  - 문서 객체(DOM)

  - 사용자 정의 객체