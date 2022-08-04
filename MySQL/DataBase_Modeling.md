### 데이터 베이스 모델링
> 데이터베이스 설계
> 데이터베이스 설계 순서
> 데이터베이스 모델링 개념

##### 데이터 베이스 설계
- 사용자의 요구를 분석하여 컴퓨터에 저장할 수 있는 데이터 베이스의 구조에 맞게 변경
- 특정 DBMS로 구현하여 일반 사용자들이 사용할 수 있게 하는 것

##### 데이터 베이스 설계 순서
![[Pasted image 20220803160800.png]]

##### 데이터베이스 모델링
- 현실 세계에 존재하는 개체의 구성 요소가 가지는 **값(데이터)** 을 **컴퓨터 세계에 표현**하기 위한 현실 세계와 컴퓨터 세계 사이의 변환 과정
- 현실 세계의 복잡한 개념을 단순화 / 추상화 시켜 데이터베이스화 하는 기법
- 프로젝트 분석과 설계 단계에서 가장 중요한 작업 중 하나
![[Pasted image 20220803161058.png]]

##### 모델링 과정에서 수행되는 작업
1. 데이터 베이스 내에 존재하는 데이터 타입 정의
2. 데이터들 사이의 관계 규정
3. 데이터의 의미와 데이터에 가해진 제약조건 명시

##### 모델링 과정
![[Pasted image 20220803161244.png]]

- 개념적 모델링
	- 현실세계를 추상적인 개념인 개체 타입과 관계 타입으로 표현
	- 요구사항 분석결과를 토대로 업무의 핵심적인 개념을 구분하고 개체(entity)추출, 관계정의
	- ER 다이어그램(ERD : Entity Relationship Diagram)이라는 표준화된 그림으로 표현
	![[Pasted image 20220803161737.png]]

- 논리적 모델링
	- 실제 데이터베이스로 구현하기 위한 모델을 만드는 과정
	- 개념적 모델링에서 산출된 ER다이어그램을 사용하고자 하는 DBMS에 맞게 사상(맵핑 : Mapping)하는 과정
	![[Pasted image 20220803162009.png]]

- 논리적 모델링 과정 중 수행 작업
	- 개념적 모델링에서 추출하지 않았던 상세 속성 모두 추출
	- 정규화 수행
	- 데이터 표준화 수행

- 물리적 모델링
	- 작성된 논리적 모델을 실체 컴퓨터의 저장 장치에 저장하기 위한 물리적 구조를 정의하는 과정
	- 데이터 베이스가 최적의 성능을 낼 수 있도록 DBMS의 특성에 맞게 저장 구조 정의
	![[Pasted image 20220803164403.png]]

##### 개념적 모델링(개체 - 관계 모델 : E - R 모델)
1. 개체 관계 모델 개념
	- 개체와 개체 간의 관계를 이용해 현실 세계 를 개념적으로 표현하는 모델
	- 데이터 베이스 설계과정중 개념적 설계 과정에 사용되는 모델
	- 개체와 개체간의 관계를 E - R 다이어그램이라는 표준화된 그림으로 표현
	![[Pasted image 20220803164648.png]]

2. E - R 다이어그램 
	- 개념적 모델링(개체-관계 모델링)의 결과물로 기호를 사용하여 현실 세계를 표현한 것
	- ERD 표기법
		- 피터첸 표기법
			- 관계에 중점을 둔 표기법
			- 쉬운 표기법으로 쉽게 이해
			- 속성이 많아지거나 관계가 복잡해 지면 표현하기 어려움
			![[Pasted image 20220803165154.png]]
			- 피터첸 기법의 ERD에서 사용되는 기호
			![[Pasted image 20220803165232.png]]
		- IE 표기법
			- 정보공학에서 사용하는 데이터 모델 표기법
			- 많이 사용되는 표기법 중에 하나이지만 집합의 상세 표현에 있어서 공간을 많이 차지하는 단점이 있음
			- ERWin이라는 데이터 모델링 툴에서 사용
			![[Pasted image 20220803165749.png]]
		- Baker 표기법
			- 영국 컨설팅 회사 CACI에 의해 처음 개발
			- 리차드 바커(Richard Baker)에 의해 지속적으로 업그레이드
			- 오라클에서 Case Method(Custom Development Method)로 채택하여 사용
			![[Pasted image 20220803165937.png]]

3. 개체(Entity)
	- 개체
		- 사람, 사물, 장소, 개념, 사건과 같이 유무형 정보를 가지고 있는 독립적인 실체
	- 개체의 유형
		- 개념적 개체
			- 학과, 과목, 예금 등과 같이 눈에 보이지 않는 개체
		- 물리적 개체
			- 사람, 도서, 상품 등과 같이 눈에 보이는 개체
	- 개체의 특징
		- 유일한 식별자에 의해 식별 가능
		- 꾸준한 관리를 필요로 하는 정보
		- 업무 프로세스에 이용
		- 반드시 자신의 특징을 나타내는 속성 포함
			- 도서명, 저자, 발행일, 출판사 등
		- 다른 개체와 관계 설정 가능
	- 개체 인스턴스(Entity Instance)
		- 특정 하나의 개체
	- 개체 집합(Entit Set)
		- 유사한 개체들의 집합
		- 동일한 속성을 공유하는 같은 유형의 개체 집합
	- 개체 타입(Entity Type)
		- 개체를 정의한 것
		![[Pasted image 20220803172149.png]]

	- 개체 타입의 E-R 다이어그램 표현
		- 직사각형으로 표현
		![[Pasted image 20220803172444.png]]

4. 속성(attribute)
	- 개체의 성질, 분류, 수량, 상태, 특성, 특징의 세부사항
	- 저장할 필요가 있는 개체에 관한 정보
	- 실제 저장되는 데이터(값)
	![[Pasted image 20220803172746.png]]
	