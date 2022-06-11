### DB/Java Connect

- Book생성자와 getters/setters(BookDTO)

  ```java
  package dbProject;
  
  public class BookDTO {
  
  	private String bookNo;
  	private String bookTitle;
  	private String bookAuthor;
  	private int bookYear;
  	private int bookPrice;
  	private String pubName;
  	
  	public BookDTO(String bookNo, String bookTitle, String bookAuthor, int bookYear, int bookPrice, String pubName) {
  		this.bookNo = bookNo;
  		this.bookTitle = bookTitle;
  		this.bookAuthor = bookAuthor;
  		this.bookYear = bookYear;
  		this.bookPrice = bookPrice;
  		this.pubName = pubName;
  	}
  
  	public String getBookNo() {
  		return bookNo;
  	}
  
  	public void setBookNo(String bookNo) {
  		this.bookNo = bookNo;
  	}
  
  	public String getBookTitle() {
  		return bookTitle;
  	}
  
  	public void setBookTitle(String bookTitle) {
  		this.bookTitle = bookTitle;
  	}
  
  	public String getBookAuthor() {
  		return bookAuthor;
  	}
  
  	public void setBookAuthor(String bookAuthor) {
  		this.bookAuthor = bookAuthor;
  	}
  
  	public int getBookYear() {
  		return bookYear;
  	}
  
  	public void setBookYear(int bookYear) {
  		this.bookYear = bookYear;
  	}
  
  	public int getBookPrice() {
  		return bookPrice;
  	}
  
  	public void setBookPrice(int bookPrice) {
  		this.bookPrice = bookPrice;
  	}
  
  	public String getPubName() {
  		return pubName;
  	}
  
  	public void setPubName(String pubName) {
  		this.pubName = pubName;
  	}
  }
  
  ```

- DB,Java연결 BookDAO/select, insert메소드

  ```java
  package dbProject;
  
  import java.sql.Connection;
  import java.sql.DriverManager;
  import java.sql.PreparedStatement;
  import java.sql.ResultSet;
  import java.sql.SQLException;
  
  public class BookDAO {
  
  	Connection con = null;
  	PreparedStatement pstmt = null;
  	ResultSet rs = null;
  	
  	public BookDAO() {
  		try {
  			Class.forName("com.mysql.cj.jdbc.Driver");
  			
  			String url = "jdbc:mysql://localhost:3306/dbtest?serverTimezone-UTC";
  			String user = "root";
  			String pwd = "1234";
  			
  			con = DriverManager.getConnection(url, user, pwd);
  			if(con != null) {
  				System.out.println("DB연결 성공");
  			}
  		} catch (Exception e) {
  			System.out.println("DB연결 실패");
  			e.printStackTrace();
  		}
  	}
  	
  	public void inserBook(BookDTO bookDTO) {
  		try {
  			String sql = "insert into book values(?,?,?,?,?,?)";
  			pstmt = con.prepareStatement(sql);
  			pstmt.setString(1,  bookDTO.getBookNo());
  			pstmt.setString(2,  bookDTO.getBookTitle());
  			pstmt.setString(3,  bookDTO.getBookAuthor());
  			pstmt.setInt(4,  bookDTO.getBookYear());
  			pstmt.setInt(5,  bookDTO.getBookPrice());
  			pstmt.setString(6,  bookDTO.getPubName());
  			
  			int result = pstmt.executeUpdate();
  			
  			if(result >0) {
  				System.out.println("데이터 입력 성공");
  			}
  		} catch (SQLException e) {
  			System.out.println("오류발생");
  			e.printStackTrace();
  		}
  	}
  	
  	public void selectBook() {
  		try {
  			String sql = "select*from book order by bookNo";
  			pstmt = con.prepareStatement(sql);
  			
  			rs = pstmt.executeQuery(sql);
  			
  			while(rs.next()) {
  				String bookNo = rs.getString(1);
  				String bookTitle = rs.getString(2);
  				String bookAuthor = rs.getString(3);
  				int bookYear = rs.getInt(4);
  				int bookPrice = rs.getInt(5);
  				String pubName = rs.getString(6);
  				
  				System.out.format("%-8s\t%-10s\t%8s\t%6d\t%6d\t%-8s\n",bookNo, bookTitle, bookAuthor, bookYear, bookPrice, pubName);
  			}
  		} catch (SQLException e) {
  			// TODO Auto-generated catch block
  			e.printStackTrace();
  		}
  		
  	}
  }
  ```

- 데이터 입력 후 출력

  ```java
  package dbProject;
  
  public class BookMain {
  
  	public static void main(String[] args) {
  
  		BookDAO bdao = new BookDAO();
  		BookDTO bdto = new BookDTO("B004", "자바스크립트", "강길동", 2022, 28000, "멀티출판사");
  		
  		
  		bdao.inserBook(bdto);
  		bdao.selectBook();
  	}
  
  }
  ```

  