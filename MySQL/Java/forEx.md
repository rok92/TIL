## For문 연습문제들

- 연습문제 1 (1~10까지 값중 홀수의 합 출력)

  ```java
  package ch04_control._if_else.sec03for;
  
  public class ForEx1 {
  
  	public static void main(String[] args) {
  		// 1 ~ 10까지 값 중 홀수, 홀수의 합 출력
  		int i;
  		int sum = 0;
  
  		for (i = 1; i <= 10; i++) {
  			if (i % 2 == 1) {
  				System.out.println(i);
  				sum += i;
  			}
  		}
  		System.out.println("1~10홀수의 합 : " + sum);
  
  	}
  
  }
  
  ```

- 연습문제 2 (구구단의 단수를 입력 받아서 구구단 출력) -Scanner를 써야한다

  ```java
  package ch04_control._if_else.sec03for;
  
  import java.util.Scanner;
  
  public class ForEx2 {
  
  	public static void main(String[] args) {
  		
  		// 구구단의 단 수를 입력 받아서 구구단 출력
  		
  		Scanner sc = new Scanner(System.in);
  		int dan;
  		System.out.print("단수 입력 : ");
  		dan = sc.nextInt();
  		
  		
  		for(int i =1 ; i<=9; i++ ) {
  			System.out.println(dan + "x"+ i +"="+ dan *i);
  		}
  		
  		sc.close();
  
  	}
  
  }
  
  ```

- 연습문제 3 (숫자 입력받아서 시작과 끝의 숫자사이합 출력)

  ```java
  package ch04_control._if_else.sec03for;
  
  import java.util.Scanner;
  
  public class ForEx3 {
  
  	public static void main(String[] args) {
  		
  		// 다음과 같이 시작 값과 마지막 값을 입력 받아서 두 수 사이의 합(두 수 포함)을 구해서 출력
  		
  		Scanner sc = new Scanner(System.in);
  		int start, end, sum = 0;
  		
  		System.out.print("start 입력 : ");
  		start = sc.nextInt();
  		
  		System.out.print("end 입력 : ");
  		end = sc.nextInt();
  		
  		for(int i = start; i <=end; i++) {
  			sum = sum + i;
  		}
  			System.out.println(start+"~"+end+"의 합 : "+sum);
  				
  		
  		sc.close();
  	}
  
  }
  
  ```

- 연습문제 4(숫자 10개를 입력받아 입력받은 숫자가 양수, 음수, 0인지를 판별하여 갯수를 출력)

  ```java
  package ch04_control._if_else.sec03for;
  
  import java.util.Scanner;
  
  public class ForEx4 {
  
  	public static void main(String[] args) {
  		// 변수 선언 
  		// 양의 개수 저장할 변수, 음의 개수 저장할 변수, 0의 개수 저장할 변수
  		Scanner sc = new Scanner(System.in);
  		int num, pos=0, neg=0, zero=0;
  		
  		
  		// 10번 입력 : 반복문 (for 문)
  		// 입력 받은 숫자 각각에 대해 양수인지, 음수인지, 0안자 판별하고 해당 변수 증가 : if 문
  		for(int i =1; i<=10; i++) {
  			System.out.print("숫자"+ i +" 입력 : ");
  			num = sc.nextInt();
  			
  			if(num > 0) 
  				pos++;
  			else if(num < 0) 
  				neg++;
  			else  
  				zero++;
  		}
  		
  		// 각 변수의 값 출력
  		System.out.println("양의 개수  : " + pos);
  		System.out.println("음의 개수 : " + neg);
  		System.out.println("0의 개수 : " + zero);
  		
  		sc.close();		
  		
  	}
  
  }
  
  ```

- 연습문제 5(입력한 학생의 수만큼 점수를 입력받아서 평균을 출력)

  ```java
   package ch04_control._if_else.sec03for;
  
  import java.util.Scanner;
  
  public class ForEx5 {
  
  	public static void main(String[] args) {
  		
  		// 그림과 같이 입력한 학생 수만큼 점수를 입력 받아 평균을 구하여 출력
  		Scanner sc = new Scanner(System.in);
  		
  		int num, score, total = 0;
  		float average = 0;
  		System.out.print("학생수 입력 : " );
  		num = sc.nextInt();
  	
  		for(int i =1; i<=num; i++) {
  			System.out.print("학생"+i+"점수입력 : ");
  			score = sc.nextInt();
  			
  			total +=score;
  		}
  		average = total / (float)num;
  		
  		System.out.println("평균 : " + average);
  		
  		sc.close();
  			}
  				
  		}
  	
  
  
  
  ```

- 연습문제 6 중첩for(구구단 횡으로 출력)

  ```java
  package ch04_control._if_else.sec04fornested;
  
  public class ForNetedEx1 {
  
  	public static void main(String[] args) {
  		// 중첩 For 구문 연습문제
  		for(int i = 1; i < 10; i++) {  //<=를 사용하고 싶으면 9까지 범위설정하면 된다.
  			for(int dan = 2; dan < 10; dan++) {
  				System.out.print(dan + "x" + i + "=" + (i*dan) + "\t");
  			}
  			System.out.println();	//단순 줄바꿈
  		}
  	}
  
  }
  ```

  