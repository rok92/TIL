## Pipe Setting

#### 1. HTTP 요청 방식

![image-20230902192323531](/Users/rok/Library/Application Support/typora-user-images/image-20230902192323531.png)

- 먼저 post 메서드와 전체 경로가 나타난 start line을 보면 전체 요청경로와 마지막에 프로토콜도 볼 수 있다.
- Header부분에는 사용하고 있는 포트와 어떠한 타입으로 나타내고 있는지 보여주고 있다.
- Body부분은 클라이언트에서 서버로 요청하는 방식을 말하고 있으며 반드시 저러한 형태로 요청해야 응답을 받을 수 있다.
- 위 정보는 필요에 따라 모두 추출할 수 있는 정보들이다. 예를 들면  `POST /message/5?validate=true HTTP/1.1` 부분에서 query값을 추출하고 싶으면 ?뒤에 있는 값을 추출할 수 있다.

#### 2. Bunch of Decorator

- 위 내용에서 알 수 있듯이 요청에 따라 수행하는 역할이 다 존재하며 필요에 따라 정보를 추출할 수 있다. NestJS에서는 그러한 역할을 수행하는 Decorator들이 존재한다.

  ![image-20230902193307788](/Users/rok/Library/Application Support/typora-user-images/image-20230902193307788.png)

- 데코레이터 영역

  - 데코레이터는 위치와 역할에 따라서 영역이 나뉘어 지게 된다..
  - Class decorator
    - 클래스의 바로 앞에 선언하며 우리가 이전에 사용했던 @Controller가 이에 속한다. 클래스의 생성자에 적용되어 클래스의 정의를 읽거나 수정할 수 있지만 선언 파일과 선언 클래스 내에서는 사용할 수 없다.
  - Method decorator
    - 메서드의 앞에 선언하는 데코레이터로 @Get, @Post와 같은 데코레이터가 이에 속한다.
  - Argument decorator
    - 선언한 메소드의 속성값으로 넣는 데코레이터로 @Param, @Query, @Body와 같은 데코레이터가 이에 속한다.

#### 3. Pipe의 역할

- 파이프는 요청방식이 유효한지를 검사하기 위해 반드시 필요하다. 요청할 때 Pipe가 없다면 데이터의 형태가 어떠한 형태든 요청이 가능해지기 때문에 정확한 요청을 할 수 없다. 예를들면 반드시 string형태로 데이터전송을 해야하는데 integer의 형태로 데이터를 전송했을 경우 Pipe에서 잘못된 요청으로 걸러주어야 한다.

- 모든 요청은 Controller에 도달하기 전에 반드시 Pipe를 통해야 한다. Pipe는 직접 만들 수 있지만 ValidationPipe라는 유용한 라이브러리로 사용할 수 있다.(nest/common에 이미 내장되어 있는 라이브러리)

- 이 프로젝트에서 요청할 방식

  ![image-20230902200101429](/Users/rok/Library/Application Support/typora-user-images/image-20230902200101429.png)

- 유효성 검사를 위해 필요한 Module

  - `npm install class-validator class-transformer`

- Main.ts

  ```typescript
  import { NestFactory } from '@nestjs/core';
  import { ValidationPipe } from '@nestjs/common';
  import { MessagesModule } from './messages/messages.module';
  
  async function bootstrap() {
    const app = await NestFactory.create(MessagesModule);
    // 파이프를 전역으로 사용하게 설정
    app.useGlobalPipes(new ValidationPipe());
    await app.listen(3000);
  }
  bootstrap();
  ```

#### 4. ValidationPipe

- Process

  ![image-20230902202429937](/Users/rok/Library/Application Support/typora-user-images/image-20230902202429937.png)

- 파일 추가

  - dtos라는 폴더를 추가 후 create-message.dto.ts 라고 파일을 생성한다.

- create-message.dto.ts

  ```typescript
  import { IsString } from 'class-validator';
  
  export class CreateMessageDto {
    @IsString()
    constent: string;
  }
  // https://github.com/typestack/class-validator#validation-decorators 에서 사용할 수 있는 데코레이터를 확인 할 수 있다.
  ```

- messages.controller.ts

  ```typescript
  import { Controller, Get, Post, Body, Param } from '@nestjs/common';
  import { CreateMessageDto } from './dtos/create-message.dto';
  
  @Controller('messages')
  export class MessagesController {
    @Get()
    listOfMessages() {}
  
    @Post()
    createMessages(@Body() body: CreateMessageDto) {
      console.log(body);
    }
  
    @Get('/:id')
    getMessages(@Param('id') id: string) {
      console.log(id);
    }
  }
  ```

#### 5. Data Transfer Object(DTO)

- DTO의 목적은 두 장소간의 정보나 데이터를 네트워크 요청의 형태로 전달하는 역할을 한다.
- 또한 DTO는 특정 테이블 정보를 레코드 단위로 정의해둔 클래스이기도 하다.
- DTO와 VO
  - DTO와 VO는 비슷한 역할을 한다. VO또한 DTO와 같이 특정 데이터를 정의해둔 클래스를 의미하지만 명확한 차이가 존재한다.
  - DTO : 가변의 성격을 가진 클래스이며 데이터 전송을 위해 존재한다(getter, setter존재) => 인스턴스 개념
  - VO : 불변의 성격을 가진 클래스이며 getter만 존재한다. 즉, 읽기만 가능한 read-only의 특성을 가지고 있다. => 리터럴 개념