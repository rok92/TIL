### React_1

> 리액트란 페이스북이 만든 사용자 UI 구축을 위한 라이브러리 이다.
>
> 오직 사용자의 view에만 초점을 맞추고 있기 때문에 Routing과 같은 기술이 리액트 자체에 있지는 않지만 개발자들이 리액트에 필요한 것들을 만들어 두어서
>
> 사실상 프레임워크의 위치에 있는 라이브러리라고 할 수 있다.

#### 1. JSX

- JSX는 자바스크립트 안에서 HTML문법을 사용할 수 있게 하여서 view페이지에 나타날 수 있도록 하는 자바스크립트 문법이다.

  ```react
  function App() {
    return (
      <div>
        <h1 className={styles.title}>Welcome back!</h1>
        <Button text={"Continue"}/>
      </div>
    );
  }
  ```

  - 위의 코드를 보면 HTML태그가 들어가 있는 것을 볼 수 있다. 함수안 return문 안에 들어가 있는 것이 바로 JSX문법이다.
  - 원래 Javascript 문법은 저런 문법을 허용하지 않지만 JSX는 허용할 수 있게 해준다.

#### 2. Component

- 컴포넌트란 기존의 웹 페이지를 작성할 때 처럼 하나의 HTML코드를 집어넣고 하는 것이 아닌 **여러 부분을 분할해서 코드의 재사용성과 유지보수성을 증가**시켜주는 것 이다. 리액트는 컴포넌트 기반의 라이브러리 이다.
- 컴포넌트 기반의 리액트로 개발을 하게 되면 어떠한 부분의 수정이 필요할 떄 HTML코드를 일부 부분 파일로 담아서 그 부분의 파일만 수정하면 된다.

#### 3. VirtualDom(가상돔)

- 가상돔은 돔(DOM)의 한계를 탈피하기 위해서 나온 개념이다.
- DOM : Document Object Model 즉 문서 객체 모델이다. 우리가 사용하는 HTML 단위 하나하나를 객체로 생각한 모델이라고 생각하면 된다.

#### 4. useState

-  데이터를 UI로 나타내주는 react-hook이다

  ```react
  import {useState} from 'react';
  
  function App(){
      const [item, setItem] = useState();
  }
  ```

  



