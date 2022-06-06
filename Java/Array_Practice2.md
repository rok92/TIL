### array practice2

1. 점수가 평균이상인 사람 비율 구하기.

   ```java
   package practice_rok.s06array;
   
   import java.util.Scanner;
   
   public class Score {
   
   	public static void main(String[] args) {
   		Scanner sc = new Scanner(System.in);
   		int p = sc.nextInt();
   		
   		for(int i= 0; i < p; i++) {
   			int stu[] = new int[sc.nextInt()];
   			int sum = 0;
   			int average = 0;
   			int count = 0;
   			double overAver = 0.0;
   			
   			for(int j = 0; j <stu.length; j++) {
   				stu[j] = sc.nextInt();
   				sum += stu[j];
   			}
   			average = sum / (stu.length);
   			
   			for(int k = 0; k < stu.length; k++) {
   				if(stu[k]>average) {
   					count++;
   				}
   			}	
   			
   			overAver = count / stu.length * 100;
   			System.out.println(String.format("%.3f", overAver)+"%");
   		}
   		
   	}
   
   }
   ```

2. OX퀴즈 : O면 +1 X면 0점(연속된 O => 1+2+3+....)

   ```java
   package practice_rok.s06array;
   
   import java.util.Scanner;
   
   public class Quiz {
   
   	public static void main(String[] args) {
   		Scanner sc = new Scanner(System.in);
   
   		int p = sc.nextInt();
   
   		String []ox = new String[p];
   		
   		for(int i = 0; i < ox.length; i++) {
   			int sum = 0;
   			int count = 0;
   			ox[i] = sc.next();
   			
   			for (int j = 0; j < ox[i].length(); j++) {
   				if(ox[i].charAt(j) == 'o') {
   					count++;
   					sum += count;
   				}else {
   					count = 0;
   				}
   			}
   			System.out.println(sum);
   			sc.close();
   		}
   		
   	}
   
   }
   ```

3. 숫자의 개수 counting

   ```java
   package practice_rok.s06array;
   
   import java.util.Scanner;
   
   public class NumberOfNum {
   
   	public static void main(String[] args) {
   		
   		Scanner sc = new Scanner(System.in);
   
   		int arr[] = new int[10];
   		
   		int times = sc.nextInt() * sc.nextInt() * sc.nextInt();
   		
   		while(times > 0) {
   			arr[times % 10]++;
   			times /= 10;
   		}
   		System.out.println("=============================");
   		for(int i = 0; i < 10; i++)
   			System.out.println(arr[i]);
   		
   		sc.close();
   		
   	}
   
   }
   ```

4. 최댓값 최솟값 찾기

   ```java
   package practice_rok.s06array;
   
   import java.util.Scanner;
   
   public class MaxMin {
   
   	public static void main(String[] args) {
   		Scanner sc = new Scanner(System.in);
   
   		System.out.print("공간 입력 : ");
   		int num1 = sc.nextInt();
   
   		int arr[] = new int[num1];
   		int max = 0;
   		int min = 1000000;
   
   		for (int i = 0; i < arr.length; i++) {
   			System.out.print("숫자 입력 : ");
   			int num2 = sc.nextInt();
   			
   			if (num2 > max) {
   				max = num2;
   			}
   			if(num2 < min) {
   				min = num2;
   			}
   		}
   		System.out.println("최댓 값 : " + max);
   		System.out.println("최소 값 : " + min);
   		sc.close();
   
   	}
   
   }
   ```

5. 최댓값을 찾고 배열안에서 그 최댓값의 위치 구하기

   ```java
   package practice_rok.s06array;
   
   import java.util.Scanner;
   
   public class Max {
   
   	public static void main(String[] args) {
   		Scanner sc = new Scanner(System.in);
   
   		System.out.print("공간 입력 : ");
   		int num1 = sc.nextInt();
   
   		int arr[] = new int[num1];
   		int max = 0;
   		int j = 0;
   		for (int i = 0; i < arr.length; i++) {
   			System.out.print("숫자 입력 : ");
   			arr[i] = sc.nextInt();
   
   			if (max < arr[i]) {
   				max = arr[i];
   				j = i;
   			}
   		}
   		
   		System.out.println("최댓 값 : " + max);
   		System.out.println("최댓 값의 위치 : "+ (j+1));
   		sc.close();
   
   	}
   
   }
   ```

6. 나머지 구해서 서로다른 수 숫자세기

   ```java
   package practice_rok.s06array;
   
   import java.util.Scanner;
   
   public class Devide {
   
   	public static void main(String[] args) {
   
   		Scanner sc = new Scanner(System.in);
   
   		int arr[] = new int[10];
   		boolean tf;
   		int count = 0;
   		
   		System.out.println("수 입력 : ");
   		for (int i = 0; i < arr.length; i++) {
   			arr[i] = sc.nextInt() % 42;
   		}
   		for (int i = 0; i < arr.length; i++) {
   			tf = false;
   			for (int j = i + 1; j < arr.length; j++) {
   				if (arr[i] == arr[j]) {
   					tf = true;
   					break;
   				}
   			}
   			if (tf == false) {
   				count++;
   			}
   		}
   		System.out.println("서로 다른 나머지 갯수 : " + count);
   		sc.close();
   	}
   
   }
   ```

7. 평균점수 조작

   ```java
   package practice_rok.s06array;
   
   import java.util.Scanner;
   
   public class Average {
   
   	public static void main(String[] args) {
   
   		Scanner sc = new Scanner(System.in);
   		
   		int arr[] = new int[sc.nextInt()];
   		
   		double max = 0.0;
   		int sum = 0;
   		double average = 0.0;
   		
   		for(int i = 0; i < arr.length; i++) {
   			arr[i] = sc.nextInt();
   			if(arr[i] > max) {
   				max = arr[i];
   			}
   			sum += arr[i];
   			average = sum/arr.length / max * 100;
   		}
   		System.out.println(average);
   		sc.close();
   	}
   
   }
   ```

   