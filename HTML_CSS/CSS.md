### CSS

### 1. 스타일 시트(CSS)

- **Cascading Style Sheets** : 계단형 스타일 시트

  - 단계적으로 스타일 적용
  - 여러 스타일이 겹치면 맨 마지막 스타일 적용

- HTML의 레이아웃 배치 등의 한계를 보완하기 위해 개발된 독립언어

- 일정 기능들을 미리 지정하여 여러 부분에서 동일하게 적용

- 가능한 작업

  - HTML문서 내의 글꼴, 크기, 색상, 배경, 테두리, 레이아웃, 배치, 여백 등 지정
  - 글자의 정렬방식, 그림자 지정 등 다양한 효과
  - 애니메이션, 동적 기능 구현 가능

- **장점**

  - 자유롭게 웹 문서 편집
    - HTML한계점 극복 가능
  - 통일감 있는 문서 작성
    - 한 번만 정의하여 문서에 일관되게 적용 가능
  - 편리한 문서 관리
    - 외부 스타일 스타일시트 사용 할 때
    - 여러 웹 문서에 동일한 스타일 시트 사용가능하고 한 번만 수정하여 모든 웹 문서의 스타일을 동시에 변경가능

- 스타일 시트 적용 방법

  - (1) 문서 내부에 정의(Embedded Style)

    - < head> 태그에 삽입

    - 문서 전체에 특정 효과 주기 위해 사용

      <img src="CSS.assets/image-20220614175807457.png" alt="image-20220614175807457" style="zoom:80%;" />

  - (2) **외부 문서에 연결(Linked Style)**

    - 별도의 스타일 시트 문서를 만들어 두고 필요한 HTML문서에 연결하여 사용

    - 웹사이트의 모든 문서에 동일한 효과를 적용하여 웹사이트에 통일감을 주고 싶을 때 사용

    - 규모가 커지면 반드시 외부 문서에 연결하여 사용

      <img src="CSS.assets/image-20220614180118359.png" alt="image-20220614180118359" style="zoom:80%;" />

  - (3) 태그에 직접 정의(Inline Style)

    - 특정 태그에만 스타일 시트를 적용할 때 사용
    
      <img src="CSS.assets/image-20220614180054519.png" alt="image-20220614180054519" style="zoom:80%;" />

- **다중 스타일 시트**

  - 하나의 요소에 대하여 외부, 재부, 인라인 스타일이 서로 다르게 지정되어 있는 경우 적용되는 스타일
  - 스타일 적용 순서
    - 웹 브라우저 디폴트 값
    - 외부 스타일
    - < head> 부분의 내부 스타일
    - **태그에 정의된 인라인 스타일(최종 적용된 스타일)**

### 2. 스타일 시트의 기본 형식

- **선택자(selector)**

  - 스타일을 적용할 대상
  - HTML 문서의 태그, 아이디, 클래스, 속성 등으로 선택

- **형식 : { 속성 : 값;}**

  - 변경(적용)하고자 하는 속성
  - 글꼴, 크기, 색상, 위치 등

- 예> 모든 < h1>태그에 스타일 적용

  - h1{color : red**;**} → 세미콜론 반드시!! 있어야 함

