### Generic 제네릭

> 제네릭은 클래스, 인터페이스 그리고 메소드를 정의할 때 타입을 파라미터로 표현한 것이다.
>
> 제네릭 타입을 이용하여 잘못된 타입이 사용될 수 있는 문제를 컴파일 과정에서 제거할 수 있게 되었다.

- **제네릭 사용시 이점**

  - 컴파일시 강한 타입 체크를 할 수 있다.

    - 컴파일시 미리 타입을 강하게 체크하여 에러 사전에 방지

  - 강제 타입 변환 제거 가능(프로그램 성능 향상)

  - 제네릭을 사용하지 않을 경우

    ```java
    List list = new ArrayList();
    list.add("hello");
    String str = (String)list.get(0);		// 강제 타입 변환
    ```

  - 제네릭을 사용할 경우

    ```java
    List<String> list = new ArrayList<String>();
    list.add("hello");
    String  str = list.get(0);				// 강제 타입 변환 할 필요 X
    ```

  - public class 클래스명< T>{….}

    public interface 인터페이스명< T>{ }

    모두 총칭해서 제네릭 타입이다.

  - Gen< String> gen = new Gen< String>();

    Gen< Integer> gen2 = new Gen< Integer>();

    <> : 

    - 기본 데이터 타입은 올수 X
    - < int >  : X
    - < Integer > : O (Wrapper 클래스 사용)
    -  In short
      - 클래스나 인터페이스를 설계할 때 구체적으로 명시하지 않고 타입 파라미터로 대체하였다가 실제 클래스가 사용될 때 구체적인 타입을 지정하여 타입 변환을 최소화 시킴으로써 프로그램 성능을 향상 시킬 수 있다.
      - 컴파일시 사전에 타입을 강하게 체크하여 에러를 방지

- **타입 파라미터**

  - 일반적으로 대문자 알파벳 하나로 표현

    - E : Element
    - T : Type
    - K : Key
    - V : Value

  - 개발 코드에서는 구체적인 파라미터 타입을 주어야 한다

    ```java
    Gen<String> gen = new Gen<String>();
    Gen<Integer> gen2 = new Gen<Integer>();
    ```

  - 클래스 내부에서 사용할 데이터 타입을 클래스 외부에서 지정

- **멀티타입 파라미터**

  - 제네릭은 두 개 이상의 타입 파라미터 사용 가능하다.

  - 각 타입의 파라미터는 콤마(,)로 구분

    - class....<K, V>{,,,,,,,} / interface.....<K, V>{,,,,,,}

  - 제네릭 타입 파라미터

    ```java
    public class Product<T, M>{
        private T kind;
        private K model;		// 알파벳 하나로 표현
    }
    ```

    ```java
    Product<Tv, String> product = new Product<Tv, String>();	// 구체적 타입 지정
    ```

- **제네릭 메소드**

  - 매개변수 타입과 리턴타입으로 타입 파라미터를 갖는 메소드
  - 제네릭 메소드 선언 방법
    - 리턴타입 앞에 "<>" 기호 추가하고 타입 파라미터 기술
    - 호출할 때 < T>가 결정나면 Box< T>와 매개변수< T t>가 결정
  - 제네릭 호출 두 가지 방법
    - (1) 명시적으로 구체적 타입 지정 호출
      - 리턴타입 변수 = <구체적타입> 메소드명(매개값);
      - Box < Integer> box = < Integer>boxing(100);
    - (2) 매개값을 보고 구체적 타입 추정 호출(더 많이 쓰이는 방법)
      - 리턴타입 변수 = 메소드명(매개값);
      - Box< Integer> box = boxing(100);

- **제네릭 타입의 상속과 구현**

  - 제네릭 타입을 부모로 사용할 경우 타입 파라미터는 자식 클래스에도 기술해야함!!!!!

    ```java
    public <T> Box<T> boxing(T t){....}
     타입파라미터 리턴타입
    ```

  - 자식 클래스는 추가적인 타입 파라미터 가질 수 있음

    ```java
    public class ChildProduct<T,M,C> extends ParentProduct<T,M>{....}
    ```

  - 제네릭 인터페이스를 구현할 경우

    - 제네릭 인터페이스를 구현한 클래스도 제네릭 타입

    ```java
    public class StorageImpe<T> implements Stoarage<T>{....}
    ```

    