### switch문

> 변수 또는 연산식의 값에 따라서 실행문 선택할 때 사용한다.

```java
switch(값 또는 수식){   //(score) 또는 (score / 10)
	case 1 : 처리할 문장 - 1 break;
	case 2 : 처리할 문장 - 1 break;
	case 3 : 처리할 문장 - 1 break;
	case 4 : 처리할 문장 - 1 break;
	default : 처리할 문장 - n;
}
```

- 주의사항
  - 수식으로의 값의 결과가 정수 또는 문자열 또는 문자값이어야 한다.(실수사용 불가)
  - case뒤의 value값으로는 반드시 하나의 값만 사용되어 진다.(10<a<100과 같은 범위사용 불가)
  - case 다음에는 :(콜론)을 사용한다. ;(세미콜론)이 아니다.
  - case 띄고 value : case다음에는 띄어쓰기를 해야 한다.
  - break문이 없는 경우 case에서 실행이 멈추지 않고 다음 case 까지 수행한다.

- 예제

  - switch 1
    (숫자 입력받아 학년 표기)

    ```java
    package ch04_control._if_else.sec02switch;
    
    import java.util.Scanner;
    
    public class Switch {
    
    	public static void main(String[] args) {
    		// switch문
    		// 라인 정렬 단축기 : Ctrl +Shift + F
    
    		Scanner sc = new Scanner(System.in);
    		int year;
    
    		System.out.print("학년 입력 : ");
    		year = sc.nextInt();
    
    		switch (year) {
    			case 1:
    				System.out.println("1학년");
    				break;
    			case 2:
    				System.out.println("2학년");
    				break;
    			case 3:
    				System.out.println("3학년");
    				break;
    			case 4:
    				System.out.println("4학년");
    				break;
    			default:
    				System.out.println("잘 못 입력하였습니다");  // default문 수행 후 switch문 종료하므로 break는 사용할 필요 없다.
    		}
    		sc.close();
    	}
    
    }
    
    ```

  - switch 2

    (점수 입력받아 성적표기(A,B,C,D))

    ```java
    package ch04_control._if_else.sec02switch;
    
    import java.util.Scanner;
    
    public class SwitchEx {
    
    	public static void main(String[] args) {
    		//	다음과 같이 점수를 입력 받아서 결과를 출력하는 프로그램 작성 (switch 문 사용)
    		//	90 ~ 100 : A
    		//	80 ~ 89 : B
    		//	70 ~ 79 : C
    		//	60 ~ 69 : D
    		//	60 미만 : F
    
    		Scanner sc = new Scanner(System.in);
    		int score;
    
    		System.out.print("점수 입력 : ");
    		score = sc.nextInt();
    
    
    		switch (score / 10) {
    		case 10:
    		case 9:
    			System.out.println("학점 : A");
    			break;
    		case 8:
    			System.out.println("학점 : B");
    			break;
    		case 7:
    			System.out.println("학점 : C");
    			break;
    		case 6:
    			System.out.println("학점 : D");
    			break;
    		default:
    			System.out.println("학점 : F");
    
    			sc.close();
    		}
    	}
    
    }
    
    ```

  - switch 3(문자열 입력받아 성적 나타내기)

    ```java
    package ch04_control._if_else.sec02switch;
    
    import java.util.Scanner;
    
    public class SwitchString2 {
    
    	public static void main(String[] args) {
    		Scanner sc = new Scanner(System.in);
    		char score;
    		System.out.print("성적 입력 : ");
    		score = sc.next().charAt(0);
    		
    		switch(score) {
    		case 'A' :
    		case 'B' : System.out.println("참 잘했어요"); break;
    		case 'C' :
    		case 'D' : System.out.println("좀 더 노력하세요"); break;
    		case 'F' : System.out.println("다음 학기에 재수강 하세요"); break;
    		default : System.out.println("잘 못된 입력값입니다.");
    		
    		}
    		sc.close();
    	}
    
    }
    
    ```

    

### 반복문 for문

> 중괄호 {} 블록 내용을 반복적으로 실행할 때 사용한다.

- for

  - 반복 횟수를 알고 있을 때 주로 사용한다.

  - 반복횟수 지정 

    ```java
    for(초기식; 조건식; 증감식;){
        반복 수행되는 문장 (조건식의 결과가 true일때 사용)
    }
    ```

  - 예> 1부터 10까지 반복

    ```java
    for(int i = 1; i <= 10; i++){
        System.out.println(i);
    }
    ```

- for문 예제

  ```java
  package ch04_control._if_else.sec03for;
  
  public class For {
  
  	public static void main(String[] args) {
  		for(int i = 1; i<=10; i++) {
  			System.out.println("안녕");  //for문 안에서 선언된 i는 for문 안에서만 사용가능
  													  //for문 밖에서는 사용 불가
  		}
  		
  		System.out.println("----------------------------------------------");
  		
  		for(int j = 1; j<=10; j++) {
  			System.out.println(j);
  		}
  		System.out.println("----------------------------------------------");
  		
  		// 1부터 10까지의 합
  		int i;
  		int sum = 0;
  		for(i = 1; i<=10; i++) {
  			sum += i;
  		}
  		System.out.println("1~10합 : "+sum);
  	}
  
  }
  
  ```

  - 주의사항!!!

    - 초기값 설정시 사용하는 변수 i 

      - for문 안에서 선언하는 경우에는 for문안에서만 사용가능하다.
      - for문{}밖에서는 사용 불가

    - for문이 종료되고난 후 i의 값

      - 조건이 i <= 10일경우는

        10까지 수행되고 하나 증가한 11이 되면 조건이 맞지 않기에 for문을 빠져나오므로

        i의 최종 값은 11이 된다.

    - sum 변수 사용시 유의해야할 사항

      - int sum = 0 반드시 0값으로 초기화 한 후 사용해야만 한다.(하지 않으면 오류발생)

      - 오류발생하는 이유 : sum = sum + i

        -sum값에 i를 더해서 다시 sum값에 저장하는데 처음 sum값이 없으므로 연산수행을 할 수 없다.

        -초기화 하지 않으면 sum값에 남아있는 쓰레기 값 때문에 잘 못된 결과가 나올 수 있다.

        -때문에 반드시 초기화 하고 사용하게끔 초기화 되어있지 않으면 컴파일 오류가 뜬다

- 중첩 for문 

  >for문안에 for문 포함

  ```java
  for(int i = 1; i <= 3; i++){                  //i가 1일때 j는 5까지 수행
      for(int j = 1; j <= 3; j++)               //i가 2일때 j는 5까지 수행
          System.out.println(j + " ");          //i가 3일때 j는 5까지 수행
          
        System.out.println();  //단순 줄바꿈
  }
  ```

- for문 무한루프

  > for문의 무한반복

  - 반복문을 종료할 수의 값이 필요하다.
  - for문전에 반복문을 종료시키기 위한 변수가 필요하다.
  - for문안에서 종료되기 위한 조건이 필요하다.