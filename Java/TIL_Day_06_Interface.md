## 인터페이스(Interface)

> 객체의 사용 방법을 정의한 타입
>
> 클래스들이 구현해야 하는 동작을 지정하는데 사용되는 추상형
>
> 미리 정해진 규칙에 맞게 구현하도록 표준을 제시하기위해 사용
>
> 기본 설계도의 의미(규격 / 표준을 정함)

#### **1. 인터페이스의 역할**

- 개발 코드와 객체가 서로 **통신하는 접점 역할**

- 개발 코드가 인터페이스의 메소드를 호출하면 인터페이스는 개체의 메소드 호출

- 개발 코드는 객체의 내부 구조를 알 피룡 없고, **인터 페이스의 메소드만 알면 된다.**

- 개발 코드와 객체 중간에 인터페이스를 사용하는 이유

  - 개발 코드를 수정하지 않고 사용하는 객체를 변경하기 위함
  - **인터페이스는 하나의 객체가 아니라 여러 객체들과 사용이 가능하므로 어떤 객체를 사용하느냐에 따라 실행 내용과 리턴 값이 달라진다.**
  - 따라서 개발 코드 측면에서는 사용하는 객체에 따라 코드를 변경하지 않고 실행 내용과 리턴 값을 **다양화** 할 수 있다는 장점을 가지게 된다.
  - 개발 코드가 객체에 종속되지 않게 객체 교체할 수 있도록 하는 역할
  - 개발 코드 변경없이 리턴값 또는 실행 내용이 다양해 진다.**(다형성)**

- 인터페이스 특징

  - 인터페이스는 **객체를 생성할 수 없다.**
    - 구현되지 않은 **추상 메소드를 포함**하고 있기 때문
  - 객체를 생성할 수 없기 때문에 **생성자를 가질 수 없다.**
  - **인터페이스 간에 상속**되고 인터페이스를 **상속받아 클래스를 구현하면 인터페이스의 모든 추상 메소드들을 구현해야 한다.**

- **인터페이스 작성 과정**

  (1) **선언**

  - **interface** 키워드로 선언

  (2) **구현**

  - 클래스에서 인터페이스 구현
  - **implement** 키워드로 명시

  (3) 사용

  - 인터페이스에 구현된 **클래스의 객체에 대입**

  - interface : RemoteControl

  - 구현 클래스 : Television

  - ```java
    RemoteControl rc = new Television();
    ```

#### **2. 인터페이스 선언**

- 인터페이스 이름

  - **자바 식별자(변수, 메소드, 클래스)** 작성 규칙에 따라 작성

- 소스파일 생성

  - 인터페이스 이름과 대소문자가 동일한 소스 파일 생성(인터페이스명.java)
  - 컴파일러를 통해 .class 형태로 컴파일
  - 물리적 형태는 클래스와 동일(선언 방법은 다름)

