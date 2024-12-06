### Docker 이미지 생성 및 실행

1. Dockerfile 작성

   ```dockerfile
   # 1. 베이스 이미지 설정
   FROM openjdk:17-jdk-slim
   
   # 2. 앱 디렉터리 생성
   WORKDIR /app
   
   # 3. Gradle 빌드 후 jar 파일 복사
   COPY build/libs/*.jar app.jar
   
   # 4. 애플리케이션 실행
   ENTRYPOINT ["java", "-jar", "app.jar"]
   
   ```

2. docker-compose.yml 작성

   ```yaml
   version: '3.8'
   
   services:
     app:
       build:
         context: .
         dockerfile: Dockerfile
       ports:
         - "8080:8080" # 호스트의 8080 포트를 컨테이너의 8080 포트에 연결
       environment:
         SPRING_PROFILES_ACTIVE: prod # 프로파일 설정
   ```

3. 도커 이미지 빌드 및 실행

   - JAR 파일 생성(루트 디렉토리에서 JAR파일 생성한다.)

     `./gradlew bootJar` 명령어 실행하면 build/lib 디렉토리에 *.jar파일이 생성된다.

   - 도커 이미지 빌드

     `docker build -t <빌드할 이미지의 이름> .` 이 명령어로 이미지를 빌드한다.

   - 도커 컨테이너 실행

     `docker run -p 8080:8080 <빌드한 이미지의 이름>` 여기서 -p 8080:8080은 8080포트에서 실행한 앱을 8080포트로 끌어온다는 의미

     만약 백그라운드로 실행을 하고싶으면 -d를 추가하면 된다

     => `docker run -d -p 8080:8080 <빌드한 이미지의 이름>`