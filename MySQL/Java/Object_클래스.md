### Object 클래스

> 모든 자바의 클래스들은 Object 클래스의 자식이거나 자손 클래스
>
> Object 클래스는 모든 클래스의 최상위 클래스이다.
>
> Object 클래스는 필드가 없고 메소드들로만 구성되어 있다.

- **메소드들**

  - **equals() : 객체 비교**

    - 두 객체를 동등 비교 할때 흔히 사용되어지는 메소드
    - equals() 메소드의 매개타입은 Object 즉, 모든 객체가 매개값으로 대입될 수 있다.
    - Object가 최상위 타입이므로 다른 어떠한 객체가 대입되더라도 자동타입 변환 된다.
    - 두 객체가 동일하면 true 아니면 false 리턴한다.

    ```java
    public boolean equals(Object obj){.....}
    ```

    ```java
    Object1 obj1 = new Object();
    Object1 obj2 = new Object();
    
    boolean result = obj1.equals(obj2);
    ```

    - obj1이 기준객체가 되고 (obj2)가 비교 객체가 된다
    - (obj1 == obj2)와 결과가 동일
    - **equals() 재정의**
      - 매개값(비교 객체)이 기준 객체와 동일한 타입의 객체인지 instanceof 연산자를 이용해서 확인
      - 객체 동등 비교 예>

    ```java
    public class Member{
        public String id;
        
        public Member(String id){
            this.id = id;
        }
        
        @Override
        public boolean equals(Object obj){
            if(obj instanceof Member){				// 매개값이 Member타입인지 확인
                Member member = (Member)obj;		// Member타입으로 강제 타입변환하고
                if(id.equals(member.id)){			// id필드값 동일한지 검사
                    return true;					// 동일하면 true 리턴
                }
            }	return false						//아니면 false 리턴
        }
    }
    ```

  - **hashCode() : 객체 해시코드**

    - 객체를 식별할 하나의 정수 값
    - hashCode() 메소드는 객체의 메모리 번지를 이용해서 해시코드를 만들어 리턴하기 때문에 객체마다 다른 값을 가지고 있다.
    - 논리적 동등 비교시 오버라이딩(재정의) 해야함
      - 재정의하지 않으면 필드값이 같더라도 hashCode() 메소드에서 리턴하는 해시코드가 다르기 때문에 다른 식별키로 인식하게 되어 null이 나옴
    - 비교방법
      - hashCode() 메소드 실행하여 리턴된 코드값이 같은지 비교
      - 다르면 다른 객체로 판단, 같으면 equals() 메소드로 다시 비교하여 true / false 판단
    - hashCode() 예>

    ```java
    public class Member{
        public String id;
        
        public Member(String id){
            this.id = id;
        }
        
        @Override
        public boolean equals(Object obj){
            if(obj instanceof Member){				
                Member member = (Member)obj;		
                if(id.equals(member.id)){			
                    return true;					
                }
            }	return false						
        }
        
        @Override
        public int hashCode(){				// 재정의
            return id.hashCode();			// id가 동일한 문자열인 경우 같은 해시코드 리턴
        }
    }
    ```

  - **toString() : 객체 문자 정보**

    - 객체의 문자 정보(문자열로 표현한 값)를 리턴
    - Objectd의 toString() 메소드의 리턴값은 무쓸모....
    - Object 하위 클래스는 toString() 메소드를 오버라이딩(재정의)하여 간결하고 유익한 정보를 리턴하게 되어 있다. 물론 우리가 만드는 클래스도 toString() 메소드를 재정의 하면 유용한 정보 리턴 OK
    - Object 클래스와 Date 클래스의 toString() 리턴값>

    ```java
    Object obj1 = new Object();
    Date obj2 = new Date();
    
    System.out.println(obj1);	// java.lang.Object@1b15.... : 무쓸모..
    System.out.println(obj2);	// Fri May 27 19:28:09 KST 2022 : 유용함
    ```

    - 예시> SmartPhone클래스에서 toString() 오버라딩하여 운영체제 리턴

    ```java
    public class SmartPhone{
        private String company;
        private String os;
        
        public SmpartPhone(String company, String os){
            this.company = company;
            this.os = os;
        }
        
        @Override							// toString()오버라이딩(재정의)
        public String toString(){
            return company + ", " + os;
        }
    }
    ```

    [SmartPhone 메인 출력]

    ```java
    public static void main(String[] args){
        SmartPhone p1 = new SmartPhone("애플", "IOS");
        
        String strObj = p1.toString();
        System.out.prinln(strObj);				//애플, IOS 값 출력
        
      	System.put.prinln(p1);					//애플, IOS 값 출력
        									//p1.toString()자동호출하여 리턴값 얻은후 출력
    }
    ```

  - clone() : 객체 복제

    - 원본 객체의 필드값과 동일한 값을 가지는 새로운 객체를 생성하는 것을 의미

    - 효과 : 원본 객체의 데이터를 안전하게 보관할 수 있다

    - 얕은 복제(thin clone)

      - 단순히 필드값만을 복사해서 객체를 복제하는 것
      - 필드가 기본타입일 경우 필드값 복제, 필드가 참조타입일 경우 객체의 번지수 복제
      - 이 메소드로 객체를 복제하려면 반드시 java.lang.Clonable 인터페이스를 구현하고 있어야 함
      - ClonNotSupportException 예외처리가 필요하기 때문에 try ~ catch구문이 필요

      ```java
      public class Member implements Cloneable{
      		public String id;
      		public String name;
      		public String password;
      		public int age;
      		public boolean adult;
      		
      		public Member(String id, String name, String password, int age, boolean adult) {
      			this.id = id;
      			this.name = name;
      			this.password = password;
      			this.age = age;
      			this.adult = adult;
      		}
      		
      		public Member getMember() {
      			Member cloned = null;
      			try {
      				cloned = (Member) clone();
      			} catch (CloneNotSupportedException e) {
      				
      			}return cloned;
      		}
      }
      ```

      [복제객체에 값 변경하여 출력]

      ```java
      public class MemberMain {
      
      	public static void main(String[] args) {
      		// 원본 객체 생성
      		Member original = new Member("rok92", "홍록기", "12345", 28, true);
      		
      		// 복제객체를 얻은 후 패스워드 변경
      		Member cloned = original.getMember();
      		cloned.password = "54321";			// 복제 객체에서 패스워드 변경
      		
      		//복제 객체 패스워드 값
      		System.out.println("복제 password : " + cloned.password);
      		
      		//원본 객체 패스워드 값
      		System.out.println("원본 password : " + original.password);
      	}
      
      }
      ```

      

    - 깊은 복제(deep clone)

      - 얕은 복제와 달리 참조하고 있는 객체(배열객체)도 복제 하는 것
      - Object의 clone()메소드를 오버라이딩(재정의)해서 참조 객체를 복제하는 코드를 직접 작성해야 한다.
      - 형태 
        - 배열복제 : cloned.참조변수 = Arrays.copyOf(this.참조변수, this.참조변수.length);
        - 클래스 복제 : cloned.참조변수 = new 참조객체(this.참조변수.호출할변수);
      - Car 클래스 깊은 복제 예>

      [Car 클래스 생성]

      ```java
      public class Car {				// Car클래스 생성
      	public String model;
      
      	public Car(String model) {	// 생성자
      		this.model = model;
      	}
      }
      ```

      [clone을 재정의 하여 깊은 복제]

      ```java
      import java.util.Arrays;	// Arrays.copyOf() import
      
      public class Member implements Cloneable{
      		public String name;
      		public int age;
      		public int[] scores;			// 참조 타입 필드
      		public Car car;					// 참조 타입 필드
      		public Member(String name, int age, int[] scores, Car car) {
      			this.name = name;
      			this.age = age;
      			this.scores = scores;
      			this.car = car;
      		}	
      		@Override					// 재정의(오버라이딩)
      		protected Object clone() throws CloneNotSupportedException {
      			// 먼저 얕은 복제로 name, age를 복제
      			Member cloned = (Member) super.clone();		// Object의 clone() 호출
      			// scores를 깊은 복제
      			cloned.scores = Arrays.copyOf(this.scores, this.scores.length);
      			// Car 객체 깊은 복제
      			cloned.car = new Car(this.car.model);
      			// 깊은 복제된 Member 리턴
      			return cloned;
      		}	
          	public Member getMember() {
      			Member cloned = null;
      			try {
      				cloned = (Member) clone();
      			} catch (CloneNotSupportedException e) {}
      			return cloned;
      		}
      }
      ```

      [MemberMain 메소드로 출력]

      ```java
      public class MemberMain {
      
      	public static void main(String[] args) {
      		// 원본 객체 생성
      		Member original = new Member("홍길동", 29, new int[] {90,90},  new Car("소나타"));
      		
      		// 복제객체 얻어서 참조 객체 값 변경
      		Member cloned = original.getMember();
      		cloned.scores[0] = 100;
      		cloned.car.model = "그랜저";
      		
      		// 복제된 객체의 점수, 모델 값
      		System.out.print("복제 scores : {" );
      		for(int i = 0; i < cloned.scores.length; i++) {
      			System.out.print(cloned.scores[i]);
      			System.out.print((i == (cloned.scores.length -1))?" ":",");
      		}
      		System.out.println("}");
      		System.out.println("복제 Car model : " + cloned.car.model);
      		
      		System.out.println("-----------------------");
      		// 원본 객체 점수, 모델 값
      		System.out.print("원본 scores : {" );
      		for(int i = 0; i < original.scores.length; i++) {
      			System.out.print(original.scores[i]);
      			System.out.print((i == (original.scores.length -1))?" ":",");
      		}
      		System.out.println("}");
      		System.out.println("원본 Car model : " + original.car.model);
      	}
      }
      ```

  - **finailze() : 객체 소멸자**

    - Garbage Colloector가 힙 영역에서 참조하지 않는 객체나 배열을 소멸시킬 때 실행하는 메소드
    - 기본적으로 실행 내용이 없다.
    - 중요한 데이터 저장하고 싶을 때 finalize() 를 재정의하여 사용
    - finalize() 메소드가 실행되면 번호를 출력하여 어떤 객체가 소멸되는지 확인 가능
    - System.gc()를 호출하여 쓰레기 수집기를 실행해 달라고 JVM에 요청

    

  ​			