### Interface Example

##### 1. RemoteControl

<Interface 선언>

```java
package ch08_interface.sec02;

public interface IRemoteControl {
	// 상수 필드 선언
	// public, static, final 생략하더라도 자동으로 작성
	int MAX_VOLUME = 10;
	int MIN_VOLUME = 0;

	// 추상 메소드 선언
	void turnOn();

	void turnOff();

	void setVolume(int volume);

	// 디폴트 메소드 선언
	// 기본적으로 public 접근제한 : 생략하더라도 컴파일 과정에서 자동으로 붙음
	// default 반드시 붙여야 함
	default void setMute(boolean mute) {
		if (mute) {
			System.out.println("무음 처리합니다.");
		} else {
			System.out.println("무음 해제합니다.");
		}
	}

	// 정적 메소드 static
	static void changeBattery() {
		System.out.println("배터리를 교환해야 합니다");
	}
}

```

<Televis ion class>

```java
package ch08_interface.sec02;

public class Television implements IRemoteControl {
	private int volume;

	@Override
	public void turnOn() {
		System.out.println("Televisio을 켭니다");
	}

	@Override
	public void turnOff() {
		System.out.println("Televisio을 끕니다");
	}

	@Override
	public void setVolume(int volume) {
		if(volume > IRemoteControl.MAX_VOLUME) {
			this.volume = IRemoteControl.MAX_VOLUME;
	}else if(volume < IRemoteControl.MIN_VOLUME) {
		this.volume = IRemoteControl.MIN_VOLUME;
		}else {
			this.volume = volume;
		}
		System.out.println("현재 Television 볼륨 : " + this.volume);
	}

}

```

<Audi_o class>

```java
package ch08_interface.sec02;

public class Audio implements IRemoteControl {
	private int volume;
	private boolean mute;
	
	@Override
	public void turnOn() {
		System.out.println("Audio를 켭니다");
	}

	@Override
	public void turnOff() {
		System.out.println("Audio를 끕니다");
	}

	@Override
	public void setVolume(int volume) {
		if(volume > IRemoteControl.MAX_VOLUME) {
			this.volume = IRemoteControl.MAX_VOLUME;
	}else if(volume < IRemoteControl.MIN_VOLUME) {
		this.volume = IRemoteControl.MIN_VOLUME;
		}else {
			this.volume = volume;
		}
		System.out.println("현재 Audio 볼륨 : " + this.volume);
	}

	@Override
	public void setMute(boolean mute) {
		this.mute = mute;
		if (mute) {
			System.out.println("무음 처리합니다.");
		} else {
			System.out.println("무음 해제합니다.");
		}
	}

}

```

<메인 메소드로 출력>

```java
package ch08_interface.sec02;

public class IRemoteControlMain {

	public static void main(String[] args) {
		// 인터페이스 생성 예제
		// 인터페이스 변수 선언
		IRemoteControl irc = null;
		
		// Television 객체를 인터페이스 타입에 대입
		irc = new Television();
		irc.turnOn();
		irc.setVolume(10);
		irc.setMute(true);
		irc.setMute(false);
		irc.turnOff();
		System.out.println("---------------------------------------------");
		
		irc = new Audio();
		irc.turnOn();
		irc.setVolume(10);
		irc.setMute(true);
		irc.setMute(false);
		irc.turnOff();
		
		// 정적 메소드 사용
		IRemoteControl.changeBattery();
	}

}
```

##### 2. 회원가입 정보

<클래스 필드, 생성자, Get &Set 선언>

```java
package ch08_interface.sec04;

public class MemberDTO {
	
	// 필드 
	private String memName;
	private String memId;
	private String memPass;
	private String memPhone;
	private String memAddress;
	
	// 생성자
	public MemberDTO(String memName, String memId, String memPass, String memPhone, String memAddress) {
		super();
		this.memName = memName;
		this.memId = memId;
		this.memPass = memPass;
		this.memPhone = memPhone;
		this.memAddress = memAddress;
	}

	// Getter & Setter
	public String getMemName() {
		return memName;
	}

	public void setMemName(String memName) {
		this.memName = memName;
	}

	public String getMemId() {
		return memId;
	}

	public void setMemId(String memId) {
		this.memId = memId;
	}

	public String getMemPass() {
		return memPass;
	}

	public void setMemPass(String memPass) {
		this.memPass = memPass;
	}

	public String getMemPhone() {
		return memPhone;
	}

	public void setMemPhone(String memPhone) {
		this.memPhone = memPhone;
	}

	public String getMemAddress() {
		return memAddress;
	}

	public void setMemAddress(String memAddress) {
		this.memAddress = memAddress;
	}
	
	
}

```



