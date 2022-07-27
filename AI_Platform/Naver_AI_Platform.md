### Naver AI Platform(네이버 인공지능 플랫폼)

> - **Naver CLOVA**
> 
> - **네이버에서 개발한 인공지능 기술로 AI Service 제공**
> 
> - **API 형태로 이용 가능**
> 
> - **네이버 클라우드 플랫폼에서 이용할 수 있는 서비스**
> 
> - **Naver Cloud Platform(NCP)**

##### Naver AI API 서비스

- **CLOVA Face Recognition(CFR) -> 얼굴인식 / 유명인 얼굴인식**
  
  - 이미지 속의 얼굴을 감지하고 인식하여 얻은 다양한 정보를 제공하는 API 서비스
  
  - 입력된 비전 데이터(이미지 파일)를 통해 얼굴을 인식하거나 감지
  
  - 유명얼굴 인식 : 닮은 유명인 이름, 닮은 정도
  
  - 얼굴감지
    
    - 감지된 얼굴을 분석한 정보
    
    - 성별, 추정 나이, 감정, 얼굴 방향 등

- **CLOVA OCR(Optical Character Recognition)**
  
  - 광학 문자 인식 API 서비스
  
  - 사진(이미지) 속에서 텍스트 정보를 찾고 의미를 판별하는 기술
  
  - 언어와 이미지 데이터를 입려 받고, 그에 맞는 인식 결과를 텍스트로 변환
  
  - 텍스트 : 이미지 내에서 텍스트를 추출 반환
  
  - 영수증 : 영수증을 읽어서 추출항목 반환
  
  - API 사용 방법
    
    - 이미지 파일 전송하고 텍스트 반환 받아서 JSON 파싱해서 사용
  
  - 일반적 활용 사례
    
    - 문서파일 / 인쇄물 판독
    
    - 우편번호 추출을 통한 우편물 관리
    
    - 문자 자동 번역
    
    - 명함관리
    
    - 차량번호 자동 인식

- **CLOVA Speech Recognition(CSR)**
  
  - 음성 합성 API 서비스
  
  - 텍스트를 음성으로 변환
  
  - TTS (Text-to-Speech)
  
  - 텍스트 파일을 입력받아서 변환된 음성 파일 반환 - mp3 / wav
  
  - 언어, 음색 선택 가능

- **CLOVA Voice - Premium**
  
  - CLOVA Speech Recognition(CSR)
  
  - 서비스 통합

- **CLOVA Chatbot**
  
  - 챗봇 제작 API 서비스
  
  - 사용자의 질문 의도를 이해하여 고객 대응 등 다양한 서비스에 활용할 수 있는 챗봇 제작 지원

- **Pose Estimation**
  
  - 입력된 비전 데이터를 통해 사람을 인식하고 포즈 분석
  
  - 이미지 속의 사람을 감지하고 주요 신체부위(18개)의 좌표 정보와 정확도를 얻을 수 있음

- **Object Detection / Papago**
  
  - 이미지 내에 사람, 자동차, 동물 등 객체의 타입과 위치를 감지하여 정보를 제공
  
  - 탐지된 객체명, 객체의 수, 바운딩 박스용 좌표, 객체별 확률 값

##### AI API 사용 방법

- 서비스 요청(뷰 페이지 : index.jsp)

- 컨트롤러

- 서비스
  
  - API 요청 코드를 서비스 클래스의 메소드 작성
  
  - JSON 파싱 / 결과 반환

- 컨트롤러

- 뷰 페이지로 결과 출력

##### 작업과정

- AI Platform 계정으로 접속(1인 1계정)

- 첫 접속시 비밀번호 변경(필수)

- Console로 이동

- Service
  
  - AI-NAVER API / Application
  + +Aplication 등록

##### Pose Estimation(포즈인식)

