## 중첩 클래스와 중첩 인터페이스

> 중첩 클래스 : 클래스 내부에 선언한 클래스
>
> 중첩 인터페이스 : 클래스 내부에 선언한 인터페이스

##### 1. 중첩 클래스

- 멤버 클래스

  - 인스턴스 멤버 클래스

    - static 키워드 없이 선언된 클래스

    - 인스턴스 필드, 메소드만 선언 가능, 정적 필드, 메소드는 선언X

    - 내부 클래스를 생성하려면 외부 클래스의 객체 먼저 생성후 내부 클래스 객체를 생성해야 한다.

      ```java
      class A{
          // 인스턴스 멤버 클래스
          class B{
              B(){}   // 생성자
              int field1;  // 인스턴스 필드
              void method1(){}  // 인스턴스 메소드
          }
      }
      ```

      ```java
      A a = new A();   // 외부 클래스 객체 생성
      A.B b = a.new B();  // 내부 클래스 객체 생성
      b.field1 = 3;
      b.method1();
      ```

  - 정적 멤버 클래스

    - **static 키워드**로 선언된 클래스

    - **모든 종류의 필드와 메소드 선언 가능**

    - 정적 클래스의 객체를 생성할 때는 외부 클래스 객체생성 할 필요X

    - **외부클래스.정적클래스 변수  = new 외부클래스.정적클래스();** 이러한 형태로 생성하면 된다.

      ```java
      class A{
          // 정적 클래스 static
          class C{
              C(){}   // 생성자
              int field1;  // 인스턴스 필드
              static int field2;  //정적 필드
              void method1(){}     // 인스턴스 메소드
              static void method2(){}  // 정적 메소드
          }
      }
      ```

      ```java
      A.C c = new A.C();
      c.field1 = 3;   // 인스턴스 필드 사용할 때
      c.method1();    // 인스턴스 메소드 사용할 때
      A.C.field2 = 3; // 정적 필드 사용할 때
      A.C.method2();  // 정적 메소드 사용할 때
      ```

      

- 로컬 클래스

  - 메소드 내에서도 선언할 수 있다.

  - **접근제한자(public, private)와 static 붙일 수 X**

  - 메소드 내부에서만 사용된다.

  - **로컬 클래스의 내부에서는 인스턴스 필드와 메소드만 선언 가능, 정적 필드, 메소드는 선언X**

  - 로컬 클래스에서는 반드시 메소드 내부에서 객체 생성 후 사용해야 함.

    ```java
    void method(){
        // 로컬 클래스
        Class D{
            D(){}     // 생성자
            int field1 = 3;   // 인스턴스 필드
            void method1(){}   // 인스턴스 메소드
        }
        // 반드시 메소드 내부에서 객체 생성 후 사용
        D d = new D();
        d.field1 = 3;
        d.method1();
    }
    ```

##### 2. 중첩 클래스의 접근 제한

- 외부 필드와 메소드에서 사용제한

  - **멤버 클래스가 인스턴스 or 정적**으로 선언됨에 따라 외부클래스의 필드와 메소드에 사용제한이 생김

    ```java
    public class A{
        // 인스턴스 멤버 클래스
        class B{}
        // 정적 멤버 클래스
        static class C{}
        
        // 인스턴스 필드
        B field1 = new B();           //o
        C field2 = new C();           //o
        
        // 인스턴스 메소드
        void method1(){
            B var1 = new B();         //o
            C var2 = new C();         //o
        }
        
        // 정적 필드 초기화
        static B field3 = new B();    //x
        static C field4 = new C();    //o
        
        // 정적 메소드
        static void method2(){
            B var1 = new B();         //x
            C var2 = new C();         //o
        }
    }
    ```

- **멤버 클래스에서 사용 제한**

  - **인스턴스** 멤버 클래스 안에서는 바깥 클래스의 **모든 필드와 메소드 접근 O**

  - **정적** 멤버 클래스 안에서는 바깥 클래스의 **정적 필드와 정적 메소드에만 접근 O**

    인스턴스 필드와 메소드에는 접근X

    ```java
    public class A{
        int field1;
        void method1(){}
        
        static int field2;
        static void method2(){}
        
         // 인스턴스 멤버 클래스
        class B{
            void method(){
                field1 = 10;     // (인스턴스 필드)접근O
                method1();       // (인스턴스 메소드)접근O
                
                field2 = 10;     // (정적 필드)접근O
                method2();       // (정적 메소드)접근O
            }
        }
        // 정적 멤버 클래스
        static class C{
            void method(){
                field1 = 10;     // (인스턴스 필드)접근X
                method1();       // (인스턴스 메소드)접근X
                
                field2 = 10;     // (정적 필드)접근O
                method2();       // (정적 메소드)접근O
            }
        }
        
        
    }
    ```

