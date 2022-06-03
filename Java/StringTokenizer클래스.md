### StringTokenizer 클래스

> 문자열이 특정 구분자로 연결되어 있을 경우, 구분자를 기준으로 부분 문자열을 분리하기 위해서
>
> String의 split()메소드나 StringTokenizer클래스를 이용할 수 있다.

- split()

  - 정규 표현식을 구분자로 하여 문자열을 분리한 후 배열에 저장하고 리턴

  ```java
  String[] result = "문자열.split("정규표현식");
  ```

  - 예>

  ```java
  String text = "홍길동&박수홍,박연수,김자바-최명호";
  
  String[] names = text.split("&|,|-");
  for(String name : names){
      System.out.println(name);	//출력값 : 홍길동
      									  이수홍
                                            박연수
                                            김자바
                                            최명호
  }
  ```

- StringTokenizer 클래스

  - 문자열이 한 ㅈ종류의 구분자로 연결되어 있을 경우 손쉽게 문자열 (토큰)을 분리해 낼 수 있다.
  - 사용방법

  ```java
  StringTokenizer st = new StringTokenizer("문자열", "구분자");
  
  //예를들어
  String text = "홍길동/이수홍/박연수/김자바/최명호";
  StringTokenizer st = new StringTokenizer(text, "/");
  ```

  