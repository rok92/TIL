### ChatBot

##### 1. 도메인 생성

##### 2. 대화 생성

- 학습 질문 입력(여러개)

- 챗봇 답변 입력(여러개)

- 웰컴 메시지 작성

##### 3. 챗봇 빌드(대화 모델 빌드)

##### 4. 챗봇 테스트

##### 5. 서비스 배포

- 빌드 내역 확인

##### 6. 메신저 연동(Custom 연동 설정)

- Custom API Gateway와 … 필요합니다 / [연동] 클릭
- [자동 연동] / [확인] 
- API Gateway URL : [주소 복사]
- 아래로 내려서
- Secret Key : [생성] / [복사]
- [연동]
- 연동 완료 : 파란색으로 변경

##### 7. 스프링에서 작업

1. **API 호출 결과 출력**
   
   - ChatbotService 서비스 클래스 생성
   
   - API 코드 복사(3개 다 복사) => main() / makeSignature() / getReqMessage()
   
   - API 컨트롤러에 추가
     
     - main()메소드 호출하면서 "넌 누구니?" 호출
   
   - index.jsp에 추가하고 json viewer로 확인
   
   - **주의!!! : static 호출할 때 클래스명으로 직접 호출한다!(Do not use @Autowired)**

2. **JSON 파싱**
   
   - jsonToString() 메소드 추가
   
   - 응답 메시지 추출 / 출력  

3. **뷰 페이지에서 입력 / 출력**
   
   - AIRestController / Ajax
   
   - chatbot.js
   
   - chatForm.jsp 생성
   
   - 컨트롤러 변경
   
   - index 변경