1. **기본 (API) 호출결과 확인**
   
   - PoseEstimationService 서비스 클래스 생성
   
   - poseEstimate() 메소드 추가
   
   - API 자바코드 복사 붙여넣기
   
   - image : run.jpg
   
   - 컨트롤러에 매핑 추가
   
   - index.jsp에 추가
   
   - 결과 확인 : 콘솔에 JSON문자열 출력 확인후 JSON viewer에서 전체 구조 확인

2-  **JSON결과 파싱**

- PoseVO 생성
  
  - int index
  
  - double x, y

- jsonToVOList() 메소드 추가
  
  - JSON형태의 문자열 파싱해서 VO에 저장 / List에 추가(poseList)
    
    ```java
    public ArrayList<PoseVO> jsonToVOList(String jsonResultStr){
    
            ArrayList<PoseVO> poseList = new ArrayList<PoseVO>();
    
            // JSON 형태의 문자열에서 JSON 오브젝트 "predictions"추출해서 JSONArray에 저장
            JSONObject jsonObj = new JSONObject(jsonResultStr);
            JSONArray poseArray = (JSONArray)jsonObj.get("predictions");
    
            if(poseArray != null) {
    
                for(int i = 0; i<poseArray.length(); i++) {
                    JSONObject poseObj = poseArray.getJSONObject(i);
    
                    for(int j = 0; j<=17; j++) {
    
                        if(poseObj.has(String.valueOf(j)) == false) {
                            continue;
                        }
                        JSONObject tempObj = (JSONObject) poseObj.get(String.valueOf(j));
    
                        // x, y값 추출 저장
                        double x = Double.parseDouble(String.valueOf(tempObj.get("x")));
                        double y = Double.parseDouble(String.valueOf(tempObj.get("y")));
    
                        // VO에 저장
                        PoseVO vo = new PoseVO();
                        vo.setIndex(i);
                        vo.setX(x);
                        vo.setY(y);
    
                        // 리스트에 추가
                        poseList.add(vo);
                    }
    
                }
            }else {
                PoseVO vo = new PoseVO();
                vo.setIndex(0);
                vo.setX(0);
                vo.setY(0);
            }
    
            return poseList;
        }
    ```
3. **파일 업로드 / 이미지 출력 / 좌표 표시 / 신체 부위 좌표 출력**
   
   - @RestController 추가
     
     ```java
     @RestController
     public class AIRestController {
        @Autowired
            PoseEstimationService peService;
     
         
         // 포즈인식
        // (3) 파일 업로드하고 결과 받기
            @RequestMapping("/poseDetect")
            public ArrayList<PoseVO> poseDetect(@RequestParam("uploadFile") MultipartFile file) throws IOException {
     
                // 1. 파일 저장경로 설정 : 실제 서비스되는 위치(프로젝트 외부에 저장)
                String uploadPath = "C:/upload/";
                // 마지막에 있어야 함
     
                // 2. 원본파일 이름 알아오기
                String originalFileName = file.getOriginalFilename();
                String filePathName = uploadPath + originalFileName;
     ```
     
                 // 3. 파일생성
                 File newFile = new File(filePathName); 
         
                 // 4. 서버로 전송
                 file.transferTo(newFile);
         
                 ArrayList<PoseVO> poseList = peService.poseEstimate(filePathName);
         
                 return poseList;
             }
- poseResult.sjp 추가
  
  - 파일 업로드
  
  - < canvas>태그 추가
    
    - 포즈 인식결과를 이미지 상에서 각 부위에 좌표로 표시
    
    - < div id="resultBox"> 각 신체부위와 좌표값 출력
  
  ```jsonp
  <%@ page language="java" contentType="text/html; charset=UTF-8"
      pageEncoding="UTF-8"%>
  <%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
  <!DOCTYPE html>
  <html>
      <head>
          <meta charset="UTF-8">
          <title>포즈 인식 결과</title>
          <script src="<c:url value='/js/jquery-3.6.0.min.js'/>"></script>
          <script src="<c:url value='/js/pose.js'/>"></script>
      </head>
      <body>
          <!-- 파일 업로드 -->
          <h3>포즈인식</h3>
          <form id="poseForm" enctype="multipart/form-data">
              파일 : <input type="file" id="uploadFile" name="uploadFile">
              <input type="submit" value="결과확인">
          </form>
  
          <!-- 결과 출력 -->
          <h3>포즈 인식 결과를 이미지에 좌표로 표시</h3>
          <canvas id="poseCanvas" width="600" height="600"></canvas>
          <br><br>
  
          <!-- 각 신체부위와 좌표 갑 출력 -->
          <div id="resultBox"></div>
  
          <br><br>
          <a href="<c:url value='/'/>">index 페이지로 이동</a>
      </body>
  </html>
  ```

