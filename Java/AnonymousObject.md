## 익명 객체

> 익명(anonymous)객체란 이름이 없는 객체로 정의
>
> 단독으로 생성할 수 없고 클래스를 상속하거나 인터페이스를 구현해야만 생성가능

##### 1. 익명 자식 객체 생성

- 자식클래스가 재사용 되지 않고, 해당 필드와 변수의 초기값으로만 사용하는 경우에 생성

- **주의사항!!**

  - 익명 자식 객체는 하나의 실행문이므로 반드시 세미콜론(;)을 붙여야 한다

    ```java
    Parent field = new Parent(){
        /*입력값....*/
    };  // 반드시 세미콜론 붙여야 함!!!
    ```

- 부모 생성자를 호출하는 코드로 매개값은 부모 생성자의 매개변수에 맞게 입력

- 방법은 3가지가 존재

  - (1) 익명 객체 생성하여 클래스 필드에 대입

    ```java
    class A{
        Parent field = new Parent(){
            int childField;
            void childMethod(){}			// 자식클래스의 필드와 메소드
            -----------------------------------
            @Override
            void parentMethod(){}			// 부모클래스 메소드를 오버라이딩
        };
    }
    ```

  - (2) 메소드 내에 변수 선언할 때

    ```java
    class A{
        void method(){
            Parent localVar = new Parent(){
              int childField;
              void childMethod(){}			// 자식클래스의 필드와 메소드
            -----------------------------------
            @Override
            void parentMethod(){}			// 부모클래스 메소드를 오버라이딩
            };
        }
    }
    ```

  - (3) 매개변수에 익명 자식 객체 생성하여 대입

    ```java
    class A{
        void method1(Parent parent){}
        void method2(){
            method1(						// method1() 메소드 호출
        	new Parent(){					// method1() 매개값으로 익명자식 객체 대입
              int childField;
              void childMethod(){}			// 자식클래스의 필드와 메소드
            -----------------------------------
            @Override
            void parentMethod(){}			// 부모클래스 메소드를 오버라이딩
            }
        );
       }
    }
    ```

    - 익명 자식 개게에 새롭게 정의된 필드와 메소드는 익명 자식 객체 내부에서만 사용O
    - 외부에서는 필드와 메소드에 접근 X

##### 2. 익명 구현 객체 생성

- 인터페이스 타입으로 필드, 변수 선언

- 필드 초기값으로 익명 구현 객체를 생성하여 대입

  ```java
  인터페이스 필드/변수 = new 인터페이스(){
      // 인터페이스에 선언된 추상 메소드의 실체 메소드 선언
      // 필드
      // 메소드
  };
  ```

- 이 때, 인터페이스에 선언된 모든 추상메소드들의 실체 메소드를 작성해야 한다.

- 추가 필드 선언 가능하지만 실체 메소드에서만 사용 가능하고 외부에서는 사용하지 못한다.

- 예>

  ```java
  public class Anonymous {
  	// 1. 필드 초기값으로 익명 구현 객체를 생성해서 대입
  	RemoteControl  field = new RemoteControl() {
  		
  		void volumeUp() {
  			System.out.println("소리를 올립니다.");		// 선언하고
  		}
  		-------------------------------------------------------------
  		@Override
  		public void turnOn() {						// 반드시 작성해야하는 실체 메소드
  			System.out.println("TV를 켭니다.");		
  			volumeUp();								// 실체 메소드에서만 사용 가능
  		}
  		
  		@Override
  		public void turnOff() {
  			System.out.println("TV를 끕니다.");
  		}
  	};
  	
  	// 2. method1() 메소드 내에서 로컬 변수를 선언할 때
  	// 초기값으로 익명 구현 객체를 생성해서 대입
  	void method1() {
  		RemoteControl localVar = new RemoteControl() {
  			
  			void changeChannel() {
  				System.out.println("채널을 바꿉니다");
  			}
  			
  			@Override
  			public void turnOn() {
  				System.out.println("Audio를 켭니다.");
  				changeChannel();
  			}
  			
  			@Override
  			public void turnOff() {
  				System.out.println("Audio를 끕니다.");	
  			}
  		};
  		localVar.turnOn();
  		localVar.turnOff();
  	}
  	
  	void method2(RemoteControl remote) {
  		remote.turnOn();
  		remote.turnOff();
  	}
  ```

  

