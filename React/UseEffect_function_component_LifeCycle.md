# UseEffect(function component LifeCycle)

### useEffect

- **function component**에서는 react hook중 하나인 **useEffect**가 클래스 컴포넌트에서의 lifeCycle역할을 수행해 준다.

- 사용전에 반드시 useEffect를 import 해줘야 한다.

  ```react
  import { useState, useEffect } from "react";
  ```

- useEffect는 함수로 arguments(매개변수)를 2개 받는다.(함수, 배열)

  ```react
  
  function App(){
      let counter = 0;
      const [counter2, setCoutner2] = useState(0);
      const increase = () => {
          counter = counter + 1;
          setCoutner2(counter2 + 1);
      }
      useEffect(() => {
      console.log("useEffect1 fire!");
  	}, []);
      return (
          <div>
              {console.log("render")}
              <div>{counter}</div>
              <div>{counter2}</div>
              <button onClick={increase}>클릭!</button>
          </div>
  	)
  }
  ```
  
  - `console.log`로 출력을 해보면 useEffect는 `return`안에 render후에 출력되고, LifeCycle에서의 `componentDidMount()`의 역할을 해준다는 것을 확인할 수 있다.
  - api호출작업을 여기서 한다.
  
  ```react
  function App(){
      let counter = 0;
      const [counter2, setCoutner2] = useState(0);
      const increase = () => {
          counter = counter + 1;
          setCoutner2(counter2 + 1);
      }
      useEffect(() => {
      console.log("useEffect2 fire!");
  	}, [counter2]);
      return (
          <div>
              {console.log("render")}
              <div>{counter}</div>
              <div>{counter2}</div>
              <button onClick={increase}>클릭!</button>
          </div>
  	)
  }
  ```
  
  - `console.log()`를 통해서 확인해보면 첫번째 예시와 같이 render후 useEffect2 fire가 호출되는 것을 볼 수 있고, array안에 counter2를 넣어주었을 때 `button`을 클릭하면 `counter2`가 호출되는 것을 볼 수있다. 따라서 useEffect에서 array의 역할은 `componentDidUpdate()`의 역할을 하는 것을 알 수 있다.
  - array의 특징상 여러개의 값을 넣을 수 있기 때문에 주시해야 하는 값들을 여러개 넣을 수 있다.

