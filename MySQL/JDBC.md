### JDBC(Java Database Connectivity)

- 다양한 종류의 관계형 데이터베이스에 접근할 때 사용하는 자바 표준 SQL 인터페이스

- 자바 프로그램이 DBMS에 접근하여 작업할 수 있게 해주는 API를 제공하는 클래스 모음

- 모든 DBMS에서 공통적으로 사용할 수 있는 인터페이스와 클래스로 구성

- 실제 구현 클래스는 각 DBMS 벤더가 구현했기 때문에 거의 모든 벤더가 JDBC 드라이버 제공

- 각 DBMS에 맞는 JDBC드라이버 사용

- **구성**

  - JDBC 인터페이스
  - JDBC드라이버

- **역할**

  - 응용프로그램과 DBMS사이에서 연결 역할
  - SQL문을 DBMS에 전달하고 그 결과값을 응용프로그램에 전달하는 역할

- **효용성**

  - 사용하는 RDBMS에 독립적인 프로그래밍이 가능
  - 쉽게 RDBMS의 교체가 가능

- **이클립스 프로젝트 생성하고 라이브러리 추가**

  - 이클립스에서 Java Project 생성 : DBTest
  - 프로젝트 이름에 대고 우클릭 Properties
  - Java Build Path
  - Libraries 탭
  - ModulePath 선택하고 [Add External JARS..] 선택
  - mysql-connector-java-8.0.29.jar 파일 찾아서 선택

- **JDBC를 이용한 연결 과정**

  - **(1) 드라이버 로드**
    - Java에서 MySQL Driver를 사용하기 위해 드라이버를 JVM에 로딩하는 과정
    - 동적으로 MySQL JDBC Driver 클래스의 객체를 생성해서 런타임시 메모리에 로딩
    - Class.forName(”com.mysql.cj.jdbc.Driver”);
  - **(2) Connection 객체 생성**
    - DriverManager 클래스의 static 메소드인 getConnection() 메소드를 이용해서 Connection 객체를 얻어옴
    - MySQL 서버 실제 연결
    - Connection 객체가 생성되면 DBMS 접속 성공
    - String url = “jdbc:mysql://localhost:3306/sqldb4?serverTimezone-UTC”;
      - jdbc:mysql: → JDBC드라이버
        - jdbc : JDBC URL의 프로토콜 이름
        - mysql: MySQL JDBC 드라이버
      - localhost → MySQL이 설치된 IP(호스트 이름)
    - String user = “root”;
    - String pwd = ‘1234”;
    - DriverManager.getConnection(url, user, pwd);
  - **(3) Statement 객체 생성**
  - **(4) SQL 문에 결과 반환이 있는 경우 ResultSet 객체 생성 (결과 획득)**
  - **(5) 쿼리 수행**
  - **(6) 모든 객체(자원) close()**
    - ResultSet
    - Statement
    - Connection (접속 종료)