- pose.js 추가(ajax 사용)
  
  - 컨트롤러로 요청 전달하고 결과 받아서 < canvas>와 resultBox에 출력
  
  ```javascript
  /**
   * pose.js
   */
  
   $(document).ready(function(){
       $('#poseForm').on('submit', function(){
           // submit 이벤트 기본 기능 : 페이지 새로 고침
           // 기본 기능 중단
           event.preventDefault();
  
           // 폼 데이터 읽어오기
           var formData = new FormData($('#poseForm')[0]);
  
           //  업로된 파일명 알아오기
           var fileName = $('#uploadFile').val().split("\\").pop();
           //alert(fileName);
  ```
  
              $.ajax({
                  type: "post",
                  url: "poseDetect",
                  enctype: 'multipart/form-data',
                  data: formData,
                  processData: false,   // multipart 사용하기 위한 필수
                  contentType: false,
                 success: function(result){
                     drawCanvas(result, fileName); 
                 },
                 error: function(){
                     // 오류 있을 경우 수행되는 함수
                     alert("전송 실패");
                 }
              }); // ajax 끝
          }); // submit 끝
      
          function drawCanvas(result, fileName) {
              //canvas 객체 생성
              var canvas = document.getElementById("poseCanvas");
              var context = canvas.getContext("2d");
      
              // 이미지 설정 : 경로, 파일명, 크기
              var poseImage = new Image();
              poseImage.src = "/images/" + fileName;
              poseImage.width = canvas.width;
              poseImage.height = canvas.height;
      
              // 이미지 로드되었을 때 context, 색상, 위치 배열 설정
              poseImage.onload = function(){
                  context.drawImage(poseImage, 0, 0, poseImage.width, poseImage.height);
      
                  var colors = ["red", "blue", "yellow", "yellow","yellow","green", "green",
                                         "green", "skyblue","skyblue","skyblue","black","black","black",
                                         "pink","gold", "orange","brown"];        
      
                 var position = ["코", "목", "오른쪽 어깨", "오른쪽 팔굼치", "오른쪽 손목", 
                                             "왼쪽 어깨", "왼쪽 팔굼치", "왼쪽 손목", "오른쪽 엉덩이", "오른쪽 무릎",
                                             "오른쪽 발목", "왼쪽 엉덩이", "왼쪽 무릎", "왼쪽 발목", "오른쪽 눈",
                                             "왼쪽 눈", "오른쪽 귀", "왼쪽 귀"];     
      
              // 각 신체부위별 좌표 표시
              var values = "";
      
              $.each(result, function(i) {
                  if(this.x != 0 | this.y != 0 ){
                      context.strokeStyle = colors[i]; 
                      context.strokeRect(this.x * poseImage.width, this.y * poseImage.height, 2, 2); // 출력위치
                      var text = this.x.toFixed(2) + ", " + this.y.toFixed(2); // 소수점 2자리
                      context.font = '10px serif'; // 폰트
                      context.strokeText(text, this.x * poseImage.width, this.y * poseImage.height); // 텍스트 출력
                  };
      
                  values += position[i] + "(" + this.x + ", " + this.y + ")<br>";
              });
      
              // resultBox에 출력
              $('#resultBox').html(values);
              };
          }
       })

##### CLOVA OCR
