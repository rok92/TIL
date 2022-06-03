#### 추상 클래스 예제

##### 1. Animal

<추상 클래스 선언 Animal>

```java
package ch07_inheitance.sec16;

public abstract class Animal {
	public String kind;
	
	public void breathe() {
		System.out.println("숨을 쉽니다.");
	}
	
	// 추상 메소드 선언
	public abstract void sound();
	//public void sound2();                    // abstract 안 붙이면 body 없다는 오류 뜬다
}

```

<추상클래스 Animal을 상속받는 동물 객체 Dog 선언>

```java
package ch07_inheitance.sec16;

public class Dog extends Animal {
	
	public Dog(){
		this.kind = "포유류";
	}

	// 추상 메소드 오버라이딩(재정의)
	@Override
	public void sound() {
		System.out.println("멍멍");
		
	}
     	// 만일 추상 메소드를 오버라이딩 하지 않으면 오류
		// The type Dog must implement the inherited abstract method Animal.sound()
}

```

<추상클래스 Animal을 상속받는 동물 객체 Cat 선언>

```java
package ch07_inheitance.sec16;

public class Cat extends Animal {
		
	public Cat() {
		this.kind = "포유류";
	}

    // 추상 메소드 오버라이딩(재정의)
	@Override
	public void sound() {
		System.out.println("야옹");
	}

}
```

<메인 메소드로 입력값 출력>

```java
package ch07_inheitance.sec16;

public class AnimalMain {

	public static void main(String[] args) {
		// 추상 클래스 예제
		Dog dog = new Dog();
		Cat cat = new Cat();
		
		dog.sound();
		cat.sound();
		System.out.println("---------------------------------------------------------");
		
		// 추상 클래스는 new 연산자로 객체 생성 불가
		// Cannot instantiate the type Animal
		//Animal animal = new Animal();          
		
		Animal animal = null;
		animal = new Dog();
		animal.sound();
		
		animal = new Cat();
		animal.sound();
		
	}
	
	// 매개변수 자동 타입 변환 - 매개변수 다형성
	public static void animalSound(Animal animal) {
		animal.sound();  //재정의된 메소드 호출
	}

}
```

##### 2. Vehicle

<차량 기본 필드와 메소드 설정>

```java
package practice_rok.s03;

public abstract class Vehicle {
	String name;
	String cc;
	
	public Vehicle(String name, String cc) {
		this.name = name;
		this.cc = cc;
	}
	public void showInfo() {
		System.out.println("차량 모델 : " + name);
		System.out.println("배기량 : " + cc);
	}
}

```

<추상 클래스를 오버라이딩하여 객체 재선언>

```java
package practice_rok.s03;

public class Car extends Vehicle {
	
	private String km;
	
	public Car(String name, String cc, String km) {
		super(name, cc);
		this.km = km;
	}

	@Override
	public void showInfo() {
		super.showInfo();
		System.out.println("운행 거리 : "+km);
		
	}
}
```

<메인 메소드에서 출력>

```java
package practice_rok.s03;

public class CarMain {

	public static void main(String[] args) {
		Vehicle car = new Car("Avante", "2000", "5000km");
		car.showInfo();
		
	}

}
```



