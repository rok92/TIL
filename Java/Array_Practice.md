### Array Practice

1. 배열 arr 에 담긴 모든 값을 더하는 프로그램을 완성하시오

   ```java
   package practice_rok.s05array;
   
   public class Q5_3 {
   
   	public static void main(String[] args) {
   		
   		
   		int[]   arr   =    {10,   20,   30,    40,   50}; 
   		int sum   =    0;
   		
   		for(int i = 0; i < arr.length; i++) {
   			sum+=arr[i];
   		}
   		System.out.println(sum);
   	} 
   
   }
   
   ```

2. 2차원 배열 arr 에 담긴 모든 값의 총 합과 평균을 구하는 프로그램을 완성하시오.

   ```java
   package practice_rok.s05array;
   
   public class Q5_4 {
   
   	public static void main(String[] args) {
   		
   				int[][]   arr   =    {
   				{ 5, 5, 5, 5, 5}, {10,10,10,10,10}, {20,20,20,20,20}, {30,30,30,30,30}
   				};
   				int   total   =    0; 
   				float   average   =   0;
   				
   				for(int i = 0; i < arr.length; i++) {
   					for(int j = 0; j < arr[i].length; j++) {
   						total += arr[i][j];
   						average =(float) total /( arr[i].length*arr.length);
   				
   					}
   				}
   				System.out.println(total);
   				System.out.println(average);
   	}
   
   }
   ```

3. 다음은    1과    9사이의    중복되지    않은    숫자로    이루어진    3자리    숫자를    만들어내는    프 로그램이다.   (1)~(2)에   알맞은    코드를    넣어서    프로그램을   완성하시오.

   ```java
   package practice_rok.s05array;
   
   public class Q5_5 {
   
   	public static void main(String[] args) {
   		int[] ballArr = {1,2,3,4,5,6,7,8,9}; 
   		int[] ball3 = new int[3];
   		
   		for(int   i=0;   i<   ballArr.length;i++)   {
   			int    j   =   (int)(Math.random()    *   ballArr.length); 
   			int    tmp   =   0;
   			
   			tmp = ballArr[i];
   			ballArr[i] = ballArr[j];
   			ballArr[j] = tmp;
   		}
   		System.arraycopy(ballArr, 0, ball3, 0, 3);
   		for(int   i=0;i<ball3.length;i++)   { 
   			System.out.print(ball3[i]);
   		}
   	
   	}
   
   }
   ```

4. 다음은 거스름돈을 몇 개의 동전으로 지불할 수 있는지를 계산하는 문제이다. 변 수 money의 금액을 동전으로 바꾸었을 때 각각 몇 개의 동전이 필요한지 계산해서 출력하라. 단 가능한 한 적은 수의 동전으로 돌려주어야 한다. 프로그램을 완성하시오.

   ```java
   package practice_rok.s05array;
   
   public class Q5_6 {
   
   	public static void main(String[] args) {
   
   		int[] coinUnit = { 500, 100, 50, 10 };
   
   		int money = 2680;
   		System.out.println("money = " + money);
   		
   		for(int i = 0; i<coinUnit.length; i++) {
   			System.out.println(coinUnit[i] + "원 : " + money / coinUnit[i]);
   			money %= coinUnit[i];
   		}
   	}
   
   }
   ```

