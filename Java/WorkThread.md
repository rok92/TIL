
### 작업 스레드 생성과 실행

> 멀티 스레드로 실행하는 애플리케이션을 개발하려면 몇 개의 작업을 병렬로 실행할지 결정하고 
>
> 각 작업별로 스레드 생성해야 한다

- Thread 클래스를 직접 객체화해서 생성 또는 Thread를 상속해서 하위 클래스를 만들어 생성할 수 있다.

- **Thread 클래스로부터 직접 생성**

  - Runnable을 매개값으로 갖는 생성자 호출

    ```java
    Thread thread = new Thread(Runnable target);
    ```

  - Runnable은 인터페이스 타입이기 때문에 구현 객체를 만들어 대입해야 한다

  - Runnable에는 run() 메소드 하나가 정의 되어 있는데 구현 클래스는 run()을 재정의해서 작업 스레드가 실행할 코드 작성해야 한다.

    ```java
    class Task implements Runnable{
        public void run(){
            스레드가 실행할 코드;
        }
    }
    ```

  - Runnable은 작업내용을 가지고 있는 객체이며 실제 스레드는 X

  - Runnable을 통해 구현객체를 생성후 이것을 매개값으로 하여 Thread생성자를 호출하면 작업 스레드 생성이 된다

    ```java
    Runnable task = new Task();
    Thread thread = new Thread(task);
    ```

  - Thread 생성자를 호출 할 때 Runnable 익명 객체를 매개값으로 사용 가능(더 자주 쓰이는 방법)

    ```java
    Thread thread = new Thread(new Runnable(){
        public void run(){
            실행할 코드;
        }
    });
    thread.start();
    ```

  - 작업 스레드는 start() 메소드를 호출해야만 실행된다.

- **Thread 하위 클래스로부터 생성**

  - Thread의 하위 클래스로 작업스레드를 정의 하면서 작업내용 포함(Thread 상속)

  - run() 메소드를 오버라이딩(재정의)해서 스레드가 실행할 코드 작성

    ```java
    public class WorkThread extends Thread{
        @Override
        public void run(){
            실행할 코드;
        }
    }
    public static void main(String[] args){
        Thread thread = new Thread();
    }
    ```

  - 코드를 좀더 절약하기 위해 Thread 익명 객체로 작업 스레드 객체를 생성할 수 있다.

    ```java
    Thread thread = new Thread(){
        public void run(){
            실행 코드 작성;
        }
    };
    thread.start();
    ```

- **스레드의 이름**

  - 메인 스레드 이름 : main

  - 작업 스레드 이름 : Thread-n(자동설정)

    - Thread-n대신 다른 이름으로 설정하고 싶으면 setName() 메소드로 변경가능
    - Thread 의 이름을 알고 싶을 때는 getName() 메소드 호출
    - 위의 두 메소드들은 인스턴스 메소드이기 때문에 스레드 객체의 참조가 필요 
    - currentThread() : Thread의 정적 메소드로 코드를 실행하는 현재 스레드의 참조를 얻을 수 있다.

    ```java
    thread.setName("스레드이름");
    thread.getName();
    Thread thread = Thread.currentThread();
    ```

    

  