<Interface 추상메소드 선언>

```java
package ch08_interface.sec04;

import java.util.ArrayList;

public interface IMemberDAO {
	// 추상 메소드 선언
	public void insertMember(MemberDTO dto);   // 회원 등록
	public void deleteMember(String memId);       // 회원 정보 삭제
	public ArrayList<MemberDTO> getAllMember(); // 전체 회원 정보 조회
	public void updateMember(MemberDTO dto);// 회원 정보 수정
	
}

```

<Controller class 선언>

```java
package ch08_interface.sec04;

public class MemberController {
	MemberDAO dao = new MemberDAO();
	
	// 회원 가입 데이터를 전달하면 데이터를 받아서
	// MemberDAO클래스의 insertMember 메소드에게 전달
	public void insertMember(MemberDTO dto) {
		dao.insertMember(dto);
	}
}

```

<MemberDAO를 Interface한 클래스 선언>

```java
package ch08_interface.sec04;

import java.util.ArrayList;

public class MemberDAO implements IMemberDAO {

	@Override
	public void insertMember(MemberDTO dto) {
		// DB에 등록 했다고 가정
		System.out.println("회원 등록 성공");
		System.out.println("ID : " + dto.getMemId());
		System.out.println("비밀번호 : "+dto.getMemPass());
		System.out.println("성명 : "+dto.getMemName());
		System.out.println("전화 : "+dto.getMemPhone());
		System.out.println("주소 : "+dto.getMemAddress());
	}

	@Override
	public void deleteMember(String memId) {
		// TODO Auto-generated method stub
		
	}

	@Override
	public ArrayList<MemberDTO> getAllMember() {
		// TODO Auto-generated method stub
		return null;
	}

	@Override
	public void updateMember(MemberDTO dto) {
		// TODO Auto-generated method stub
		
	}

	
}
```

<메인 메소드로 출력>

```java
package ch08_interface.sec04;

public class MemberMain {

	public static void main(String[] args) {
		// 회원 가입 정보
		MemberDTO dto = new MemberDTO("홍길동", "abcd", "1234124", "010-1234-1234", "서울시 종로구");
		
		MemberController ctrl = new MemberController();
		ctrl.insertMember(dto);
	}

}
```

##### 3. 버스인가? 택시인가? 

<Interface로 추상 메소드 선언>

```java
package ch08_interface.sec07;

public interface Vehicle {
	public void run();
}
```

<Bus class 생성>

```java
package ch08_interface.sec07;

public class Bus implements Vehicle {

	@Override
	public void run() {
		System.out.println("버스가 달립니다.");
	}

}
```

<Taxi class 생성>

```java
package ch08_interface.sec07;

public class Taxi implements Vehicle {

	@Override
	public void run() {
		System.out.println("택시가 달립니다.");
	}

}
```

<Bus, Taxi타입 받을 Driver class 생성>

```java
package ch08_interface.sec07;

public class Driver {
	
	// Vehicle인데 Bus, Taxi 타입 객체 매개변수를 받을 수 있음
	// 자동 타입 변환 : 매개변수의 다형성
	public void drive(Vehicle vehicle) {
		vehicle.run();
	}
}
```

<메인 메소드로 출력>

```java
package ch08_interface.sec07;

public class DriverMain {

	public static void main(String[] args) {
		Driver driver =new Driver();
		
		Bus bus = new Bus();
		Taxi taxi = new Taxi();
		
		// 매개변수 다형성
		driver.drive(taxi);   // 자동 타입 변환 : Vehicle vehicle = bus;
		driver.drive(bus);    // 자동 타입 변환 : Vehicle vehicle = taxi;
	}

}

```





