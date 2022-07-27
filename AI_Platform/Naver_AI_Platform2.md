### Naver AI Platform2(네이버 인공지능 플랫폼)

> - **Naver CLOVA**
> 
> - **네이버에서 개발한 인공지능 기술로 AI Service 제공**
> 
> - **API 형태로 이용 가능**
> 
> - **네이버 클라우드 플랫폼에서 이용할 수 있는 서비스**
> 
> - **Naver Cloud Platform(NCP)**

##### 음성변환 서비스

- **CLOVA Speech Recognition(CSR)**
  
  - 사람의 목소리를 인식하여 텍스트로 변환해주는 음성 인식 API 서비스
  
  - 언어별 지원 가능
    
    - Kor : 한국어
    
    - Jpn : 일본어
    
    - Chn : 중국어
    
    - Eng : 영어
  
  - 전송 : 음성 파일 전송
  
  - 응답 : 텍스트 반환(JSON 파싱)

- 진행 순서
  
  1. **API 호출 결과 출력 : Speech To Text**
     
     - STTService 클래스 추가하고 stt()메소드 추가
     
     - API 코드 복사(ClientID, Client Secret 입력)
     
     - 파일 : mp3파일 경로로 지정
     
     - 컨트롤러 : sttService 객체 사용을 위한 @Autowired 후 ("/stt")로 매핑 지정
     
     - index.jsp에 추가 후 JSON VIEWER로 형식 결과 확인
  
  2-  **JSON 결과 파싱**
     
     - jsonToString()메소드 추가 후 JSON 형태의 문자열 파싱해서 반환
       
       ```java
       //JSON 파싱
       	public String jsonToString(String jsonResultStr) {
       		
       		String result = new JSONObject(jsonResultStr).getString("text").toString();
       		
       		return result;
       ```
  
  3- 파일 업로드 / 추출한 텍스트 출력 / 오디오 플레이
     
     - @RestController에 추가
       
       ```java
       // stt
       		// 파일 업로드 / 오디오 플레이 사용
       		@RequestMapping("/stt")
       		public String stt(@RequestParam("uploadFile") MultipartFile file) throws IOException {
       			
       			String result = "";
       			
       			// 1. 파일 저장경로 설정 : 실제 서비스되는 위치(프로젝트 외부에 저장)
       			String uploadPath = "C:/upload/";
       			// 마지막에 있어야 함
       					
       			// 2. 원본파일 이름 알아오기
       			String originalFileName = file.getOriginalFilename();
       			String filePathName = uploadPath + originalFileName;
       
       			
       			// 3. 파일생성
       			File newFile = new File(filePathName); 
       			
       			// 4. 서버로 전송
       			file.transferTo(newFile);
       			
       			result = sttService.stt(filePathName);
       			
       			
       			return result;
       		}
       ```
     
     - stt.js / Ajax 사용해서 작성
       
       ```javascript
       /**
        * stt.js
        */
        
        $(document).ready(function(){
        	$('#sttForm').on('submit', function(){
        		// submit 이벤트 기본 기능 : 페이지 새로 고침
        		// 기본 기능 중단
        		event.preventDefault();
        		
        		// 폼 데이터 읽어오기
        		var formData = new FormData($('#sttForm')[0]);
        		
        		//  업로도된 파일명 알아오기
        		var fileName = $('#uploadFile').val().split("\\").pop();
        			//alert(fileName);
        		
        		
        		$.ajax({
        			type: "post",
        			url: "stt",
        			enctype: 'multipart/form-data',
        			data: formData,
        			processData: false,   // multipart 사용하기 위한 필수
        			contentType: false,
       			success: function(result){
       				
       				$('#audioBox audio').attr('src', '/audio/'+fileName);
       				
       				$('#resultBox').text(result); 
       			},
       			error: function(){
       				// 오류 있을 경우 수행되는 함수
       				alert("전송 실패");
       			}
        		}); // ajax 끝
        	}); // submit 끝
        	
        });
       ```
     
     - sttResult.jsp 추가
       
       ```html
       <%@ page language="java" contentType="text/html; charset=UTF-8"
           pageEncoding="UTF-8"%>
       <%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
       <!DOCTYPE html>
       <html>
       	<head>
       		<meta charset="UTF-8">
       		<title>Insert title here</title>
       		<script src="<c:url value='/js/jquery-3.6.0.min.js'/>"></script>
       		<script src="<c:url value='/js/stt.js'/>"></script>
       	</head>
       	<body>
       		<!-- 파일 업로드 -->
       		<h3>음성파일 추출 결과</h3>
       		<form id="sttForm" enctype="multipart/form-data">
       			파일 : <input type="file" id="uploadFile" name="uploadFile">
       			<input type="submit" value="결과확인">
       		</form>
       		<br><br>
       		
       		
       		<div id="audioBox">
       			<audio preload=”auto” controls></audio>
       		</div>
       		
       		
       		<!-- 텍스트 출력 -->
       		<h3>텍스트</h3>
       		<div id="resultBox"></div>
       	</body>
       </html>
       ```
  
  4. 결과로 받은 텍스트를 파일로 저장
     
     - 음성 파일 전달하고 텍스트 반환
     
     - 텍스트를 txt 파일로 저장(2가지 방법)
     
     - FileOutputStream / FileWriter
       
       ```java
       // 결과 텍스트를 파일로 저장 : FileOutputStream 사용
       	public void resultToFileSave(String result) {
       		try {
       			// 저장할 파일명 생성
       			String fileName = Long.valueOf(new Date().getTime()).toString();
       			OutputStream os = new FileOutputStream("C:/upload/" + "stt_"+fileName + ".txt");
       			byte[] bytes = result.getBytes();
       			os.write(bytes);
       			os.close();
       		} catch (IOException e) {
       			// TODO Auto-generated catch block
       			e.printStackTrace();
       		}
       	}
       	
       	// 결과 텍스트를 파일로 저장 : FileWirter 사용
       		public void resultToFileSave2(String result) {
       			try {
       				// 저장할 파일명 생성
       				String fileName = Long.valueOf(new Date().getTime()).toString();
       				String filePath = "C:/upload/" + "stt_"+fileName + ".txt";
       				
       				FileWriter fw = new FileWriter(filePath);
       				fw.write(result);
       				fw.close();
       				
       			} catch (IOException e) {
       				// TODO Auto-generated catch block
       				e.printStackTrace();
       			}
       		}
       ```
  
  5. 언어 선택 기능 추가
     
     - 한국어 / 영어 / 일본어 / 중국어
       
       (jsp에 select태그 추가후 name값 주기)
       
       ```html
       <%@ page language="java" contentType="text/html; charset=UTF-8"
           pageEncoding="UTF-8"%>
       <%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
       <!DOCTYPE html>
       <html>
       	<head>
       		<meta charset="UTF-8">
       		<title>Insert title here</title>
       		<script src="<c:url value='/js/jquery-3.6.0.min.js'/>"></script>
       		<script src="<c:url value='/js/stt2.js'/>"></script>
       	</head>
       	<body>
       		<!-- 파일 업로드 -->
       		<h3>음성파일 추출 결과</h3>
       		<form id="sttForm2" enctype="multipart/form-data">
       			파일 : <input type="file" id="uploadFile" name="uploadFile"><br><br>
       			<select name="lang">
       			<option value="Kor">한국어</option>
       			<option value="Eng">영어</option>
       			<option value="Jpn">일본어</option>
       			<option value="Chn">중국어</option>
       		</select>
       			<input type="submit" value="결과확인">
       		</form>
       		<br><br>
       		
       		
       		
       		<div id="audioBox">
       			<audio preload="auto" controls></audio>
       		</div>
       		
       		
       		<!-- 텍스트 출력 -->
       		<h3>텍스트</h3>
       		<div id="resultBox"></div>
       	</body>
       </html>
       ```
     
     - name값 @RestController에서 전달 받기
       
       ```java
       // 파일 업로드하고 언어 선택 후 결과 받기
       			@RequestMapping("/stt2")
       			public String sttResult(@RequestParam("uploadFile") MultipartFile file,
       									@RequestParam("lang") String lang) throws IOException {
       				
       				// 1. 파일 저장 경로 설정 : 실제 서비스 되는 위치 (프로젝트 외부에 저장)
       				String uploadPath = "C:/upload/";
       				// 마지막에 / 있어야 함
       				
       				// 2. 원본 파일 이름 알아오기
       				String originalFileName = file.getOriginalFilename();
       				String filePathName = uploadPath + originalFileName;
       				
       				// 3. 파일 생성
       				File newFile = new File(filePathName);
       				
       				// 4. 서버로 전송
       				file.transferTo(newFile);		
       				
       				String ocrList = sttService.stt2(filePathName, lang);		
       					
       				return ocrList;
       			}	
       ```
     
     - Service에서 @RequestParam으로 전달받은 String 추가해주기
       
       ```java
       // 언어 선택 추가
       	public String stt2(String filePathName, String language) {
       		String clientId = "ddez3p6gxn";             // Application Client ID";
               String clientSecret = "adOOc5eC3hHQvbP1JzMxVudYPXpaREqrfPnW1lbZ";     // Application Client Secret";
               
               String result = "";
               
               try {
                   String imgFile = filePathName;
                   File voiceFile = new File(imgFile);
       
                   //String language = "Kor";        // 언어 코드 ( Kor, Jpn, Eng, Chn )
                   String apiURL = "https://naveropenapi.apigw.ntruss.com/recog/v1/stt?lang=" + language;
                   URL url = new URL(apiURL);
       
                   HttpURLConnection conn = (HttpURLConnection)url.openConnection();
                   conn.setUseCaches(false);
                   conn.setDoOutput(true);
                   conn.setDoInput(true);
                   conn.setRequestProperty("Content-Type", "application/octet-stream");
                   conn.setRequestProperty("X-NCP-APIGW-API-KEY-ID", clientId);
                   conn.setRequestProperty("X-NCP-APIGW-API-KEY", clientSecret);
       
                   OutputStream outputStream = conn.getOutputStream();
                   FileInputStream inputStream = new FileInputStream(voiceFile);
                   byte[] buffer = new byte[4096];
                   int bytesRead = -1;
                   while ((bytesRead = inputStream.read(buffer)) != -1) {
                       outputStream.write(buffer, 0, bytesRead);
                   }
                   outputStream.flush();
                   inputStream.close();
                   BufferedReader br = null;
                   int responseCode = conn.getResponseCode();
                   if(responseCode == 200) { // 정상 호출
                       br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
                   } else {  // 오류 발생
                       System.out.println("error!!!!!!! responseCode= " + responseCode);
                       br = new BufferedReader(new InputStreamReader(conn.getInputStream()));
                   }
                   String inputLine;
       
                   if(br != null) {
                       StringBuffer response = new StringBuffer();
                       while ((inputLine = br.readLine()) != null) {
                           response.append(inputLine);
                       }
                       br.close();
                       System.out.println(response.toString());
                       
                       result = jsonToString(response.toString()); // 반환된 결과 텍스트
                      // System.out.println(result);
                       
                       // 결과를 파일로 저장
                       resultToFileSave2(result);
                   } 
               } catch (Exception e) {
                   System.out.println(e);
               }
               
               return result;
       	}
       ```
     
     - Ajax로 전달
       
       ```javascript
       
       ```