5. 커맨드라인으로부터 거슬러 줄 금액을 입력받아 계산한다. 보유한 동전의 개수로 거스름돈을 지불할 수 없으면, ‘거스름 돈이 부족합니다.’라고 출력하고 종료한다. 지불할 돈이 충분히 있으면, 거스름돈을 지불 한 만큼 가진 돈에서 빼고 남은 동전의 개수를 화면에 출력한다. (1)에 알맞은 코드를 넣 어서 프로그램을 완성하시오.

   ```java
   package practice_rok.s05array;
   
   import java.util.Scanner;
   
   public class Q5_7 {
   
   	public static void main(String[] args) {
   		Scanner sc =new Scanner(System.in);
   		int money ;
   		System.out.print("money=" );
   		money = sc.nextInt();
   		int[] coinUnit = { 500, 100, 50, 10 }; // 동전의 단위
   		int[] coin = { 5, 5, 5, 5 }; // 단위별 동전의 개수
   		
   		for (int i = 0; i < coinUnit.length; i++) {
   			int coinNum = 0;
   			
   			coinNum = money / coinUnit[i]; // 1
   			
   			if (coinNum <= 5) { // 2
   				coin[i] = coin[i] - coinNum;
   			} else {
   				coinNum = 5;
   				coin[i] = 0;
   			}
   			
   			money = money - (coinNum * coinUnit[i]); // 3
   			/*   (1)   아래의   로직에   맞게   코드를   작성하시오.
   			1.    금액(money)을   동전단위로   나눠서   필요한   동전의   개수(coinNum)를   구한다.
   			2.    배열   coin에서   coinNum만큼의   동전을   뺀다.
   			(만일   충분한   동전이   없다면   배열   coin에    있는   만큼만    뺀다.)
   			3.    금액에서   동전의   개수(coinNum)와   동전단위를   곱한    값을   뺀다. */
   			
   			
   			System.out.println(coinUnit[i] + "원  :   " + coinNum);
   		}
   		if (money > 0) {
   			System.out.println("거스름돈이   부족합니다.");
   			System.exit(0); // 프로그램을 종료한다.
   		}
   		System.out.println("=남은   동전의   개수   =");
   		for (int i = 0; i < coinUnit.length; i++) {
   			System.out.println(coinUnit[i] + "     원  :" + coin[i]);
   		}
   		sc.close();
   	}
   
   }
   ```

6. 다음은 배열 answer에 담긴 데이터를 읽고 각 숫자의 개수를 세어서 개수만큼 ‘*’ 을 찍어서 그래프를 그리는 프로그램이다. (1)~(2)에 알맞은 코드를 넣어서 완성하시오.

   ```java
   package practice_rok.s05array;
   
   public class Q5_8 {
   
   	public static void main(String[] args) {
   		int[] answer = { 1, 4, 4, 3, 1, 4, 4, 2, 1, 3, 2 };
   		int[] counter = new int[4];
   		for (int i = 0; i < answer.length; i++) {
   			//(1)
   			counter[answer[i]-1]++;
   		}
   		for (int i = 0; i < counter.length; i++) {
   			//(2)
   			System.out.print(counter[i]);
   			for(int j = 0; j < counter[i]; j++) {
   				System.out.print("*");
   			}
   			System.out.println();
   		}
   	}
   
   }
   ```

7. 주어진    배열을   시계방향으로   90도   회전시켜서   출력하는    프로그램을   완성하시오.

   ```java
   package practice_rok.s05array;
   
   public class Q5_9 {
   
   	public static void main(String[] args) {
   		char[][] star = { { '*', '*', ' ', ' ', ' ' }, { '*', '*', ' ', ' ', ' ' }, { '*', '*', '*', '*', '*' },
   				{ '*', '*', '*', '*', '*' } };
   
   		char[][] result = new char[star[0].length][star.length];
   		
   		for (int i = 0; i < star.length; i++) {
   			for (int j = 0; j < star[i].length; j++) {
   				System.out.print(star[i][j]);
   			}
   			System.out.println();
   		}
   		System.out.println();
   		for (int i = 0; i < star.length; i++) {
   			for (int j = 0; j < star[i].length; j++) {
   				result[j][star.length-i-1] = star[i][j];
   				
   				/*
   				(1)   알맞은   코드를   넣어   완성하시오. */
   			}
   		}
   		for (int i = 0; i < result.length; i++) {
   			for (int j = 0; j < result[i].length; j++) {
   				System.out.print(result[i][j]);
   			}
   			System.out.println();
   		}
   	}
   
   }
   ```

