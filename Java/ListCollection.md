### List 컬렉션

> 객체를 일렬로 늘어놓은 구조를 가지고 있는 컬렉션
>
> 인덱스로 관리하기 때문에 객체를 저장하면 자동 인덱스가 부여
>
> 인덱스로 객체를 검색, 삭제할 수 있는 기능제공(중복해서 객체 저장 가능)

- **구현 클래스**

  - ArrayList
  - Vector
  - LinkedList

- **주요 메소드**

  |   기능   |             메소드             |                       설명                       |
  | :------: | :----------------------------: | :----------------------------------------------: |
  | 객체추가 |        boolean add(E e)        |            주어진 객체를 맨 끝에 추가            |
  |          | void add(int index, E element) |           주어진 인덱스에 객체를 추가            |
  |          |   set(int index, E element)    | 주어진 인덱스에 저장된 객체를 주어진 객체로 바꿈 |
  | 객체검색 |   boolean contains(Object o)   |        주어진 객체가 저장되어있는지 여부         |
  |          |        E get(int index)        |        주어진 인덱스에 저장된 객체를 리턴        |
  |          |           isEmpty()            |             컬렉션이 비어있는지 조사             |
  |          |           int size()           |         저장되어 있는 전체 객체수를 리턴         |
  | 객체삭제 |          void clear()          |              저장된 모든 객체 삭제               |
  |          |      E remove(int index)       |        주어진 인덱스에 저장된 객체를 삭제        |
  |          |    boolean remove(Object o)    |                주어진 객체를 삭제                |

- **ArrayList**

  - List 인터페이스의 구현 클래스로 객체를 추가하면 객체가 인덱스로 관리된다

  - 저장 용량을 초과한 객체들이 들어오면 자동으로 저장 용량이 늘어난다.(기본 10개)

  - 제네릭을 사용하면 강제 타입 변환할 필요가 X

  - 객체 추가 : 인덱스 0부터 차례대로 저장

  - 객체 제가 : 제거된 객체의 바로 뒤 객체가 1씩 앞으로 당겨짐(빈번하게 삭제와 삽입이 일어나는경우 ArrayList는 사용 부적합)

  - ArrayList 생성방법

    ```java
    List<String> list = new ArrayList<String>():	// 기본 생성자 : 10개 객체 저장공간
    List<String> list = new ArrayList<String>(30);	// 용량 설정 : 30개 객체 저장공간
    ```

  - 고정된 객체들로 구성된 List 생성

    - Arrays.asList(T t)메소드 사용
    - T 타입 파라미터에 맞게 asList()의 매개값을 순차적으로 입력하거나, T[]배열을 매개값으로 주면 된다.

- **Vector**

  - ArrayList와 동일한 내부 구조

    ```java
    List<E> list = new Vector<E>();
    ```

  - 차이점은 동기화된 메소드로 구성되어 있기 때문에 멀티 스레드가 동시에 이 메소드들을 실행 할 수 X

  - **Iterator**

    - java.util 패키지의 Iterator<E> 인터페이스 요소가 순서대로 저장된 컬레션에서 요소를 순차적으로 검색할 때 사용
    - Vector<Integer> v = new Vector<Integer>();
    - Iterator<Iterator> it = it.iterator();
    - 벡터v의 요소를 순차적으로 검색하 Iterator 객체 반환

- **LinkedList**

  - List 구현 클래스로 ArrayList와 사용 방법은 동일 but 내부구조는 완전 다름

  - 인접 참조를 링크해서 체인처럼 관리(이전/다음 객체의 주소를 갖고 있음)

  - 특정 인덱스에서 객체를 추가하거나 제거하게 되면 바로 앞 뒤의 링크만 변경

  - 빈번한 객체 삭제와 삽입이 일어나는 곳에서는 ArrayList보다 좋은 성능

  - 끝에서 부터 순차적으로 추가/삭제하는 경우는 ArrayList가 빠르지만 중간에 추가 또는 삭제할 경우는 LinkeList가 훨씬 빠름

    ```java
    List<String> list = new LinkedList<String>();
    ```

    