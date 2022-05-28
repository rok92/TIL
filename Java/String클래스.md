### String 클래스

- **String 생성자**
  - 자바의 문자열은 String 클래스의 인스턴스로 관리되며 소스상 문자열 리터럴은 String 객체로 자동생성된다. But String 클래스의 다양한 생성자를 이용하여 직접 객체를 생성 가능
  - 데이터는 보통 바이트 배열 Byte[]이므로 이것을 문자열로 변환하기 위해 사용함
  - 영어 알파벳 한 자 : 1바이트 / 다른 나라 언어 한 지 : 2바이트(운영체제마다 조금 다름)

- **String 메소드들**

  | 리턴타입 |                   메소드명(매개변수)                   |                            설명                             |
  | :------: | :----------------------------------------------------: | :---------------------------------------------------------: |
  |   char   |                   charAt(int index)                    |                   특정 위치의 문자열 리턴                   |
  | boolean  |                equals(Object anObject)                 |                       두 문자열 비교                        |
  |  byte[]  |                       getBytes()                       |                        byte[]로 리턴                        |
  |  byte[]  |               getBytes(Charset charset)                |          주어진 문자셋으로 인코딩한 byte[]로 리턴           |
  |   int    |                  indexOf(String str)                   |           문자열 내에서 주어진 문자열의 위치 리턴           |
  |   int    |                        length()                        |                       총 문자수 리턴                        |
  |  String  | replace(CharSequence target, CharSequence replacement) |    target부분을 replacement로 대치한 새로운 문자열 리턴     |
  |  String  |               substring(int beginIndex)                |     beginIndex위치에서 끝까지 잘라낸 새로운 문자열 리턴     |
  |  String  |       녀substring(int beginIndex, int endIndex)        | beginIndex위치에서 endIndex전까지 잘라낸 새로운 문자열 리턴 |
  |  String  |                     toLowerCase()                      |             알파벳 소문자로 변환한 문자열 리턴              |
  |  String  |                     toUpperCase()                      |             알파벳 대문자로 변환한 문자열 리텅              |
  |  String  |                         trim()                         |               앞 뒤 공백을 제거한 문자열 리턴               |
  |  String  |           valueOf(int i) / valueOf(double d)           |                 기본 타입값을 문자열로 리턴                 |

- **charAt() : 문자 추출**

  - 매개값으로 주어진 인덱스의 문자 리턴(0에서 문자열 길이 - 1까지의 번호) 
  - Ex> charAt(3) : 3 인덱스에 있는 문자 의미(띄어쓰기 포함이고 시작은 0부터 하므로, 4번째 위치한 문자 의미)

- **equals() : 문자열 비교**

  - 기본타입의 변수값을 비교할 때는 == 연산자를 이용 , 문자열일때는 비교는 가능하지만 원하지 않는 결과가 나올 수 있음.

  ```java
  String str1 = new String("홍길동");
  String str2 = "홍길동";
  String str3 = "홍길동";
  ```

  - 자바는 문자열 리터럴이 동일하면 동일한 String 객체를 참조함
  - str2, str3은 동일한 String 객체를 참조하지만, str1은 new 연산자로 생성된 다른 String 객체를 참조
  - 그래서 비교를 하면 다음과 같은 결과가 나온다

  ```java
  str1 == str2	// false
  str2 == str3	//true
  ```

  - == 연산자는 변수에 저장된 번지를 비교하기 때문에 위와 같은 결과

  ```java
  str1.equals(str2)	//true
  str2.equals(str3)	//true
  ```

  - equals()는 문자열만을 비교하기 때문에 위와 같은 결과

- **getBytes() : 바이트 배열로 변환**

  - 네트워크로 문자열을 전송하거나, 문자열을 암호화할 때 문자열을 바이트열로 종종 변환한다.
  - 메소드

  ```java
  byte[] bytes = "문자열".getBytes();
  byte[] bytes = "문자열".getBytes(Charset charset);
  ```

- **indexOf() : 문자열 찾기**

  - 매개값으로 주어진 문자열이 시작되는 인덱스를 리턴(만약 주어진 문자열이 포함되어 있지 않으면 -1리턴)
  - 사용하는 방법>

  ```java
  String name = "자바 프로젝트";
  int index = name.indexOf("프로젝트");
  ```

  - indexOf()는 if문에서 특정 문자열이 포함되어 있는지 여부에 따라 실행코드를 달리할 때 자주 사용

  ```java
  if(name.indexOf("자바") != -1){
      System.out.println("자바와 관련된 책이군요");
  }else{
      System.out.println("자바와 관련없는 책이군요");
  }
  ```

- **length() : 문자열 길이**

  - 문자열의 길이(문자의 수)를 리턴

  ```java
  String a = "안녕 반가워";
  int length = a.length();	// length변수에 6이 저장된다(공백을 포함한 글자수)
  ```

- **replace() : 문자열 대치**

  - replace()메소드는 첫 번째 문자열을 찾아 두 번째 매개값인 문자열로 대치한 새로운 문자열을 리턴한다.

  ```java
  String oldStr = "자바 프로그래밍";
  String newStr = oldStr.replace("자바", "Java");
  ```

- **substring() : 문자열 잘라내기**

  - 주어진 인덱스에서 문자열을 추출
  - 두 가지의 형태
    - substring(beginIndex) > 주어진 인덱스부터 끝까지 문자열 추출
    - substring(beginIndex, endIndex) > 주어진 시작과 끝 인덱스 사이의 문자열 추출

  ```java
  String ssn = "880505-1234567";
  String first = ssn.substring(0, 6);		// 출력 : 880505
  String second = ssn.substring(7);		// 출력 : 1234567
  ```

- **toLowerCase(), toUpperCase() : 알파벳 소, 대문자 변경**

  - toLowerCase() 메소드는 문자열을 모두 소문자로, toUpperCase() 메소드는 문자열을 모두 대문자로 리턴

  ```java
  String origin = "Java Programming";
  String lower = origin.toLowerCase();	// 소문자로 리턴
  String upper = origin.toUpperCase();	// 대문자로 리턴
  ```

  - 위 메소드는 대/소문자 관계없이 비교할 때 자주 사용하는데 이때 equalsIgnoreCase() 메소드를 이용
  - equalsIgnoreCase() 이용하지 않으면 대문자 / 소문자가 서로 다르기 때문에 false 발생

- **trim() : 문자열 앞뒤 공백 잘라내기**

  - trim() 메소드는 문자열의 앞뒤 공백을 제거한 새로운 문자열을 리턴
  - 단, 앞뒤의 공백만 제거할 뿐 중간의 공백은 제거하지 않는다.

  ```java
  string old = "    자바 프로그래밍    ";
  String new = old.trim();		// 출력 : 자바 프로그래밍
  ```

- **valueOf() : 문자열 변환**

  - valueOf() 메소드는 기본 타입의 값을 문자열로 변화하는 기능을 가지고 있다.
  - String 클래스에는 매개 변수의 타입별로 valueOf() 메소드가 오버로딩 되어있다

  ```java
  static String valueOf(boolean b);
  static String valueOf(char c);
  static String valueOf(int i);
  static String valueOf(long l);
  static String valueOf(double d);
  static String valueOf(float f);
  ```

  