8. 다음은   알파벳과    숫자를   아래에    주어진   암호표로   암호화하는   프로그램이다. (1)에    알맞은   코드를   넣어서    완성하시오.

   ![image-20220605154239964](C:\Users\kyeon\AppData\Roaming\Typora\typora-user-images\image-20220605154239964.png)

   ```java
   package practice_rok.s05array;
   
   public class Q5_10 {
   
   	public static void main(String[] args) {
   
   		char[] abcCode = { '`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '|', '[',
   				']', '{', '}', ';', ':', ',', '.', '/' };
   
   		char[] numCode = { 'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p' };
   		String src = "abc123";
   		String result = "";
   		// 문자열 src의 문자를 charAt()으로 하나씩 읽어서 변환 후 result에 저장
   		for (int i = 0; i < src.length(); i++) {
   			char ch = src.charAt(i);
   			//(1)
   			if('a'<=ch && ch <= 'z') {
   				result += abcCode[ch -'a'];
   			}else if('0'<=ch && ch<='9'){
   				result += numCode[ch - '0'];
   			}
   		}
   		System.out.println("src : " + src);
   		System.out.println("result : " + result);
   
   	}
   
   }
   ```

9. 주어진 2차원 배열의 데이터보다 가로와 세로로 1이 더 큰 배열을 생성해서 배열 의 행과 열의 마지막 요소에 각 열과 행의 총합을 저장하고 출력하는 프로그램이다. (1) 에 알맞은 코드를 넣어서 완성하시오.

   ```java
   package practice_rok.s05array;
   
   public class Q5_11 {
   
   	public static void main(String[] args) {
   
   		int[][] score = { { 100, 100, 100 }, { 20, 20, 20 }, { 30, 30, 30 }, { 40, 40, 40 }, { 50, 50, 50 } };
   		int[][] result = new int[score.length + 1][score[0].length + 1];
   		for (int i = 0; i < score.length; i++) {
   			for (int j = 0; j < score[i].length; j++) {
   				//(1)
   				result[i][j] = score[i][j];
   				result[i][score[0].length] += result[i][j];
   				result[score.length][j] += result[i][j];
   				result[score.length][score[0].length] += result[i][j];
   				
   			}
   		}
   		for (int i = 0; i < result.length; i++) {
   			for (int j = 0; j < result[i].length; j++) {
   				System.out.printf("%4d", result[i][j]);
   			}
   			System.out.println();
   		}
   	}
   
   }
   ```

10. 단어의    글자위치를    섞어서    보여주고    원래의    단어를    맞추는    예제이다.    실행결과와 같이   동작하도록    예제의   빈    곳을   채우시오.

    ```java
    package practice_rok.s05array;
    
    import java.util.Scanner;
    
    public class Q5_13 {
    
    	public static void main(String[] args) {
    		
    		String[]   words   =   {   "television",   "computer",    "mouse",   "phone"   }; 
    		
    		Scanner   scanner   =    new   Scanner(System.in);
    		for(int   i=0;i<words.length;i++)   {
    		char[]   question   =   words[i].toCharArray();   //   String을   char[]로   변환 
    		
    		//(1)
    		for(int j = 0; j < question.length; j++) {
    			int n  = (int)(Math.random()*question.length);
    			
    			char chr = 'n';
    			chr = question[n];
    			question[n] = question[i];
    			question[i] = chr;
    		}
    		System.out.printf("Q%d.    %s의   정답을   입력하세요.>", i+1, new String (question));
    		
    		String answer = scanner.nextLine();
    		
    		// trim()으로 answer의 좌우 공백을 제거한 후, equals로 word[i]와 비교
    		
    		if(words[i].equals(answer.trim()))
    			System.out.printf("맞았습니다.%n%n");
    		else
    			System.out.printf("틀렸습니다.%n%n");
    			
    		}
    		scanner.close();
    	}
    
    }
    ```

    







