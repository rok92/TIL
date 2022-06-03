### Map 컬렉션

> 키(key)와 값(value)으로 구성된 Entry개게를 저장하는 구조
>
> 키와 값은 모두 객체
>
> 키는 중복저장 X, 값은 중복저장 O
>
> 기존에 저장된 키와 동일한 키로 값을 저장하면 기존의 값을 덮어쓴다.

- **구현 클래스들**

  - **HashMap**, HashTable, LinkedHashMap, TreeMap, Preoperties

- **Map 주요 메소드들**

  |   기능   |               메소드                |                             설명                             |
  | :------: | :---------------------------------: | :----------------------------------------------------------: |
  | 객체추가 |        V put(K key, V value)        | 주어진 키로 값을저장. 새로운 키일 경우 null을 리턴하고 동일한 키가 있을 경우 값을 대체하고 이전 값 리턴 |
  | 객체검색 |   boolean containsKey(Object key)   |                   주어진 키가 있는지 여부                    |
  |          | boolean containsValue(Object value) |                   주어진 값이 있는지 여부                    |
  |          |   Set<Map.Entry<K,V> setry Set()    | 키와 값의 쌍으로 구성된 모든 Map.Entry 객체를 Set에 담아 리턴 |
  |          |          V get(Object key)          |                  주어진 키가 있는 값을 리턴                  |
  |          |          boolean isEmpty()          |                  컬렉션이 비어 있는지 여부                   |
  |          |           Set<K> keySet()           |                모든 키를 Set 객체에 담아 리턴                |
  |          |             int size()              |                   저장된 키의 총 수를 리턴                   |
  |          |       Collection<V> values()        |           저장된 모든 값을 Collection에 담아서리턴           |
  | 객체삭제 |            void clear()             |                 모든 Map.Entry(키와 값) 삭제                 |
  |          |        V remove(Object key)         |     주어진 키와 일치하는 Map.Entry를 삭제하고 값을 리턴      |

  - 객체 추가는 put()메소드, 키로 객체를 찾아 올 때는 get()메소드 사용, 객체 삭제는 remove()메소드 사용

  - 저장된 전체 객체 대상으로 하나씩 얻고싶을 경우 방법 두 가지

    - (1) keySet() 메소드로 모든 키를 Set컬렉션으로 얻은 후 반복자를 통해 키 하나씩 얻고get()메소드로 값 얻기

      ```java
      Map<K,V> map = ~;
      Set<K> keySet = map.keySet();
      Iterator<K> keyIterator = keySet.iterator();
      while(leyIterator.hasNext()){
          K key = keyIterator.next();
          V value = map.get(key);
      }
      ```

      

    - (2) entrySet() 메소드로 모든 Map.Entry를 Set컬렉션으로 얻은 후 반복자를 통해 Map.Entry를 하나씩 얻고 getKey(), getValue() 메소드를 이용해 키와 값 얻기 

- **HashMap**

  - Map인터페이스를 구현한 Map컬렉션

  - HashMap을 사용할 때 hashCode()와 equals() 메소드를 재정의핵서 동등객체가 될 조건을 정해야 함

  - 동일한 키가 될 조건은 hashCode()의 리턴값이 같아야 하고 equals()메소드가 true를 리턴해야 함

  - 키타입은 String 많이 사용한다.

  - 기본타입은 사용할 수 없고 클래스 및 인터페ㅐ이스 타입만 가능

  - **HashMap생성하기 위해서는 키 타입과 값 타입을 파라미터로 주고 기본 생성자를 호출!!!!!!!**

    ```java
    Map<K, V> map = new HashMap<K, V>();
    ```

    - K : 키타입, V : 값 타입

  - 예>

    ```java
    Map<String, Integer> map = new HashMapo<String, Integer>();
    ```

    