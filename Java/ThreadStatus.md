### 스레드 상태

- 스레드 객체를 생성후 start()메소드를 실행하면 실행되는 것처럼 보이지만 사실 실행대기 상태가 된다. 실행대기 상태에 있는 스레드 중 스레드 스케줄링으로 선택된 스레드가 비로소 CPU를 점유하고 run()메소드를 실행한다(Running상태)

  - 스레드 객체 생성 > (start()) > 실행대기(Runnable)  < > 실행 > 종료(이 때 실행대기(Runnable)와 실행상태 반복하면서 run()을 조금씩 실행)

  - **일시정지**

    - 실행상태에서 실행대기 상태로 가지 않고 일시정지 상태로 가기도 함(스레드가 실행될 수 없는 상태)
    - **WAITING**
      - 다른 스레드가 통지할 때까지 기다리는 상태
      - 실행중에 Object가 가지고 있는 wait() 메소드를 호출하게 되면 스레드는 일시정지 상태
      - WAITING된 스레드는 다른 스레드가 notify() 메소드를 호출해야만 실행 대기 상태로 가게 됨
      - WAITING된 스레드는 자기 스스로 또는 자동으로 실행 대기 상태로 갈 수 없고 다른 스레드가 통지를 해줘야만 실행 대기로 갈 수 있음(다른 스레드가 알려줘야만 실행 대기 상태로 갈 수 있는 상태)
    - **TIMED_WAITING**
      - 주어진 시간동안 기다리는 상태
      - sleep(시간) : 주어진 시간 동안 일시 정지 상태
      - 주어진 시간이 지나면 자동적으로 실행 대기 상태로 감
    - **BLOCKED**
      - 사용하고자 하는 객체의 락이 풀릴 때까지 기다리는 상태
      - 동기화 메소드와 동기화 블록에서 한 스레드가 동기화 메소드를 호출하고 있다면 다른 스레드는 이 동기화 메소드 호출 불가(이 때 다른 스레드는 BLOCKED된 상태)
      - 동기화 메소드를 다 실행하고 난 후 다른 스레드가 BLOCKED 상태가 해제되면서 실행 대기 상태로 되고, 다시 실행 상태가 되어 동기화 메소드를 호출할 수 있게 됨.

  - **스레드 상태를 나타내는 열거상수**

    |   상태    |   열거상수    |                          설명                          |
    | :-------: | :-----------: | :----------------------------------------------------: |
    | 객체 생성 |      NEW      | 스레드 객체가 생성. 아직 start() 가 호출되지 않은 상태 |
    | 실행 대기 |   RUNNABLE    |          실행 상태로 언제든지 갈 수 있는 상태          |
    | 일시 정지 |    WAITING    |       다른 스레드가 통지할 때까지 기다리는 상태        |
    |           | TIMED_WAITING |             주어진 시간동안 기다리는 상태              |
    |           |    BLOCKED    | 사용하고자 하는 객체의 락이 풀릴 때까지 기다리는 상태  |
    |   종료    |  TERMINATED   |                    실행을 마친 상태                    |

- **스레드 상태 제어**

  - 실행중인 스레드의 상태를 변경하는 것
  
  - 메소드를 이용하여 상태 변화시킴
  
  - 상태변화를 가져오는 메소드 종류
  
    |                            메소드                            |                             설명                             |
    | :----------------------------------------------------------: | :----------------------------------------------------------: |
    |                         interrupt()                          | 일시정지 상태의 스레드에서 InterruptedException 예외를 발생시켜, 예외처리코드(catch)에서 실행대기상태로 가거나 종료로 갈수있도록 한다 |
    |                  notify()<br />notifyAll()                   | 동기화 블록내에서 wait()메소드에 의해 일시정지 사애에 있는 스레드를 실행대기 상태로 만든다 |
    |                           resume()                           | suspend()메소드에 의해 일시 정지 상태에 있는 스레드를 실행 대기 상태로 만든다 |
    |    sleep(long millis)<br />sleep(long millis, int nanos)     | 주어진 시간동안 스레드를 일시정지 상태로 만든다. 시간이 지나면 자동적으로 실행대기 상태가 된다 |
    | join()<br />join(long millis)<br />join(ling millis, int nanos) | join()메소드를 호출한 스레드는 일시정지 상태가 된다. 실행대기 상태로 가려면 join() 메소드를 멤버로 가지는 스레드가 종료되거나, 매개값으로 주어진 시간이 지나야 한다 |
    | wait()<br />wait(long millis)<br />wait(long millis, int nanos) | 동기화 블록내에서 스레드를 일시 정지 상태로 만든다. 매개값으로 주어진 시간이 지나면 자동적으로 실행 대기 상태가 된다. 시간이 주어지지 않으면 notify(), notifyAll()에 의해 실행대기 상태로 갈 수 있다 |
    |                          suspend()                           | 스레드를 일시정지 상태로 만든다. resume() 메소드를 호출하면 다시 실행대기 상태가 된다 |
    |                           yield()                            | 실행 중에 우선순위가 동일한 다른 스레드에게 실행을 양보하고 실행대기 상태가 된다 |
    |                            stop()                            |                  스레드를 즉시 종료시킨다.                   |
  
    