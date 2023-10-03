## Service and Repository

#### 1. How different Service and Repository

![image-20230909235700230](/Users/rok/Library/Application Support/typora-user-images/image-20230909235700230.png)

- Service는 주로 비즈니스 로직(수학적 연산)이 수행되는 장소이고, Repository는 연산된 데이터가 저장, 읽기, 수정, 삭제되는 데이터베이스와 연결 역할을 하는 장소로 사용되어 진다.

- 프로젝트의 사이즈에 따라 달라지지만 하나의 Service가 여러개의 repository를 사용할 수도 있다.

- 우리가 수행할 프로젝트의 로직

  ![image-20230910001219007](/Users/rok/Library/Application Support/typora-user-images/image-20230910001219007.png)

  - 의문점 :  메서드의 사용이나 생김새가 Service와 Repository와 차이가 없다는 것을 알 수 있다. 위에서 설명했듯이 모든 로직은 Repository에서 보통 끝이 나는데 그렇다면 Service로직의 존재이유는 무엇인가?
  - Service: 컨트롤러 클래스와 분리되어 비즈니스 로직과 HTTP요청을 분리하는 등 코드의 재사용을 가능하게 만들기 때문에 필요하다. 만약에 컨트롤러와 직접 repository와 연동하게 되면 하나의 로직밖에 수행하지 못하기 때문에 코드 재사용 가능성이 떨어지게 된다.
  - Repository : 데이터베이스와 직접적으로 연결되어 CRUD를 실행하는 클래스로 쿼리등을 작성하게 되는 클래스 이다.
  - 요약하면, Service 클래스는 비즈니스 로직을 처리하고 컨트롤러와 분리된 계층이고,  Repository 클래스는 데이터베이스와의 상호작용을 담당하고 데이터의 CRUD 작업을 처리한다. NestJS에서 이 두 가지 클래스를 사용하는 이유는 애플리케이션을 보다 구조적으로 관리하고 유지보수 가능하게 만들기 때문이다.

#### 2. Messages Project

- 먼저 messages폴더안에 service.ts, repository.ts를 생성한다.

- root폴더에 messages.json(데이터를 저장할 작은 임시저장소)를 생성한다.