- **로컬 클래스에서 사용 제한**

  - 로컬 클래스 내부에서는 외부 클래스의 필드나 메소드 제한 없이 사용 O

  - But,객체는 메소드 실행이 끝나도 **힙 메모리에 remain**, 매개변수 or 로컬변수는 **스택 메모리에서 disappear**

  - 로컬 변수 or 매개변수의 값을 로컬 클래스 내부에 Copy and Use.

    - 로컬 변수 or 매개변수의 값이 수정되어 로컬 클래스 내부에 복사해 둔 값과 달라지는 것을 방지하기위해  이 둘을 final로 선언하여 예방한다.

    - final로 따로 선언하지 안아도 내부적으로 final로 인식

      ```java
      public class Outter{
          public void method(int arg){    // final로 선언하지 않아도 final로 인식
              int localVar = 1;
              arg = 100;     // final로 선언, 재선언 불가, 오류생김
              localVar = 100; // final로 선언, 재선언 불가, 오류생김
              
              class Inner{
                  public void method(){
                      int result = arg + localVar;
                  }
              }
          }
      }
      ```

- **중첩 클래스에서 외부 클래스 참조 얻기**

  - this 키워드를 사용하여 참조얻기

  - 중첩 클래스에서 this는 객체 자신이 아니라 중첩 클래스의 객체가 참조

  - this.필드 / this.메소드() 하면 중첩 클래스의 필드와 메소드가 사용된다.

  - 사용 형태 : **외부클래스.this.필드 / 외부클래스.this.메소드();**

    ```java
    Public class Outter{
        String field = "Outter-field";    // 외부 인스턴스 필드
        
        void method(){
            System.out.println("Outter-method");   //외부 인스턴스 메소드
        }
        
        class Nested{
            String field = "Nested-field";   // 내부 인스턴스 필드
            
            void method(){  
                System.out.println("Nested-method");   // 내부 인스턴스 메소드
            }
            
            void print(){
                System.out.println(this.field);   // 중첩 객체 참조
                this.method();				// 중첩 객체 참조
                
                System.out.println(Outter.this.field);   // 외부 객체 참조
                Outter.this.method();        // 외부 객체 참조
            }
        }
    }
    ```

    

##### 3. 중첩 인터페이스

- 인터페이스와 해당 클래스의 긴밀한 관계를 맺는 구현 클래스 만들기 위해 사용

- 형태

  ```java
  class A{
      interface I{   // 중첩 인터페이스
          void method();   // 추상메소드 구현
      }
  }
  ```

- 예>

  [중첩 인터페이스 클래스 Button]

  ```java
  public class Button{
      OnClickListener listener;     // (2)인터페이스 타입 필드 선언
      
      void setOnClickListener(OnClickListener listener){  // (3)매개변수 다형성
          this.listener = listener;
      }
      
      void touch(){						//(4)구현 객체의 onClic()메소드 호출
          listener.onClick();
      }
      
      interface OnClickListener{    // (1)중첩 인터페이스 선언
          void onClick();
      }
  }
  ```

  [구현 클래스 CallListener]

  ```java
  public class CallListener implements Button.OnClickListener{  // 인터페이스 하는 방법
      @Override					// 상위 클래스의 메소드 재선언
      public void onClick(){
          System.out.println("전화를 겁니다.");
      }
  }
  ```

  [구현 클래스 MessageListener]

  ```java
  public class MessageListener implements Button.OnClickListener{  // 인터페이스 하는 방법
      @Override					// 상위 클래스의 메소드 재선언
      public void onClick(){
          System.out.println("메세지를 보냅니다.");
      }
  }
  ```

  - 여기서 onClickListener의 메소드에 Call 인가 Message인가에 따라 실행결과다 달라짐.

​	   [메인 클래스]

```java
public class ButtonMain{
    public static void main(String[] arg){
        Button btn = new Button();    // 객체 생성
        
        btn.setOnClickListener(new CallListener);
        btn.touch();    // 출력값 : 전화를 겁니다
        
        btn.setOnClickListener(new MessageListener);
         btn.touch();    // 출력값 : 메세지를 보냅니다
    }
}
```

