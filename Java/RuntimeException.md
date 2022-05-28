### 실행예외(RuntimeException)

> 자바 컴파일러가 체크하지 않기 때문에 개발자의 경험에 의해 예외 처리 코드 삽입해야 함
>
> 중요 : 개발자가 실행예외에 대해 예외처리 코드 삽입하지 않으면 프로그램 바로 종료됨.

- **NullPointerException**

  - 자바 프로그램에서 가장 빈번하게 발생하는 실행 예외

  - 참조상태가 없는 상태(null값을 갖는 참조 변수), 객체 연산자 도트(.)를 사용했을 때 발생

  - NullPointerException이 발생하는 예>

    - data 변수가 null값을 가지고 있기때문에 String 객체를 참조하고 있지 않음.
    - 다음 라인에서 String객체의 toString(); 메소드를 호출하기 때문에 NullPointerException 발생

    ```java
    public class NullPointerException{
        public static void main(String[] args){
            String data = null;			// 참조변수가 null값을 가짐
            System.out.println(data.toString());
        }
    }
    ```

- **ArrayIndexOutOfBoundsException**

  - 배열에서 인덱스 범위를 초과하여 사용할 경우 발생하는 실행예외

  - ArrayIndexOutOfBoundsException이 발생하는 예>

    - 길이가 3인 배열 int[] arr = {1, 2, 3}을 선언했을때, 배열 항목을 지정하기위해 arr[0] ~ arr[2]까지사용 가능하다.
    - 이 때, arr[3]을 사용하게 되면 ArrayIndexOutOfBoundsException이 발생

    ```java
    public class ArrayIndexOutOfBoundsException{
         public static void main(String[] args){
             int[] arr = {1,2,3};
    		 
    		 for(int i = 0; i < 4; i++) {
    			 System.out.println(arr[i]);
    		 }
         }
    }
    ```

- **NumberFormatException**

  - 문자열로 되어있는 데이터를 숫자형으로 변경하는 경우 사용하는 실행 예외

    | 반환타입 | 메소드명(매개변수)           | 설명                                 |
    | -------- | ---------------------------- | ------------------------------------ |
    | int      | Integer.parseInt(String s)   | 주어진 문자열을 정수로 변환하여 리턴 |
    | double   | Double.parseDouble(String s) | 주어진 문자열을 실수로변환하여 리턴  |

  - Integer / Double은 Wrapper클래스라고 불린다

  - 위 표와 같이 parse.XXX() 메소드를 이용하면 문자열을 숫자로 변환 가능

  - 주의!!!!

    - 문자열 안에 숫자로 변환될 수 없는 문자가 섞여있으면 NumberFormatException 발생

  - NumberFormatException 예>

    - String data1 = "100";  /  String data2 = "a200"  일때 data1의 경우는 문자열 안 형태가 숫자라서 숫자형태로 변환이 가능하나, data2의 경우에는 a라는 문자가 함께 있어 NumberFormatException 예외를 발생시킨다.

    ```java
    public class NumberFormatException{
        public static void main(String[] args){
            String data1 = "100";
            String data2 = "a200";
            
            int value1 = Integer.parseInt(data1);		// 예외발생 X
            int value2 = Integer.parseInt(data2);		//NumberFormatException예외 발생
            
            int result = value1 + value2;
            System.out.println(data1+"+"+data2+"="+result);
        }
    }
    ```

- **ClassCastException**

  - 타입변환은 상위 클래스와 하위 클래스간에 발생하고 구현 클래스와 인터페이스 간에 발생한다.

  - 타입 변환하는 과정에서 억지로 타입 변환을 시도 했을 때 발생하는 실행예외

  - 올바른 타입변환 : 자식타입에서 부모타입으로 즉, 하위 클래스에서 상위 클래스로 타입변환(자동타입변환)

  - 올바르지 못한 타입 변환 : 대입된 객체가 아닌 다른 클래스로 타입변환하였을 때(ClassCastException)

  - 항상 instanceof 연산자로 타입 변환이 가능한지 확인해야 한다.

    ```java
    package ch10_exception.sec01;
    
    class Animal{}
    class Dog extends Animal{}
    class Cat extends Animal{}
    public class ClassCastExceptionEx {
    	public static void main(String[] args) {
    		Dog dog = new Dog();
            changeDog(dog);
    		
    		Cat cat = new Cat();
    		changeCat(cat);
    	}
    	public static void changeDog(Animal animal) {
    		// instanceof 연산자 사용해서 타입 확인
    		if(animal instanceof Dog) {
    		Dog dog = (Dog)animal;
    		}
    		// 강제 타입 변환 : 이전에 자동 타입 변환된 것이 아니면 ClssCastException발생
    	}
    }
    
    ```
    

  
