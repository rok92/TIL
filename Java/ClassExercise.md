### Class Exercise

1. 섯다 카드

   ```java
   package practice_rok.s07class;
   
   public class Sutda {
   
   		int num;
   		boolean isKwang;
   		
   		
   		public Sutda() {
   			this(1, true);
   		}
   		
   		public Sutda(int num, boolean isKwang) {
   			this.num = num;
   			this.isKwang = isKwang;
   		}
   		
   		String info() {
   			return num + (isKwang ? "K" : "");
   		}
   		
   		
   		
   	public static void main(String[] args) {
   		
   		Sutda card1 = new Sutda(3, false);
   		Sutda card2 = new Sutda();
   		
   		System.out.println(card1.info());
   		System.out.println(card2.info());
   	}
   }
   ```

2. Student 클래스에 평균과 총점을 구하시오

   ```java
   package practice_rok.s07class;
   
   import java.text.DecimalFormat;
   
   public class Student {
   
   	
   	String name;
   	int ban;
   	int no;
   	int kor;
   	int eng;
   	int math;
   	
   	public Student() {
   		
   	}
   	
   	
   
   	public Student(String name, int ban, int no, int kor, int eng, int math) {
   		this.name = name;
   		this.ban = ban;
   		this.no = no;
   		this.kor = kor;
   		this.eng = eng;
   		this.math = math;
   	}
   	
   	public String info() {
   		return name + "," + ban + "," + no + ","+kor+","+eng+","+math + ","+getTotal()+","+getAverage();
   	}
   
   
   	int getTotal() {
   		return (kor + eng + math);
   	}
   
   	float getAverage() {
   		return (int) (getTotal() / 3f * 10 + 0.5f) / 10f;
   	}
   
   	public static void main(String[] args) {
   		DecimalFormat df = new DecimalFormat("0.0");
   		Student s = new Student();
   		s.name = "홍길동";
   		s.ban = 1;
   		s.no = 1;
   		s.kor = 100;
   		s.eng = 60;
   		s.math = 76;
   		System.out.println("이름:" + s.name);
   		System.out.println("총점:" + s.getTotal());
   		System.out.println("평균:" + df.format(s.getAverage()));
   		
   		Student s1 = new Student("홍길동", 1, 1, 100, 60, 76);
   		System.out.println(s1.info());
   		
   	}
   }
   ```

3. 두 점사이의 거리를 구하시오

   ```java
   package practice_rok.s07class;
   
   public class Distance {
   	
   	// 두 점 (x,y)와 (x1,y1)간의 거리를 구한다
   	static double getDistance(int x, int y, int x1, int y1) {
   		double dx, dy;
   		dx = Math.pow(x1-x, 2.0);
   		dy = Math.pow(y1-1, 2.0);
   		double result = Math.sqrt(dy+dx);
   		return result;
   	}
   	public static void main(String[] args) {
   		System.out.println(getDistance(1,1,2,2));
   	}
   	
   }
   ```