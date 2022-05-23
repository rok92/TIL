## 타입 변환과 다형성 / 객체 배열

#### 1. 다형성

> 같은 타입이지만 실행 결과가 다양한 객체를 이용(대입) 할 수 있는 성질을 말한다

- 하나의 타입에 여러개의 객체를 대입하여 다양한 기능 이용 가능

- 부모 타입에는 모든 자식 객체가 대입 가능

- 자식 타입은 부모 타입으로 자동 타입 변환 발생

  <img src="C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20220523191327361.png" alt="image-20220523191327361" style="zoom:67%;" />

- **자동 타입 변환(Promoted)**

  - 프로그램 실행중에 자동으로 타입변환이 일어나는 것

    <img src="C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20220523191839255.png" alt="image-20220523191839255" style="zoom:67%;" />

  - 바로 위의 부모가 아니더라도 상속 계층의 상위이면 자동 타입변환 가능

    - 비록 변수는 자식 객체를 참조하지만 변수로 접근 가능한 멤버는 부모 클래스 멤버로 한정한다.

      <img src="C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20220523192426730.png" alt="image-20220523192426730" style="zoom:67%;" />

  - **주의**

    - 변환 후에는 부모 클래스 멤버만 가능

      <img src="C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20220523192709309.png" alt="image-20220523192709309" style="zoom:67%;" />

  - 자동 타입 변환 후에는 부모 클래스 멤버만 접근 가능

  - ```java
    Animal cat = new Cat(); // 자동 타입 변환
    //cat 변수는 Cat 객체를 참조하지만 Animal멤버만 접근이 가능하다.
    ```

  - 예외의 경우 : 오버라이딩

    - 메소드가 자식 클래스에 오버라이딩이 되었다면 자식 클래스의 메소드가 대신 호출된다.

  - 상속받은 경우

    - cat객체 Animal, Cat 멤버 접근 가능

    - ```java
      Animal c = new Cat();
      	// c는 Animal만 접근 가능
      	// 단, 오버라이딩 메소드는 Cat메소드 사용 가능
      ```

#### 정리

- 다형성

  - 동일한 타입이지만 실행 결과가 다양한 객체를 이용할 수 있는 성질
  - 코드 측면해서 보면 하나의 타입에 여러 객체를 대입함으로써 다양한 기능을 이용할 수 있게 된다.
  - 자식 클래스에서 다양하게 메소드 오버라이딩 구현

- 강제 타입 변환(Casting)

  - 부모 타입을 자식 타입으로 변환하는 것

  - **주의!!**

    - 모든 부모 타입을 자식 클래스 타입으로 강제 변환할 수 있는 것은 아니다

    - 조건

      - 자식 타입을 부모 타입으로 자동 변환된 후, 다시 자식 타입으로 변환할 때만 가능하다.(원위치의 개념)

        <img src="C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20220523193557269.png" alt="image-20220523193557269" style="zoom:67%;" />

  - **강제 타입 변환이 필요한 경우**

    - 자식 타입이 부모 타입으로 자동 변환되면 부모 타입에 선언된 필드와 메소드만 사용 가능(오버라이딩 예외)

    - **자식 타입에 선언된 필드와 메소드를 다시 사용해야 할 경우**

#### 2. 객체 배열

> 객체를 가리키기 위한 레퍼런스 배열을 의미한다.

<img src="C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20220523193842605.png" alt="image-20220523193842605" style="zoom:50%;" />

<img src="C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20220523193903210.png" alt="image-20220523193903210" style="zoom:50%;" />

- 객체를 가리키는 레퍼런스를 원소로 가지는 배열

- ```java
  Person[] p = new Person[5];  //레퍼런스(참조변수) 5개 생성
  ```

  <img src="C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20220523194000029.png" alt="image-20220523194000029" style="zoom:67%;" />

- ```java
  p[i] = new Person();     //객체 생성
  ```

  - 객체가 생성되고 레퍼런스 배열의 각 원소가 객체를 가리킴

    <img src="C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20220523194053302.png" alt="image-20220523194053302" style="zoom:67%;" />

    => p : 레퍼런스 배열을 가리키는 참조 변수

    =>p[i] : **객체를 가리키는 참조 변수**

    
