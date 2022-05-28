### System 클래스

> 자바 프로그램은 기본적으로 운영체제에서 바로 실행되지 않고 JVM에 의해 실행된다.
>
> System 클래스를 이용하면 운영체제의 일부 기능 이용 가능
>
> 프로그램 종료, 키보드로부터 입력, 모니터로 출력, 메모리 정리 등등...
>
> System 클래스의 모든 필드와 메소드는 static!!

- **exit() : 프로그램 종료!**

  - exit() 메소드는 현재 실행하고 있는 프로세스를 강제종료 시키는 역할을 한다.

  - 매개값은 int를 지정하도록 되어 있음 : 종료 상태값!

  - if(종료상태값 == 0){"정상종료"}

    else{"비정상 종료"}

  - 어떠한 값을 줘도 종료는 실행되지만 특정값이 입력되었을 경우에만 종료하고 싶으면 자바의 보안관리자를 직접 설정하여 종료상태값을 확인하면 된다.
  - checkExit()
    - exit() 메소드가 실행되면 자동으로 실행되는 메소드
    - 만약 특정값이 입력되지 않으면 SecurityException예외를 발생시켜 System.exit()을 호출한 곳에서 예외처리 실행, 정상적으로 실행되면 JVM종료가 된다.

- **gc() : 쓰레기 수집기 실행**

  - JVM이 메모리가 부족할 때, CPU가 한가할 때 gc(Garbage Collector)를 실행하여 사용하지 않는 객체 제거하는 역할
  - gc는 개발자가 직접 코드를 실행시킬 수 없음
  - System.gc() 를 실행하면 가능한 빨리 실행해 달라고 요청은 가능

- **현재 시각 읽기(currentTimeMillis(), nanoTime())**

  - 위의 두 메소드는 컴퓨터의 시계로부터 현재 시간을 일거 밀리세컨드(1/1000초), 나노세컨드(1/10^9초)단위의 long값을 리턴한다
  - 사용법 >

  ```java
  long time1 = System.nanoTime();
  long time2 = System.currentTimeMillis();
  ```

- **시스템 프로퍼티 읽기 : getProperty()**

  - JVM이 시작할 때 자동 설정되는 시스템의 속성값
  - 시스템 프로퍼티는 키(key)와 값(value)으로 구성되어 있음
  - 키 이름을 매개값으로 받아 문자열로 리턴한다

  ```java
  String value = System.getProperty(String key);
  ```

- **환경변수 읽기 : getenv()**

  - 프로그램상의 변수가 아닌 운영체제(OS) 에서 이름(Name)과 값(Value)으로 관리되는 문자열 정보
  - 환경변수의 값이 필요할 경우 System.getenv() 메소드를 이용함.

  ```java
  String value = System.getenv(String name);
  ```

  