- messages.repository.ts

  ```typescript
  // 파일을 읽고 쓰기위한 라이브러리 추가
  import { CUSTOM_ROUTE_ARGS_METADATA } from '@nestjs/common/constants';
  import { readFile, writeFile } from 'fs/promises';
  
  export class MessagesRepository {
    async findOne(id: string) {
      const contents = await readFile('messages.json', 'utf-8'); // 어떠한 파일을 어떠한 형식으로 읽어들일지 정함
      // 제이슨을 객체형태로 변환작업
      const messages = JSON.parse(contents);
  
      return messages[id];
    }
  
    async findAll() {
      const contents = await readFile('messages.json', 'utf-8');
      const messages = JSON.parse(contents);
  
      return messages;
    }
  
    async create(content: string) {
      const contents = await readFile('messages.json', 'utf-8');
      const messages = JSON.parse(contents);
  		// id값을 세 자리 난수로 부여
      const id = Math.floor(Math.random() * 999);
  		// 다음과 같은 객체 형태로 값을 생성
      messages[id] = { id, content };
  		// 글을 작성
      await writeFile('messages.json', JSON.stringify(messages));
    }
  }

- 메세지를 추가하게 되면 다음과 같은 형식으로 json 파일에 저장되게 된다.

  ```json
  {
    "1":{
      "content": "건방진 자식들",
      "id": 1
    }
  }
  ```

- messages.json(빈 객체를 하나 넣어둔다)

  ```json
  {}
  ```

- messages.service.ts

  ```typescript
  import { MessagesRepository } from './messages.repository';
  
  export class MessagesService {
    messagesRepo: MessagesRepository;
  
    // 서비스는 자체만으로 동작할 수 없기 때문에 repository에 의존을 하라고 의존성 주입
    // 그냥 의존성 주입이 어떠한 형태로 되는지 과정을 보기 위한 코드이므로 대강보셈.
    // 실제로는 @Injection 데코레이터를 사용해서 의존성 주입을 할 예정. 내가 스터디 나갈때 소스 줄거임
    constructor() {
      this.messagesRepo = new MessagesRepository();
    }
  
    findOne(id: string) {
      return this.messagesRepo.findOne(id);
    }
  
    findAll() {
      return this.messagesRepo.findAll();
    }
  
    create(content: string) {
      return this.messagesRepo.create(content);
    }
  }
  ```

- messages.controller.ts

  ```typescript
  import { Controller, Get, Post, Body, Param } from '@nestjs/common';
  import { CreateMessageDto } from './dtos/create-message.dto';
  import { MessagesService } from './messages.service';
  
  @Controller('messages')
  export class MessagesController {
    messageService: MessagesService;
  
    constructor() {
      // 마찬가지로 의존성 주입
      this.messageService = new MessagesService();
    }
    @Get()
    listOfMessages() {
      return this.messageService.findAll();
    }
  
    @Post()
    createMessages(@Body() body: CreateMessageDto) {
      // 우리가 메세지를 받아오는 타입을 CreatemessageDto에 지정했으므로 body에 있는 content값으로 가져와야함
      this.messageService.create(body.content);
    }
  
    @Get('/:id')
    getMessages(@Param('id') id: string) {
      return this.messageService.findOne(id);
    }
  }
  
  ```

#### 3. HTTP 통신

- Request 버튼을 눌러서 호출하면 다음과 같이 빈객체가 나오게 된다.

  ![image-20230910014918343](/Users/rok/Library/Application Support/typora-user-images/image-20230910014918343.png)

- 두 번째 생성하기 Request를 호출하면 다음과 같이 요청이 전송이 되고, 다시 첫 번째 목록 호출 Request를 호출하면 데이터가 들어간 것을 확인할 수 있다.

  ![image-20230910015053471](/Users/rok/Library/Application Support/typora-user-images/image-20230910015053471.png)

  ![image-20230910015156025](/Users/rok/Library/Application Support/typora-user-images/image-20230910015156025.png)

- 마지막으로 데이터를 몇 개 더 추가하고, 해당 id값으로 호출을 하면 해당 객체만 호출하는 것을 확인할 수 있다.

  ![image-20230910015629602](/Users/rok/Library/Application Support/typora-user-images/image-20230910015629602.png)

  ![image-20230910015710504](/Users/rok/Library/Application Support/typora-user-images/image-20230910015710504.png)


### 4. Error Exception

- 현재 특정 메세지를 찾을 때 id 값을 통해서 호출한다. 하지만 실제로 등록이 되지 않은 경우에도 메세지를 호출했을 때 다음과 같이 OK사인과 함께 에러가 출력되지 않는 것을 확인할 수 있다.

  ![image-20231003210741190](/Users/rok/Library/Application Support/typora-user-images/image-20231003210741190.png)

  일반적인 페이지는 페이지가 없으면 404코드와 함께 Not Found 메세지가 출력된다.

  ![image-20231003210858235](/Users/rok/Library/Application Support/typora-user-images/image-20231003210858235.png)

- 위와 같은 버그를 수정하기 위해서 코드를 수정해야 한다.

- messages.controller.ts

  ```typescript
  // 먼저 예외처리를 위한 의존성을 추가해 준다 => NotFoundException
  import { Controller, Get, Post, Body, Param, NotFoundException } from '@nestjs/common';
  import { CreateMessageDto } from './dtos/create-message.dto';
  import { MessagesService } from './messages.service';
  
  @Controller('messages')
  export class MessagesController {
    messageService: MessagesService;
  
    constructor() {
      // 마찬가지로 의존성 주입
      this.messageService = new MessagesService();
    }
    @Get()
    listOfMessages() {
      return this.messageService.findAll();
    }
  
    @Post()
    createMessages(@Body() body: CreateMessageDto) {
      // 우리가 메세지를 받아오는 타입을 CreatemessageDto에 지정했으므로 body에 있는 content값으로 가져와야함
      this.messageService.create(body.content);
    }
  	
  	// 순차적으로 진행을 시켜주기 위해 비동기 처리를 해줌 
    @Get('/:id')
    async getMessages(@Param('id') id: string) {
      // 바로 반환을 해준 코드를 변수에 담아주고 예외처리를 해준다.
      const msg = await this.messageService.findOne(id);
  
      // 예외처리
      if (!msg) {
        throw new NotFoundException('message does not exist!');
      }
      return msg;
    }
  }
  ```

- 코드 수정 후 실행을 했을 때 해당 값이 없는 경우는 아래와 같이 메세지를 출력하게 된다.

  ![image-20231003211025087](/Users/rok/Library/Application Support/typora-user-images/image-20231003211025087.png)