- 인터페이스 선언

  - interface 키워드 사용

  - 형식 : [public] **interface** 인터페이스명{……..}

    <인터페이스 선언>

    ```java
    package ch08_interface.sec01;
    
    public interface ISmartPhone {
    	public void sendCall();
    	public void receiveCall();
    	public void sendSMS();
    	public void receiveSMS();
    }
    
    ```

    <상속받는 객체 선언 1>

    ```java
    package ch08_interface.sec01;
    
    public class SamsungPhone implements ISmartPhone{
    	String name;
    	
    	public SamsungPhone() {
    		name = "삼성";
    	}
    	
    	@Override
    	public void sendCall() {
    		System.out.println(name +"삼성폰으로 전화를 겁니다.");
    	}
    
    	@Override
    	public void receiveCall() {
    		// TODO Auto-generated method stub
    		
    	}
    
    	@Override
    	public void sendSMS() {
    		// TODO Auto-generated method stub
    		
    	}
    
    	@Override
    	public void receiveSMS() {
    		// TODO Auto-generated method stub
    		
    	}
    	
    }
    
    ```

    <상속받는 객체선언 2>

    ```java
    package ch08_interface.sec01;
    
    public class Iphone implements ISmartPhone {
    	String name;
    	
    	public Iphone() {
    		name = "아이폰";
    	}
    	
    	@Override
    	public void sendCall() {
    		System.out.println(name + "으로 전화를 겁니다.");
    	}
    
    	@Override
    	public void receiveCall() {
    		// TODO Auto-generated method stub
    
    	}
    
    	@Override
    	public void sendSMS() {
    		// TODO Auto-generated method stub
    
    	}
    
    	@Override
    	public void receiveSMS() {
    		// TODO Auto-generated method stub
    
    	}
    
    }
    
    ```

    <메인 메소드로 출력>

    ```java
    package ch08_interface.sec01;
    
    public class SmartPhoneMain {
    
    	public static void main(String[] args) {
    		ISmartPhone isp = new SamsungPhone();
    		isp.sendCall();
    		
    		ISmartPhone iip = new Iphone();
    		iip.sendCall();
    	}
    
    }
    ```

  #### **3. 인터페이스 구성 멤버**

  - **상수 필드**

    - 인터페이스는 런타임시 데이터를 저장할 수 있는 필드를 선언할 수 없다.

    - 하지만, **상수필드는 선언 가능**
      - 인터페이스에 고정된 값으로 런타임시 데이터를 바꿀 수 없다.
    - 인터페이스에 선언된 필드는 모두 public static final
      - 자동적으로 컴파일 과정에 붙음
    - **인터페이스는 인스턴스 필드는 가질 수 없음**
    - 선언과 동시에 초기값 지정
      - static{  }블록 작성 불가
    - 상수명은 대문자로 작성
      - 서로 다른 단어로 구성되어 있을 경우에는 언더바(_)로 연결

  - **추상 메소드**

    - 선언 형식
      - **(public abstract) 리턴타입 메소드명(매개변수,…….);**
    - 선언은 되어 있으나 **body가 정의되어 있지않은 메소드(중괄호{  } 없음)**
    - 객체가 가지고 있는 메소드를 설명한 것으로 **메소드명, 매개변수, 리턴 타입만 기술**
    - 실제 실행 내용은 객체(구현 객체)에 작성
      - 실체 클래스에서 메소드의 실행내용 작성
      - 오버라이딩
    - **이클립스에서 구현 클래스 생성하면서 인터페이스 지정하면 추상 메소드 자동오버라이딩 되서 생성**
    - 인터페이스에서 선언된 추상 메소드는 모두 public abstract
    - **public abstract을 생략하더라도 자동으로 컴파일 과정에서 붙게 된다**.

  - **디폴트 메소드**

    - 실행 블록을 가지고 있는 메소드

    - **default 키워드를 반드시 붙여야함**

    - 기본적으로 public 접근제한

      - 생략하더라도 컴파일 과정에서 자동으로 붙음

    - **선언 형식**

      - ```java
        (public) default 리턴타입 메소드명(매개변수, …….);{
        
        // 실행 블록이 있음
        
        }
        ```

        

    - 인터페이스에 선언되지만 사실 객체(구현 객체)가 가지고 있는 인스턴스 메소드

    - 자바 8 부터 디폴트 메소드 허용

      - 기존 인터페이스를 확장해서 새로운 기능을 추가하기 위해

  - **static 메소드(정적 메소드)**

    - static 키워드 사용

    - 디폴트 메소드와 달리 **객체 없어도** 인터페이스만으로 호출 가능한 메소드

    - 실행 블록을 가지고 있는 메소드

    - 선언 형식

      ```java
      (public) static 리턴타입 메소드명(매개변수, …..){
      
      // 실행블록이 있음
      
      }
      ```

      

  - **private 메소드**

    - 인터페이스 내에서만 사용 가능한 메소드

    - default 또는 static(정적메소드) 내에서 사용하기 위해 작성되는 메소드

    - 인터페이스를 구현클래스에서 재정의하거나 사용할 수 없다.



#### 4. 다중 인터페이스

- 다수의 인터페이스 타입으로 사용

- 다중 인터페이스를 구현할 경우 구현 클래스는 모든 인터페이스의 추상 메소드에 대해 실체 메소드를 작성해야 함./

  ```java
  public 클래스명 implements 인터페이스 A, 인터페이스 B{
  // 인터페이스 A에 선언된 추상 메소드의 실체 메소드 선언
  // 인터페이스 B에 선언된 추상 메소드의 실체 메소드 선언
  }
  ```

#### 5. 타입 변환과 다형성

- 다형성
  - 하나의 타입에 여러가지 객체 대입해서 다양한 실행 결과를 얻는 것
- 다형성 구현 기술
  - 상속 또는 인터페이스의 자동 타입 변환
  - 오버라이딩
- 다형성의 효과
  - 다양한 실행 결과를 얻을 수 있음
  - 객체를 부품화시킬 수 있어 유지보수 용이
  - 메소드의 매개변수로 효율적 사용
- 필드의 다형성
  - 상속에서와 마찬가지로 인터페이스도 다형성을 구현하는 기술 사용
  - 요즘은 상속보다는 인터페이스를 통해 다형성을 구현하는 경우가 더 많음
- 매개변수의 다형성
  - 매개변수의 타입이 인터페이스인 경우
    - 어떠한 구현 객체도 매개값으로 사용 가능
    - 구현 객체에 따라 메소드 실행 결과 다름