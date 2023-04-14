# Solidity란?

> 솔리디티는 contract를 이행해 주는 프로그래밍 언어로 이더리움에서 개발되어 Smart Contract 개발에 특화된 언어기술 입니다.
>
> 프로그래밍 언어를 개발할 때 IDE를 다들 사용해 보셨을 겁니다. 솔리디티 또한 IDE 환경을 제공해 주는데 브라우저에 있는 remix ide를 주로 많이 사용합니다.

### **1. Remix 셋팅**

- remix ide를 오픈하면 VsCode처럼 왼쪽에 폴더와 파일을 만들 수 있습니다.

- Practice라는 폴더를 생성 후 그 안에 HelloWorld.sol이라는 파일을 생성합니다.
  - 이때 .sol은 솔리디티의 확장자명 입니다.(javascript는 .js이듯이 솔리디티도 확장명이 있습니다.)

![img](https://blog.kakaocdn.net/dn/4bb1c/btr9YkCOlXs/WcklIv0rdUGrUYCEDDRdLk/img.png)

### 2. **Solidity 코드작성 및 시작**

프로그래밍 언어를 경험해보신 분들이라면 콘솔창에 'hello world'를 출력해본 경험이 있을 겁니다.

하지만 솔리디티는 print함수가 내장되어있지 않아서 event를 통해 print함수를 대체하여 remix상에서 출력해야 합니다.

간단하게 변수를 생성하여 'hello world'를 출력하겠습니다.

```solidity
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.18;

contract HelloWorld{
    string public greet = "Hello World!!";
}
```

**코드작성**

- // SPDX-License-Identifier: MIT => 이 라이센스를 무조건 맨 위에 작성해 주어야 에러가 나지 않습니다.
- pragma solidity ^0.8.18; => 솔리디티 컴파일 버전을 명시하는 것 입니다. ^는 이상을 의미하기에 0.8.18이상의 버전을 사용한다는 뜻 입니다.
- contract HelloWorld{ => 스마트 컨트랙트를 명시하는 것 입니다.
- string public greet = "Hello World!!"; => greet이라는 문자열 변수안에 'hello world'를 대입해 줍니다.
- **유의사항 : 세미콜론(;)은 변수명 끝에 항상 명시해 줘야하며 {}에는 사용하지 않습니다.**

### **3. Compile**

위의 간단한 코드로 스마트 컨트렉트가 생성되었습니다.

이제 컴파일을 해야 하는데 컴파일은 Ctrl+s를 누르거나 ide의 왼쪽 솔리디티 언어 로고를 클릭하면 컴파일을 할 수 있는 버튼과 컴파일러의 정보가 나타납니다.

![img](https://blog.kakaocdn.net/dn/bASgps/btr95qgT0V2/gXURuV3xWZeRs6D6sx7SWk/img.png)

1. 컴파일러의 버전을 명시해 줍니다.

2. 컴파일 버튼을 누르면 컴파일이 되고

3. 솔리디티 언어 로고모양 아래에 체크모양이 생기면 컴파일이 됬다는 의미 입니다.

4. **ABI는 정말 중요합니다. 스마트 컨트렉트의 함수와 파라미터에 대한 Meta Data를 정의해 Contract객체를 생성할 수 있고 Contract의 함수를 호출할 수 있는 표준방법입니다. Contract의 함수를 호출하기 위해서는 ABI Spec에 맞게 데이터를 변환해야 합니다. 이 때 데이터는 함수에 대한 정보와 함수 호출에 사용할 수 있는 인수로 구분하는데 이것이 ABI입니다.**

### **4. Deploy**

컴파일이 완료됬으면 배포를 해야합니다. 먼저 배포를 하려면 로고버튼 아래에 있는 버튼을 클릭해서 배포환경으로 이동해야 합니다.

![img](https://blog.kakaocdn.net/dn/bnWuvc/btr91TdmAvI/LrtWtTok0J0LzjGnrAFK61/img.png)

1. 배포를 할 때는 gas비가 발생하는데 리믹스는 이더리움 기반으로 제공하기 때문에 100이더가 주어집니다. 이때 사용할 수 있는 계좌를 나타냅니다

2. Deploy버튼을 누릅니다.

3. 콘솔창에 체크표시가 뜨면서 아래쪽에 3번과 같이 생성된 것을 알 수 있고, 문자열 안에 "Hello World"가 잘 들어가 있는 것을 확인할 수 있습니다.

 