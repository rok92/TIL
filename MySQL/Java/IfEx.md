# If

### Alarm

```java
package practice_rok.s02;

import java.util.Scanner;

public class Alarm {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int H, M;
		System.out.print("시 입력 : ");
		H = sc.nextInt();
		
		System.out.print("분 입력 : ");
		M = sc.nextInt();
		
		if((H>=0 & H <= 23) && (M>=0 & M<=59)) {
			if(M-45 <0) {
				H -= 1;
				M = 60 + (M- 45);
			}
			else if(M-45 >=0) {
				M -= 45;
			}
			else if(H==0) {
				H = 23;
			}
			System.out.println(H +"시" + M + "분");
		}
		sc.close();
		
	}

}

```

### QuadRant

```java
package practice_rok.s02;

import java.util.Scanner;

public class QuadRant {

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int x, y;
		
		System.out.print("X값 입력 : ");
		x =sc.nextInt();
		System.out.print("y값 입력 : ");
		y = sc.nextInt();
		
		if(x > 0 && y > 0) {
			System.out.println("A"+"(" + x + "," + y + ") : " +" Quadrant 1" );
		}else if(x < 0 && y > 0) {
			System.out.println("B"+"(" + x + "," + y + ") : " +" Quadrant 2" );
		}else if(x < 0 && y < 0) {
			System.out.println("C"+"(" + x + "," + y + ") : " +" Quadrant 3" );
		}else {
			System.out.println("D"+"(" + x + "," + y + ") : " +" Quadrant 4" );
	}
		sc.close();
	}
}

```

### ForEach

```java
package practice_rok.s02;

public class ForEach {

	public static void main(String[] args) {

		int[] mark = { 70, 60, 55, 75, 95, 90, 80, 80, 85, 100 };
		int sum = 0;
		double average = 0;
		for(int i : mark) {
			sum+=i;
			average = sum / mark.length;
		}
		System.out.println(average);
	}

}

```

### Dice

```java
package practice_rok.s02;

import java.util.Random;

public class Dice {

	public static void main(String[] args) {
		int num1, num2, num3;
		int money;
		int max;
		Random r = new Random();
		num1 = r.nextInt(6)+1;
		num2 = r.nextInt(6)+1;
		num3 = r.nextInt(6)+1;
		System.out.println(num1+ ","+num2+","+num3);
		
		if((num1 == num2) & (num2==num3)) {
			money = 10000 + 3*1000;
			System.out.println(money);
		}
		else if((num1 ==num2) || (num2 == num3) || (num1 == num3)) {
			money = 1000 + 2*100;
			System.out.println(money);
		}
		else {
			if(num1>num2 && num1>num3) {
				max = num1;
			}
			else if(num2>num1 && num2 > num3) {
				max = num2; 
			}else {
				max = num3;
			}
			System.out.println(max * 100);
		}
	}

}

```

### Year

```java
package practice_rok.s02;

import java.util.Scanner;

public class Year {

	public static void main(String[] args) {

		int year;

		
		Scanner sc =new Scanner(System.in);
		System.out.print("년도 입력 : ");
		year = sc.nextInt();
		
		if(year % 4 ==0 & (year % 100 != 0 | year % 400 == 0)) {
			System.out.println("1");
		}
		else {
			System.out.println("0");
		}
		sc.close();
	}

}

```

