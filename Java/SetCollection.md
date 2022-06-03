### Set 컬렉션

> 저장 순서가 유지되지 않는 컬렉션
>
> 객체 중복 저장 X, 하나의 null만 저장가능 / get() 메소드가 없음
>
> 들어갈 때의 순서와 나올 때의 순서가 다를 수 있다.

- **구현 클래스**

  - HashSet, LinkedHashSet, TreeSet

    |   기능   |           메소드           |                             설명                             |
    | :------: | :------------------------: | :----------------------------------------------------------: |
    | 객체추가 |      boolean add(E e)      | 주어진 객체를 저장, 객체가 성공적으로 저장되면 true리턴하고 중복객체이면 false 리턴 |
    | 객체검색 | boolean contains(Object o) |              주어진 객체가 저장되어 있는지 여부              |
    |          |     boolean isEmpty()      |                   컬렉션이 비어있는지 조사                   |
    |          |   Iterator<E> iterator()   |          저장된 객체를 한 번씩 가져오는 반복자 리턴          |
    |          |         int size()         |                저장되어 있는 전체 객체수 리턴                |
    | 객체삭제 |        void clear()        |                   저장된 모든 객체를 삭제                    |
    |          |  boolean remove(Object o)  |                       주어진 객체 삭제                       |

  - **반복자 Iterator**

    - iterator() 메소드를 호출하여 얻을 수 있다.

    - 하나의 객체를 가져올 때 next() 메소드 사용(true가 리턴될 때 사용)

    - hasNext() 는 가져올 객체가 있으면 true, 없으면 false 리턴

    - Iterator 메소드들

      | 리턴타입 | 메소드명  |                     설명                     |
      | :------: | :-------: | :------------------------------------------: |
      | boolean  | hasNext() | 가져올 객체가 있으면 true, 없으면 false 리턴 |
      |    E     |  next()   |       컬렉션에서 하나의 객체를 가져옴        |
      |   void   | remove()  |          Set 컬렉션에서 객체를 제거          |

- **HashSet**

  - Set 인터페이스의 구현 클래스

  - Set<E> set = new HashSet<E>();

  - 객체를 순서없이 저장하고 동일 및 동등객체는 중복저장하지 않음

  - 동등 객체 판단 방법!!!!

    - 객체 저장전 hashCode()를 호출하여 해시코드를 얻어내 저장되어있는 객체들의 해시코드와 비교하여 동일한 해시코드가 있으면 equals() 메소드로 비교함

    - true가 나오면 동일객체로 판단, 저장하지 않음

      ```java
      String name;
      int age;
      
      public Member(String name, int age){
          this.name = name;
          this.age = age;
      }
      
      @Override
      public boolean equals(Object obj){	//name과 age값 같으면 true리턴(equal재정의)
          if(obk instanceof Member){
              Member member = (Member)obj;
              return member.equals(name) && (member.age == age);
          }
          
      @Override
         public int hashCode(){
             return name.hashCode() + age;	//name과 age값 같으면 동일한 hashCode리턴
         }									// hashCode재정의
      }
      ```

      

    