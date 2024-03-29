# MultiCampus Final Project



### 팀명 :

![image-20220805164454737](README.assets/image-20220805164454737.png)

<center>
    <h3>
        불사조
    </h3>
</center>







### 팀원 : 

####       황재윤 곽경록 이동욱 이혜원



### 주제 : 

##     **반려동물 AI 정보 커뮤니티**



### 목적 : 

1.  반려동물을 키우는 인구가 1500만을 돌파하고 반려동물 관련 사이트가 많이 증가하여 사료 또는 반려용품을 구매하거나 호텔, 병원, 애견카페 등 위치 정보를

    확인하기 어렵고 불필요한 많은 정보들이 포함되고 있는 현황이다.

2. 이에 우리팀은 반려동물 관련 용품이나 필요한 정보들을 효율적으로 제공하기 위한 반려동물 사이트를 구상하게 되었다.

3. 지능형 서비스를 활용한 추천 서비스, 위치기반 시설 검색 서비스, 반려동물 관련 질의 응답 기능을 제공하는 챗봇 서비스를 제공하여 다른 사이트에서 

   제공하지 않는 차별화된 서비스 제공하고자 한다.



### 프로젝트 수행 도구 :

- 개발 환경 : JDK 11, Apache Tomcat9, bootstrap, Spring boot

- 개발 언어 : HTML, CSS, Javascript, jQuery, MySQL

- 통합 개발 툴 : Eclipse

- 협업 툴 : git, gitHub



### 프로젝트 수행 방향:

**1.** **레이아웃(UI / UX)**



- 메인 페이지

- 게시판4종류 (공지, 질문, 자유, 중고 거래)

- 서비스(상품)

  - 사료 / 간식

  - 애견용품
  - 결제시스템
  - 장바구니

- 서비스(정보 제공)
  - 카페 / 호텔
  - 병원 

-  로그인(팝업)

- 회원 가입

- 마이 페이지

- 관리자 페이지
  - 사용자 관리
  - 탈퇴자 확인
  - 공지 사항
  - 게시글 관리(댓글 포함)
  - 사용자 문의 내역
  - 사용자 결제 내역

 

**2.** **백엔드 기능**



- 메인 페이지
  - 관리자가 접속하면 상단 메뉴 버튼 (사용자 관리) 생성
  - 그 외 일반 사용자가 접속할 때나 로그인 하지 않을 때는 숨김
  - 로그인 시 로그인, 회원가입 탭이 로그아웃, 마이페이지로 변경
  - 관리자에게 문의 기능 구현
  - 메인 페이지 챗봇 기능 구현



- 게시판
  - CRUD 구현. 단, 공지 사항은 관리자가 작성한 정보를 사용자들이 확인만 가능
  - 검색 기능 구현. 아래 사용자가 자주 검색한 단어 순위 표시
  - 최신순 추천순 댓글순 조회순 등으로 내림차순 가능



- 로그인

  - 유효성 체크

  - 비밀번호 암호화

  - 사용자의 ID 및 PW 분실 시 해당 사용자의 이메일로 ID 및 임시비번 제공(메일링 서비스) 

    

- 회원 가입

  - 유효성 체크

  - 프로필 이미지 미리보기 및 업로드 기능 구현

  - 회원가입 완료시 데이터 데이터베이스로 전송

    

- 마이 페이지

  - 가입한 사용자가 자신의 정보를 수정 및 회원탈퇴

  - 탈퇴시 DB 회원 정보 삭제하고 탈퇴 테이블에 해당 정보 추가 

    

- 관리자 페이지

  - 사용자 관리 : 현재 가입된 사용자의 정보를 확인 및 수정

  - 탈퇴자 확인 : 탈퇴한 사용자의 정보를 확인

  - 공지 사항 : 사용자들에게 제공할 중요한 사항을 입력(CRUD)

  - 게시글 관리(댓글 포함) : 사용자들이 작성한 게시글 및 댓글 정보 확인. 부적절한 게시글일 경우 삭제 기능 구현

  - 사용자 문의 내역 : 사용자들이 관리자에게 문의한 사항들을 확인

  - 사용자 결제 내역 : 사용자들이 결제한 내역을 확인
  - 

- 서비스(상품)

  - 사용자에게 조건, 구분에 따른 상품을 분류 및 제공

  - 관리자만 제공한 상품을 수정 및 삭제. 그 외 사용자는 조회

  - 상품 구매 시 결제 시스템 구현(실제 결제는 안됨)

  - 장바구니 기능 구현



- 서비스(정보)

  - 사용자에게 위치, 구분에 따른 장소 제공

  - 해당 장소에 대한 평점 표시

  - 해당 사이트를 접속한 사용자의 위치 정보를 확인(AI Service)하여 주변 위치에 정보를 제공

 

**3.** **사용할 API 및 AI 서비스**



- API

  - 패스워드 암호화 API : PasswordEncoder

  - 패스워드 분실 시 랜덤 문자열 생성 : RandomStringUtils

  - 메일링 서비스 구현 : EmailJS

  - 게시판 : Summernote

  - 자주쓰는 검색어 : Redis Sorted set 

- AI 서비스

  - 챗봇 : Naver CLOVA Chatvot

  - 사용자 위치 제공 : Naver GeoLocation

  - 해당 위치 정보 제공 : Naver Web Dynamic Map



### 프로젝트 예상 일정 :

- 1주차(8월 2일 ~ 8월 7일) : 프로젝트 기획 및 설계



- **8월 8일 : 주제 발표**



- 2주차(8월 9일 ~ 8월 14일) : UI/UX 설계 및 구현

- 3주차(8월15일 ~ 8월 21일) : DB설계

- 4주차(8월 22일 ~ 8월 28일) : 백엔드 기능 구현



- **8월 31일 : 중간 발표**



- 5주차(8월 29일 ~ 9월 4일) : 백엔드 기능 구현

- 6주차(9월 5일 ~ 9월 11일) : AI 기능 구현

- 7주차(9월 12일 ~ 9월18일) : AI 기능 구현

- 8주차(9월 19일 ~ 9월 22일) : 포트폴리오 작성



- **9월 23일 : 프로젝트 발표**



### TIMELINE

![image-20220805151357675](MultiCampus Final Project.assets/image-20220805151357675.png)



### 데이터베이스 설계 

​                                                             ![MultiCampus](MultiCampus Final Project.assets/MultiCampus.png)



### UI 설계(홈페이지 계층 구조도)

![image-20220805151823313](MultiCampus Final Project.assets/image-20220805151823313.png)![image-20220805151823313](MultiCampus Final Project.assets/image-20220805151823313.png)

