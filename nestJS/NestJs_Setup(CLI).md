## Nest Project Setup(CLI)

#### 1. NestCLI 설치 And Create new Project

- NestCLI 설치하기

  - `npm install -g  @nestjs/cli` 명령어를 터미널에서 실행하여 전역으로 설치를 해준다. 
    - 만약 설치가 되지 않는다면 `sudo npm install -g @nestjs/cli` 명령어를 통해 관리자 모드로 설치를 진행하면 된다.(환경설정에 따라 차이가 있다.)

-  Nest Project 생성하기

  - `nest new [프로젝트 이름]` 다음 명령어를 새로 생성할 프로젝트 네임과 함께 터미널에 입력해주면 간단하게 새로운 프로젝트가 만들어진다.

  - Process

    - 프로젝트이름과 함께 설치

    ![image-20230825181124312](/Users/rok/Library/Application Support/typora-user-images/image-20230825181124312.png)

    - npm, yarn, ppm 중 선택

    ![image-20230825181237824](/Users/rok/Library/Application Support/typora-user-images/image-20230825181237824.png)

    - 완료

    ![image-20230825181324903](/Users/rok/Library/Application Support/typora-user-images/image-20230825181324903.png)

#### 2. Practice Simple Project

- **Project Name: messages**

- 프로젝트의 로직

  1. Get방식으로 전체 메세지의 리스트를 요청하는 로직으로 구현

     - 단지 리스트 전체를 호출하기 위함이기 때문에 Pipe, Guard와 같은 기능은 현재는 필요하지 않다.

     - 실제 프로젝트구성에서는 Repository의 역할은 MySQL, MongoDB와 같은 데이터베이스를 이용하지만 여기서는 파일로 대체하여 구성

       ![image-20230827012232752](/Users/rok/Library/Application Support/typora-user-images/image-20230827012232752.png)

  2. Post요청을 통해서 새로운 메세지를 입력하는 로직

     - 여기서는 요청데이터가 있기 때문에 Pipe기능이 필요하다.

       ![image-20230827014010206](/Users/rok/Library/Application Support/typora-user-images/image-20230827014010206.png)

  3. Get요청으로 사용자가 특정 id로 부터 메세지를 받는 로직

     - 사용자가 특정 Id로 메세지 받기

       ![image-20230827014936526](/Users/rok/Library/Application Support/typora-user-images/image-20230827014936526.png)

- NestJS(CLI)로 파일 자동생성 및 프로젝트 셋업

  1. 모듈 생성

     - `nest generate module messages` 명령어로 모듈을 생성한다.

       => 위 명령어를 실행하면 src폴더안에 messages라는 폴더명이 생성되고 그 안에 모듈이 자동으로 생성된다.

  2. 컨트롤러 생성

     - `nest generate controller messages/messages --flat` 명령어로 컨트롤러를 생성한다.

       => 이 때 --flat을 쓰지 않으면 controllers 폴더를 생성하고 그 안에 컨트롤러 파일을 생성하게 된다. (필요에 따라 사용할 수 있음.)

       => 위 명령어로 컨트롤러를 생성하게 되면 자동으로 모듈에 사용할 컨트롤러가 등록까지 된다.

  3. 라우팅 설정

     - 로직을 설명할 때 요청방식을 이미 정해둔 것이 있다.

     - Get, Post 요청으로 메세지를 생성하고 받고, 전체 리스트를 가져오는 기능을 구현한다.

     - 방법 1 : 모든 라우팅은 messages라는 경로를 통해서 요청이 들어간다. 따라서 Get, Post 데코레이터 안에 messages를 넣어준다.

       ```ty
       import { Controller, Get, Post } from '@nestjs/common';
       
       @Controller()
       export class MessagesController {
         @Get('/messages')
         listOfMessages() {}
       
         @Post('messages')
         createMessages() {}
       
         @Get('/messages/:id')
         getMessages() {}
       }
       ```

     - 방법 2: 매번 messages라는 문구를 넣어주기 번거롭기 때문에 모든 경로를 messages라는 경로로 바로 갈 수 있게 controller 데코리에너 안에 messages를 넣어준다

       ```ty
       import { Controller, Get, Post } from '@nestjs/common';
       
       @Controller('messages')
       export class MessagesController {
         @Get()
         listOfMessages() {}
       
         @Post()
         createMessages() {}
       
         @Get('/:id')
         getMessages() {}
       }
       ```

       