- DBConnect(자바와 MySQL 연동)

  ```java
  package db3;
  
  import java.sql.Connection;
  import java.sql.DriverManager;
  import java.sql.PreparedStatement;
  import java.sql.ResultSet;
  import java.sql.SQLException;
  
  
  // DB연결 담당 클래스
  public class DBConnect {
  		// 데이터베이스 연결하고 Connection 객체 반환 메소드
  		// 호출하는 곳에서 객체 생성하지 않고 바로 메소드 호출해서 사용할 수 있도록 static 메소드로 정의
  		public static Connection getConnection() {
  			Connection con = null;
  		// DB연결
  		try {
  			// JDBC Driver 클래스의 객체 생성 런타임시 로드
  			Class.forName("com.mysql.cj.jdbc.Driver");
  
  			// 연결 url, 사용자 계정, 패스워드 문자열로 지정
  			String url = "jdbc:mysql://localhost:3306/sqldb4?serverTimezone-UTC";
  			String user = "root";
  			String pwd = "1234";
  
  			// DB 연결하기 위한 객체`
  			// DriverManger를 통해 Connection 객체 생성
  			// MySQL 서버 연결 : url, 사용자 계정, 패스워드 전송
  			con = DriverManager.getConnection(url, user, pwd);
  
  			// Connection 객체 생성되면 DB연결 성공
  			if (con != null) {
  				System.out.println("DB연결 성공");
  			}
  		} catch (Exception e) {
  			System.out.println("DB연결 실패");
  			e.printStackTrace();
  		}
  		return con;
  		
  	}
  		// 사용한 리소스 반납하는 close() 메소드 생성
  		public static void close(Connection con, PreparedStatement pstmt, ResultSet rs) {
  			
  				try {
  					if(rs!=null)rs.close();rs=null;
  					if(pstmt!=null)pstmt.close();pstmt=null;
  					if(con!=null)con.close();con=null;
  				} catch (SQLException e) {
  					// TODO Auto-generated catch block
  					e.printStackTrace();
  				}
  		}
  		
  		public static void close(Connection con, PreparedStatement pstmt) {
  			
  			try {
  				if(pstmt!=null)pstmt.close();pstmt=null;
  				if(con!=null)con.close();con=null;
  			} catch (SQLException e) {
  				// TODO Auto-generated catch block
  				e.printStackTrace();
  			}
  	}
  }
  ```

- 연결한 DB 정보 조회(SELECT)

  ```java
  package db3;
  
  import java.sql.Connection;
  import java.sql.DriverManager;
  import java.sql.PreparedStatement;
  import java.sql.ResultSet;
  import java.util.Date;
  
  public class BookSelectMain {
  
  	public static void main(String[] args) {
  		// JDBC : 도서정보 조회(SELECT수행)
  		
  		Connection con = null;
  		// (1) DB 연결
  		try {
  			// DB 연결 담당 클래스의 연결 메소드 호출해서 Connection 객체 받아옴
  			con = DBConnect.getConnection();
  			// (2)SELECT 쿼리문 작성
  			String sql = "select * from book order by bookNo";
  
  			// (3)쿼리문 전송을 위한 PreparedStatement 객체 생성
  			// Connection 인터페이스의 prepareStatement()메소드를 사용하여 객체 생성
  			PreparedStatement pstmt = con.prepareStatement(sql);
  
  			// (4)쿼리문 실행 시키고 결과 받아옴 : executeQuery() 메소드 사용
  			// 결과는 RersultSet 객체가 받아옴
  			ResultSet rs = pstmt.executeQuery(sql);
  
  			System.out.println("도서 정보 조회");
  			System.out.println("도서번호\t\t\t\t도서명\t\t\t저자\t  가격\t      발행일\t 재고\t      출판사번호");
  
  			// (5) executeQuery() 실행결과 받아온 ResultSet에서 데이터 추출
  			// ResultSet의 next()메소드를 이용해서 논리적 커서 이동하면서 다음 행 지전
  			// 다음 행이 있으면 true, 없으면 false 반환
  			// 모든 행 가져오려면 반복문(while) 사용
  			// 데이터 타입에 맞춰 getXXX() 메소드 사용
  			while (rs.next()) {
  				String bookNo = rs.getString(1);
  				String bookName = rs.getString(2);
  				String bookAuthor = rs.getString(3);
  				int bookPrice = rs.getInt(4);
  				Date bookDate = rs.getDate(5);
  				int bookStock = rs.getInt(6);
  				String pubNo = rs.getString(7);
  				// (6) 한 행씩 출력
  				System.out.format("%-10s\t%-25s\t%10s\t%6d\t%13s\t%3d\t%10s\n", bookNo, bookName, bookAuthor, bookPrice,
  						bookDate, bookStock, pubNo);
  
  			}
  			// (7) 리소스 닫기 close()
  			DBConnect.close(con, pstmt, rs);
  		} catch (Exception e) {
  			System.out.println("DB연결 실패");
  			e.printStackTrace();
  		}
  
  	}
  
  }
  ```

- 연동한 DB에 정보 등록(INSERT)

  ```JAVA
  package db3;
  
  import java.sql.Connection;
  import java.sql.DriverManager;
  import java.sql.PreparedStatement;
  
  public class BookInsertMain {
  
  	public static void main(String[] args) {
  		// JDBC : 도서정보 등록(INSERT수행)
  		Connection con = null;
  		
  		// (1) DB연결
  		try {
  			con = DBConnect.getConnection();
  			// 저장할 데이터 변수에 저장해서 사용
  			String bookNo = "1017";
  			String bookName = "알고리즘2";
  			String bookAuthor = "김철수";
  			int bookPrice = 25000;
  			String bookDate = "2202-01-05";
  			int bookStock = 10;
  			String pubNo = "1";
  			// (2) INSERT 쿼리문 작성
  			// 저장할 데이터 위치 설정 : values(?,?,?,?,?,?,?);
  			String sql = "insert into book values(?,?,?,?,?,?,?)";
  			
  			
  			// (3) sql문 values에 들어갈데이터 설정
  			// setXXX() 메소드 사용 "pstmt.setString(1, bookNo);
  			PreparedStatement pstmt = con.prepareStatement(sql);
  			pstmt.setString(1,  bookNo);
  			pstmt.setString(2, bookName);
  			pstmt.setString(3, bookAuthor);
  			pstmt.setInt(4, bookPrice);
  			pstmt.setString(5,  bookDate);
  			pstmt.setInt(6,  bookStock);
  			pstmt.setString(7,  pubNo);
  			
  			// (4) 쿼리문 실행 : executeUpdate() 실행
  			// 영향을 받은 행의 수 반환
  			// 작업완료 메세지 출력
  			// result가 0보다 크면 성공(1행이라도 영향을 받았으면 성공)
  			int result = pstmt.executeUpdate();
  			if(result > 0) {
  				System.out.println("도서 정보 등록 성공");
  			}
  			
  			// 리소스 close()
  			DBConnect.close(con, pstmt);
  			
  		} catch (Exception e) {
  			System.out.println("DB연결 실패");
  			e.printStackTrace();
  		}
  		
  	}
  
  }
  ```

- 연동한 DB의 정보 수정하기(UPDATE)

  ```JAVA
  package db3;
  
  import java.sql.Connection;
  import java.sql.PreparedStatement;
  import java.sql.SQLException;
  import java.util.Scanner;
  
  public class BookUpdateMain {
  
  	public static void main(String[] args) {
  		// JDBC : 도서정보 수정 클래스(UPDATE)
  		
  		// (1)DB연결 : DBConnect.getConnection() 호출해서 con 객체 받아옴
  		Connection con = DBConnect.getConnection();
  		
  		// (2)수정할 데이터 입력
  		Scanner sc = new Scanner(System.in);
  		
  		// 데이터 입력
  		System.out.println("도서정보 수정");
  		System.out.println("------------------------------");
  		
  		System.out.print("수정할 도서 번호 입력 : ");
  		String bookNo = sc.nextLine();
  		
  		System.out.print("도서명 입력 : ");
  		String bookName = sc.nextLine();
  		
  		System.out.print("도서저자 입력 : ");
  		String bookAuthor = sc.nextLine();
  		
  		System.out.print("도서가격 입력 : ");
  		int bookPrice = sc.nextInt();
  		
  		sc.nextLine();
  		
  		System.out.print("발행일 입력 : ");
  		String bookDate = sc.nextLine();
  		
  		
  		System.out.print("도서재고 입력 : ");
  		int bookStock = sc.nextInt();
  		
  		sc.nextLine();
  		
  		System.out.print("출간번호 입력 : ");
  		String pubNo = sc.nextLine();
  		
  		
  		// (3)쿼리문 작성 : update
  		// UPDATE테이블 SET 열이름 = 값 WHERE 조건;
  		// 주의! : 기본키인 bookNo는 수정 안함
  		
  		try {
  			String sql = "update book set bookName=?, bookAuthor=?,"
  					+"bookPrice=?, bookDate=?, bookStock=?, pubNo=? where bookNo=?";
  			
  			PreparedStatement pstmt = con.prepareStatement(sql);
  			pstmt.setString(1, bookName);
  			pstmt.setString(2, bookAuthor);
  			pstmt.setInt(3, bookPrice);
  			pstmt.setString(4,  bookDate);
  			pstmt.setInt(5,  bookStock);
  			pstmt.setString(6,  pubNo);
  			pstmt.setString(7,  bookNo);
  			
  			int result = pstmt.executeUpdate();
  			
  			if(result > 0) {
  				System.out.println("도서정보 수정 성공");
  			}
  		} catch (SQLException e) {
  			// TODO Auto-generated catch block
  			e.printStackTrace();
  		}
  		
  	}
  
  }
  ```

- 연동한 DB 정보 삭제하기(DELETE)

  ```JAVA
  package db3;
  
  import java.sql.Connection;
  import java.sql.PreparedStatement;
  import java.sql.SQLException;
  import java.util.Scanner;
  
  public class BookDeleteMain {
  
  	public static void main(String[] args) {
  		// JDBC : 도서정보 삭제 클래스(DELETE)
  		Connection con = null;
  		// (1)DB연결
  		con = DBConnect.getConnection();
  		
  		// (2)삭제할 도서 번호 입력
  		Scanner sc= new Scanner(System.in);
  		
  		System.out.println("도서정보 삭제");
  		
  		System.out.print("삭제할 도서번호 입력 : ");
  		String bookNo = sc.nextLine();
  		
  		// (3)쿼리문 작성 : DELETE
  		
  		
  		try {
  			String sql = "delete from book where bookNo=?";
  			PreparedStatement pstmt = con.prepareStatement(sql);
  			pstmt.setString(1,  bookNo);
  			
  			// (4)쿼리문 실행 : executeUpdate();
  			int result = pstmt.executeUpdate();
  			
  			if(result > 0) {
  				System.out.println("삭제 성공");
  			}
  			
  			// (5)리소스 close()
  			DBConnect.close(con, pstmt);
  			
  		} catch (SQLException e) {
  			e.printStackTrace();
  		}
  
  	}
  
  }
  ```

  