- 선택자 유형

  - 태그 선택자

    - 태그명 사용

    - 요소(Element) 선택자라고도 함

    - HTML문서에 있는 같은 모든 태그에 동일하게 적용

    - 태그명{속성 : 값;}

      <img src="CSS.assets/image-20220614180210755.png" alt="image-20220614180210755" style="zoom:80%;" />

  - 클래스 선택자

    - 문서에서 특정 부분에만 필요한 CSS적용할 때 사용

    - . 사용

    - 사용자 정의 선택자 또는 도트(.) 선택자라고 함

    - 정의한 클래스 선택자를 태그에 적용

    - 여러 태그에 적용 가능

    - 그룹화 의미

    - HTML태그에 class = “클래스이름” 으로 지정되어 있어야 함

    - 형식
      - . 클래스이름 { 속성 : 값; }
      - **< 태그명 class = “클래스이름”>< /태그명>**

      <img src="CSS.assets/image-20220614180243910.png" alt="image-20220614180243910" style="zoom:80%;" />

  - 아이디 선택자

    - 문서에서 특정 부분에만 필요한 CSS적용할 때 사용

    - 필요한 부분에 **유일한 아이디**를 지정하고 CSS적용

    - 식별 선택자라고도 함

    - **#**사용

    - HTML태그에 **id= “아이디이름”** 으로 지정되어 있어야 함

    - 형식
      - \#아이디명{ 속성 : 값;}
      - < 태그명 **id = “아이디이름”**>< /태그명>

      <img src="CSS.assets/image-20220614180310928.png" alt="image-20220614180310928" style="zoom:80%;" />

  - 속성 선택자

    - 문서에 삽입된 HTML태그의 지정된 속성 값에 따라 선택자로 정의

    - 예> < a>태그의 title속성 값

      < a title = “산업기사” href = “[www.naver.com](http://www.naver.com)”>< /a>

    - 형식

      - 태그명[ 속성=”값”] : 일치하는

      - 태그명[ 속성^=”값”] : 시작하는

      - 태그명[ 속성$=”값”] : 끝나는

        <img src="CSS.assets/image-20220614192702300.png" alt="image-20220614192702300" style="zoom:80%;" />

      ![image-20220614183107487](CSS.assets/image-20220614183107487.png)

  - 상태 선택자

    - 태그의 상태에 따라서 선택 가능
    - 선택자 : **checked** - 체크된 input태그 선택
    - 선택자 : **focus**- 포커스를 받은 input태그 선택
    - 선택자 : enable- 사용 가능한 input태그 선택
    - 선택자 : disable- 사용 불가능한 input태그 선택

### 3. CSS 속성

- **텍스트 속성**

  - font-family : "굴림", "맑은 고딕", ...; 	=> (1순위, 2순위, ...)
  - font-size : 40px;		=>글자크기
  - color : blue;              => 글자색
  - font-style : italic;     => 글자모양
  - font-weight : bold;     => 글자굵게
  - text-decoration : underline;     => 밑줄긋기
  - letter-spacing : 3px;     =>글자사이의 간격
  - word-spacing : 5px;     => 단어사이의 간격
  - line-height : 10px;     => 줄간격
  - text-align : center; , left;     =>글자 가운데정렬, 왼쪽정렬
  - text-shadow : 2px, 2px, 2px, black;    => 가로, 세로 크기, 색상;

- **배경 색상 / 이미지 관련 속성**

  - **배경색**

    - background-color : #333;
    - background-color : rgb(0,255,0);

  - 배경 이미지 / 반복

    - background-image : url(back.png);
    - background-repeat : repeat;
    - background-repeat : no-repeat;
    - background-repeat : repeat-x;
    - background-repeat : repeat-y;

  - 테두리 속성

    - 테두리의 유형 / 두께 / 색상 지정
      - border : solid 1px black;
      - border-style : solid;
      - border-width : 3px;
      - border-radius : 10px;     =>모서리 둥글게

    ![image-20220614181452326](CSS.assets/image-20220614181452326.png)

  - 여백 속성(padding, margin)

    <img src="CSS.assets/image-20220614181546462.png" alt="image-20220614181546462" style="zoom:80%;" />

- **display 속성 : inline / block / inline-block**

  - block
    - 행으로 나란히 배치되며 옆으로 나란히 배치 안됌.
    - 여백여부 : 0
  - inline
    - 옆으로 나란히 배치
    - 여백없이 내용물 공간만큼만 차지
  - inline-block
    - 인라인, 블록 성격 모두 가지고 있음
    - 옆으로 나란히 배치하면서 박스내 여백 존재 : 0

- **float 속성**

  - 해당 요소를 떠 있게 만드는 속성
  - 기본 레이아웃 흐름에서 벗어나 왼쪽이나 오른쪽으로 이동하는 것을 의미
  - left : 왼쪽에 위치
  - right : 오른쪽에 위치

- **목록 관련 속성**

  - type 있고 / 없음

  - 블릿 기호 없애고 가로로 배치

    <img src="CSS.assets/image-20220614182132764.png" alt="image-20220614182132764" style="zoom:80%;" />

- **위치 관련 속성 : postion 속성**

  - **static(디폴트)**

    - 다른 요소와 겹치지 않게 배치
    - 위치를 지정하지 않으면 static 적용.**(디폴트)**

  - **relative**

    - **static의 원래 위치를 기준으로 계산**

  - **absolute**

    - 가장 가까운 상위 요소(부모)를 기준으로 배치

    - 상위 요소가 static인 경우 브라우저 화면 기준

    - 문서의 기본 margin 없애기

      ***{margin : 0;}**

  - **fixed**

    - **브라우저 화면을 기준으로 고정 위치에 배치**
    - 스크롤시 고정되어 있음

  - **레이어(겹침)**

    - z-index 속성
    - 요소들이 겹칠 때 순서 지정
    - 나중에 배치하는 것이 위에 놓임
    - z-index값이 클수록 위에 놓음

    <img src="CSS.assets/image-20220614182310609.png" alt="image-20220614182310609" style="zoom:80%;" />

- **자식 / 자손 선택자 (상속 선택자)**

  - 자식 / 자손의 개념

    <img src="CSS.assets/image-20220614182417588.png" alt="image-20220614182417588" style="zoom:80%;" />

  - **자식 선택자 : >부호 사용**
    - 선택자 > 자식 선택자
    - 선택자A > 선택자B
    - \#header > h1
  - **자손(후손) 선택자 : 띄어 쓰기(간격)**
    - 선택자 자손선택자
    - 선택자A 선택자B
    - \#header h1
    - \#pageNav ul li a : hover
    - < table> 태그에 자식 선택자 사용시 주의
      - table >tr >th{color:red;} : 적용안됨
      - 개발자 도구에서 Elements 확인하면 < tbody>태그 존재
        - **table > tbody > tr > th {color: red;} : 적용됨**
  - **first-child 선택자**
    - .wrap div:first-child
    - .wrap div:first-child + div
  - **nth-child(숫자)**
    - .wrap div:nth-child(1)
    - .wrap div:nth-child(2)
    - .wrap div:nth-child(3)
  - **동적(반응) 선택자**
    - 선택자 : active - 마우스로 클릭한 태그 선택
    - 선택자 : hover - 마우스를 올린 태그 선택
  - **가운데 정렬**
    - align.html
    - 컨테이너 태그 자신을 가운데 정렬
      - margin :0 auto; width : 400px;
    - 안에 포함된 내용을 가운데 정렬
      - text-align : center;
    - 주의 < table>인 경우
      - margin:0 auto; width:400px;
        - margin:0 auto; 사용할 경우 width 속성값이 있어야 함

- **문서 외부에 CSS 정의**

  - CSS파일 인코딩 : UTF-8
    - **Window / Preferences / Web / CSS Files**
    - **Encoding : ISO 10646/Unicode(UTF-8) 선택**
  - CSS 파일 생성 (.css)
  - HTML < head> 태그에
    - **< link rel="stylesheet" type="text/css" href="a.css">**

- **overflow 속성**

  - 자식 요소가 부모 요소의 범위를 벗어났을 때 어떻게 처리할 것인지 지정
  - **hidden**
    - 부모 영역을 벗어나는 부분은 보이지 않게 처리
  - **scroll**
    - 스크롤바 표시 (가로, 세로)
  - **auto**
    - 자동으로 필요한 부분에만 스크롤바 표시
  - 예제 : overflow.html
  - **투명도 / 가시성**
    - **투명도(불투명도)**
      - opacity 속성
        - 0 ~ 1 사이의 값 지정
        - 0 : 투명 (안 보임)
        - 1 : 불투명 (보임)
        - 0.5 : 반투명
    - **가시성 (보임 / 안 보임)**
      - visibility 속성
        - hidden : 숨김 (안 보임)
        - visible : 보임