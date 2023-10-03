## NestJS Project Setup

####  1. Package.json 설정

- 프로젝트를 설정할 폴더 생성 후 터미널에서 `npm init` 명령어를 실행해 준다.(다음과 같이 package.json이 생성됨.)

  ![image-20230819165441207](/Users/rok/Library/Application Support/typora-user-images/image-20230819165441207.png)

- 그 다음 설정에 필요한 것들을 명령어로 설치해 준다.

  `npm install @nestjs/common@7.6.17 @nestjs/core@7.6.17 @nestjs/platform-express@7.6.17 reflect-metadata@0.1.13 typescript@4.3.2`

  위의 과정이 끝나면 node_modules가 들어와있고, 다음과 같이 package.json이 설정되어 있게 된다.

```json
{
  "name": "start_nest",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "author": "",
  "license": "ISC",
  "dependencies": {
    "@nestjs/common": "^7.6.17",
    "@nestjs/core": "^7.6.17",
    "@nestjs/platform-express": "^7.6.17",
    "reflect-metadata": "^0.1.13",
    "typescript": "^4.3.2"
  }
}
```

- 각 패키지 역할
  - @nestjs/common => NestJS 라이브러리는 여러 패키지로 나뉘는데 common에서는 대부분의 기능, 클래스, 중첩 응용프로그램을 빌드하는데 사용할 기타 항목이 포함되어 있다.
  - @nestjs/core => NestJS 애플리케이션의 핵심 기능을 위한 핵심 패키지로, 모듈 로딩, 의존성 주입, 라우팅, 미들웨어 처리, 라이프사이클 관리 등을 관리한다.
  - @nestjs/platform-express => 내부적으로 NestJS는 들어오는 요청을 처리하지 않고 외부 구현에 의존하여 그에 대한 요청을 처리하게 된다. 즉, 들어오는 모든 HTTP요청을 처리하게 도와주는 패키지이다.
  - reflect-metadata => NestJS와 같은 TypeScript 기반 프레임워크에서 런타임에서 메타데이터를 사용하여 의존성 주입, 라우팅 등의 동작을 보다 동적으로 처리하기 위해 사용한다.
  - typescript => NestJS와 함께 사용하게 될 언어 설정이다.(javascript를 사용해도 무방)

#### 2. Typescript 컴파일러 설정

- root위치에 tsconfig.json파일을 만들고 다음과 같이 설정해준다.

  ``` json
  {
      "compilerOptions": {
          "module": "CommonJS",
          "target": "ES2017",
          "experimentalDecorators": true,
          "emitDecoratorMetadata": true
      }
  }
  ```

- 위 설정은 Typescript가 프로젝트를 실행하기 전에 프로젝트를 일반 Javascript코드로 적절하게 변환하도록 하는 설정이다.

#### 3. NestJS가 데이터를 처리하는 일련의 과정

- 생성하는 모든 HTTP 서버에는 요청, 응답 주기가 있다. 사용자가 서버에 요청을 하면 서버는 해당 요청을 처리할 코드가 있고 수행을 한다. 수행을 하는 과정에는 일부 데이터의 유효성을 검사할 수도 있을 것이며, 처리되는 경로에 따라 요청을 다르게 처리할 수도 있다.  일련의 과정을 거친 후 응답을 공식화 해서 사용자에게 다시 전송해주게 된다. 이것이 요청, 응답주기이다.

  ![image-20230819183921943](/Users/rok/Library/Application Support/typora-user-images/image-20230819183921943.png)

- 어떠한 프레임워크이든 위 과정은 동일하게 거치게 되며 NestJS에서는 각각의 역할을 도와주는 툴이 있다.

  ![image-20230819184544996](/Users/rok/Library/Application Support/typora-user-images/image-20230819184544996.png)

  - Pipe : 요청한 데이터를 검증하는데 도움을 주는 툴
  - Guard : 들어오는 요청이 우리 응용프로그램을 사용하도록 인증되거나 권한이 있는 사용자로부터 오는지 확인
  - Controller : 라우팅의 기능이 내포
  - Service : 일련의 비즈니스 로직이 수행되는 장소

#### 4. Controller Module 설정

- root에 src폴더를 생성 후 그 안에 main.ts파일을 생성

```ty
import { Controller, Module, Get } from "@nestjs/common";
import { NestFactory } from "@nestjs/core";

@Controller() // 데코레이터라 부르며 해당 파일이 수행하는 역할을 지정해주는 역할(자바의 어노테이션 개념)
class AppController {
  @Get() // 요청방식을 설정
  getRootRoute() {
    return "Hello Nest!";
  }
}

// 모듈의 역할은 컨트롤러를 마무리하는 역할을 수행한다. 그렇기 때문에 모듈을 반드시 생성해 주어야 한다.
// 모듈을 만들기 위해서는 클래스의 형태로 모듈을 선언해줘야 한다.
@Module({
  controllers: [AppController],
})
class AppModule {}

// 모듈 생성 후 컨트롤러 적용 완료

// 모든 셋팅한 후 어플리케이션을 실행하기위한 함수 설정을 해줘야 한다.
// 보통 bootstrap이라고 설정을 하는 것이 보편적이며 이름은 아무거나 해도 됨.
const bootstrap = async () => {
  const app = await NestFactory.create(AppModule);

  await app.listen(3000);
};

bootstrap();
```

- `npx ts-node-dev src/main.ts` 명령어로 실행해준다.

  ![image-20230819192013392](/Users/rok/Library/Application Support/typora-user-images/image-20230819192013392.png)

  실행하면 위와 같이 실행이 되는 것을 확인할 수 있고, 브라우저에 해당 포트로 접속하면 return값을 확인할 수 있다.
