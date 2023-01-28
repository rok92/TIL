# React LifeCycle(Class_component)

![image-20230127174600487](C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20230127174600487.png)

- **Mounting** : 앱, 컴포넌트가 막 시작되었을 때
  - constructure : 첫번째로 실행되는 lifecycle함수(앱이 실행되면 무조건 constructure을 실행하고 들어감), state를 만든다.
  - render : UI그려주는 함수
  - componentDidMount : UI가 완벽하게 셋팅이 되었을 때 알려주는 함수, API 콜을 해준다.
- **Updating** : state가 업데이트되고 UI업데이트 될 때
  - render : state, props, forceUpdate가 업데이트가 되면 render가 발생한다.
  - componentDidUpdate : state가 최신값으로 업데이트가 된지 알려주는 함수
- **Unmounting** : 컴포넌트가 종료될 때
  - componentWillUnmount : 컴포넌트가 종료되는 것을 알려주는 함수