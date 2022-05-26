### 예외 / 예외 클래스

- **예외(Exception)** - java.lang.Exception 클래스 상속

  >사용자의 잘못된 조작 또는 개발자의 잘못된 코딩으로 인해 발생하는 프로그램 오류
  >
  >오류이지만! 예외처리를 통해서 프로그램을 종료하지 않고 정상 실행 가능!
  >
  >자바에서는 예외를 클래스로 관리함
  >
  >JVM은 프로그램을 실행하는 도중 예외가 발생하면 해당 예외 클래스로 객체 생성하여 예외객체를 이용

- 두 종류(일반예외, 실행예외)가 있고 컴파일시 예외처리를 확인하는 차이가 있음

- 일반예외(Exception)

  - 자바 소스를 컴파일하는 과정에서 예외 처리 코드가 필요한지 검사(컴파일러 체크 예외라고도 부름)
  - Exception을 상속받지만 RuntimeException은 상속받지 않는 클래스

- 실행예외(RuntimeException)

  - 컴파일하는  과정에서 예외 처리 코드를 검사하지 않는 예외
  - Exception과 RuntimeException 둘다 상속 받는다.
  - JVM이 RuntimeException을 상속했는지 여부를 보고 판단하여 일반예외 / 실행예외 판단
  - 대표적인 실행예외의 종류(사실 엄청 많음....)
    - NullPointerException
    - ArrayIndexOutOfBoundsException
    - NumberFormatException
    - ClassCastException
  