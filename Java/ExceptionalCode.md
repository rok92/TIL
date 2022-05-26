### 예외 처리 코드

> 예외가 발생했을 경우 프로그램의 갑작스러운 종료를 막고, 정상 실행을 유지할 수 있도록 처리하는 코드
>
> 일반예외일 경우 코드를 발견하면 컴파일 오류를 발생시켜 예외처리 코드 작성하도록 요구
>
> 실행예외일 경우 컴파일러가 체크해 주지 않기 때문에 개발자의 경험을 바탕으로 작성해야 함.
>
> (try ~ catch ~ finally)

- try ~ catch ~ finally 블록

  - 생성자 내부와 메소드 내부에서 작성되어 일반예외, 실행예외가 발생할 경우 예외 처리를 할 수 있도록 해준다.

  - try블록 안에 예외발생 가능코드를 위치시켜줌

  - catch 블록안에 예외발생 코드를 실행시켜 예외처리 시켜줌

  - 작성 방법 

    ```java
    try{
        예외 발생 코드		// 만약 예외발생 코드가 없으면 catch블록은 건너뛰고 바로
    }catch(예외 클래스 e){	 // finally로 실행
        발생한 예외 처리
    }finally{				// 생략 가능
        항상 실행
    }
    ```

- Class.forName()

  - Class.forName() 메소드는 매개값으로 주어진 클래스가 존재하면 Class객체를 리턴

  - But, 존재하지 않으면 ClassNotFoundException 예외 발생

    - 이 예외는 일반예외이므로 컴파일러가 개발자에게 예외 처리 코드를 작성하도록 요구함.

    ```java
    public class TryCatchFinally{
        public static void main(String[] args){
            try{
                Class clazz = Class.forName(String2);		// 예외 발생
            }catch(ClassNotFoundException e){
                System.out.println("클래스가 존재하지 않습니다.");  // 예외 처리
            }
        }
    }
    ```

    - java.lang.String은 존재하지만 java.lang.String2는 존재하지 않기 때문에 ClassNotFoundException 예외가 발생한다. 
    - ClassNotFoundException 의 경우 일반예외이기 때문에 자바 컴파일러가 붉은줄로 예외 처리코드 실행을 요구하지만 NumberFormatException과 같은 실행 예외는 개발자가 찾아 처리해 주어야 함



### 다중 catch

> 예외별로 처리코드를 다르게 하기위해 사용하는 catch 블록

- 다중catch

  - try 블록 내부에 다양한 종류의 예외가 발생할 수 있는데 예외별로 예외처리 코드를 다르게 하기위해 사용

    ```java
    try{
        NumberFormatException 발생 1
            
        ArrayIndexOutOfBoundsException 발생 2
    }catch(NumberFormatException e){
        예외처리 1
    }catch(ArrayIndexOutOfBoundsException e){
        예외처리 2
    }
    ```

    - 단, catch 블록이 여러개 이지만 단 하나의 catch블록만 실행된다.
    - try에서 동시다발적으로 예외가 발생하지 않고, 하나의 예외가 발생하면 그 즉시 샐행 멈추고 catch블록으로 이동하기 때문

- catch 순서

  - 다중 catch를 작성할 때 항상 하위 클래스가 상위 클래스보다 위쪽에 작성되어야 한다

  - 하위 클래스는 상위 클래스를 상속했기 때문에 상위 클래스가 위쪽에 작성되며 하위 클래스의 블록은 실행되지 않기 때문이다.

  - 잘 못된 코드작성 예>

    ```java
    try{
        NumberFormatException 
            
        ArrayIndexOutOfBoundsException 
    }catch(Exception e){
        예외처리
    }catch(ArrayIndexOutOfBoundsException e){			// 상위클래스가 위쪽에 있음
        예외처리									 // 실행되지 않음
    }												// 따라서 두 위치가 바뀌어야 한다.
    ```

  - 하위 클래스가 먼저 작성되면 첫 번째 catch 블록을 실행하고 그 외 다른 예외가 발생하면 두 번째 블록 실행하게 된다.

- 멀티 catch

  - catch블록 안에서 여러개의 예외를 처리할 수 있도록 넣어준 기능

  - catch() 괄호 안에 처리해야 할 예외들을 |로 연결하면 된다.

  - 작성 방법 >

    ```java
    try{
        NumberFormatException or ArrayIndexOutOfBoundsException 
            
        Exception
    }catch(NumberFormatException | ArrayIndexOutOfBoundsException e){
        예외처리
    }catch(Exception){
        예외 처리
    }
    ```

    