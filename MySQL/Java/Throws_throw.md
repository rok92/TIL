### 예외 떠넘기기

> try ~ catch로 예외를 처리하는 것이 기본 but, 메소드를 호출한 곳으로 예외를 떠넘기기 가능
>
> throws 키워드를 사용한다.

- **throws**

  - throws 키워드는 메소드에서 처리하지 않은 예외를 떠넘기는 역할을 하며, 메소드 선언부 끝에 작성된다

  - 예외 클래스가 여러개 일 경우 쉼표(,)로 구분해서 나열한다.

    ```java
    리턴타입 메소드명(매개변수, ...) throws 예외클래스1, 예외클래스2, ...{  }
    ```

  - 위의 예시처럼 발생할 수 있는 예외를 종류별로 나열할 수도 있으나 상위 클래스인Exception만으로 모든 예외를 처리할 수 있다.

    ```java
    리턴타입 메소드명(매개변수, ...) throws Exception{  }
    ```

  - throws 키워드가 있는 메소드는 반드시!!! try 블록 내에서 호출되어야 함.

  - 예시>

    ```java
    public method1(){
        try{
            method2();
        }catch(ClassNotFoundException e){
            System.out.println("클래스가 존재하지 않습니다");
        }
    }
    public void method2() throws ClassNotFoundException{
        Class clazz = Class.forName("java.lang.String2");
    }
    ```

  - throws 키워드는 예외를 호출한 곳으로 떠넘기는 역할!!!!!

### 사용자 정의 예외와 예외 발생(throw)

> API에서 제공하는 예외 클래스만으로는 다양한 종류의 예외 표현이 어려움
>
> 잔고 부족과 같은 애플리케이션과 관련된 예외를 애플리케이션 예외라 하며 이는 개발자가 직접 정의해야함.
>
> 예외를 발생시키는 키워드

- **사용자 정의 예외 클래스 선언**

  - 사용자 정의 예외 클래스는 컴파일러가 체크하는 일반예외로 선언가능

  - 컴파일러가 체크하지 않는 실행 예외로 선언 가능

  - 사용자 정의 예외 클래스 이름은 Exception으로 끝나게!

  - 필드, 생성자, 메소드 선언 가능 But, 보통 생성자만 선언

  - 생성자는 보통 두 개 선언

    - 매개변수가 없는 기본 생성자 : public XXXException(){}

    - 예외 발생원인(예외메시지) 전달하기 위한 String타입 매개 변수를 갖는 생성자 : 

      public XXXException(String message){ super(message); }

  ```java
  public class BalanceInsufficientException extends Exception{
      public BalanceInsufficientException(){}
      public BalanceInsufficientException(String message){
          super(message);
      }
  }
  ```

  

- 예외 발생(throw)

  - throw 키워드를 사용하여 예외 발생을 시킨다

  - throws랑 혼동되지 않게 잘 사용해야 함

  - 발생시키는 방법>

    ```java
    throw new XXXException();
    throw new XXXException("메시지")
    ```

  - 예외 객체는 기본생성자 or 예외 메시지를 가지는 생성자 중 어떤것을 사용해도 OK

  - catch블록에서 예외 메시지가 필요하면 예외 메시지를 가지는 생성자 이용

  - 예외발생 코드는 try ~ catch 블록으로 예외처리 가능하나 대부분 throws로 예외떠넘기기 함

  - 예외발생throw / 떠넘기기 throws 예>

    ```java
    public class Account{
        private long balance;
        
        public Account(){}
        
        public long getBalance(){
            return balance;
        }
        public void deposit(int money){
            balance += money
        }
        public void withdraw(int money) throws BalanceInsufficientExceptoin{
            if(balance < money){
                throw new BalanceInsufficientException("잔고부족 : "+(money-balance)+"모자람");
            }
            balance -= money;
        }
    }
    ```

    ```java
    public class BalanceInsufficientException extends Exception{
        public BalanceInsufficientException(){}
        public BalanceInsufficientException(String message){
            super(message);
        }
    }
    ```

  - getMessage()

    - 예외 발생시킬 때 생성자 매개값으로 전달하여 예외 객체 내부에 저장된 메시지 리턴
    - catch 블록에서 사용

    ```java
    }catch(Exception e){
        String message = e.getMessage();
    }
    ```

  - printStackTrace()

    - 예외 발생 추적한 코드 내용을 모두 콘솔에 출력
    - 프로그램 테스트 하면서 오류 찾을때 유용하게 쓰임(개발자 전용)
    - 위에 작성한 Account 클래스 활용한 예>

    ```java
    class AccountMain{
        public static void main(String[] args){
            Account ac = new Account();
            // 예금하기
            ac.deposit(10000);
            System.out.println("예금액 : " + ac.getBalance());
            // 출금하기
            try{
                ac.withdraw(30000);
            }catch(BalanceInsufficientException e){
                String message = e.getMessage();		// 예외 메시지 얻기
                System.out.println(message);
                System.out.println();
                e.printStackTrace();					// 예외 추적 후 출력
            }
        }
    }
    ```

    