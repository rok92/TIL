# TIL Day 01

> 2022년 05월 19일 목요일

## Why Git & Github?

![Git로고]( https://user-images.githubusercontent.com/49775540/168756716-68f9aebb-380f-4897-8141-78d8403f6113.png) 

### Git

- 분산 버전 관리 프로그램
-  백업, 복구, 협업을 위해 사용
- [Git 공식문서]( https://git-scm.com/book/ko/v2)

### Github

- Git을 사용하는 프로젝트의 협업을 위한 웹호스팅 서비스
- 포트폴리오를 자랑할 수 있는 공간
- 1일 1커밋 하기
- [이동욱님 Github 계정](https://github.com/jojoldu) 



## CLI

> CLI (Command Line Interface, 커맨드 라인 인터페이스)는 터미널을 통해 사용자와 컴퓨터가 상호 작용하는 방식을 뜻한다.

### 터미널 명령어 정리

| 명령어 |              설명              |
| ------ | :----------------------------: |
| mkdir  |           폴더 생성            |
| touch  |           파일 생성            |
| Is     |   현재 폴더의 파일 목록 출력   |
| cd     |        다른 폴더로 이동        |
| rm     | 파일 삭제 / 폴더 삭제(-r 옵션) |



### 예시

```bash
$ mkdir test

$ touch a.txt

$ ls
$ ls -a

$ cd ..
$ cd test

$ rm a.txt
$ rm -r test
```





## Visual Studio Code

> Visual Studio Code (비주얼 스튜디오 코드)는 마이크로소프트에서 개발한 텍스트 에디터의 한 종류이다.

### 장점

- Windows, Mac, Linux 운영체제를 모두 지원한다.
- 기존 개발 도구보다 빠르고 가볍다.
- Extension을 통해 다양한 기능을 설치할 수 있어서, 무한한 확장성을 가진다.
- 무료로 사용 가능하다.

### Git Bash 연동하기

1. 터미널을 연다. (Ctrl + `)
2. 화살표를 누르고 Select Default Profile을 클릭한다.
3. Git Bash를 선택한다.
4. 휴지통을 눌러서 터미널을 종료하고, 재시작한다.
   - 휴지통은 Kill Terminal 로써, 터미널 자체를 아예 종료한다.
   - 닫기는 Close Terminal 로써, 터미널을 종료하지 않고 창만 보이지 않게 만든다.
5. 기본 터미널이 Git Bash로 열리는지 확인한다.



## Markdown

> Markdown (마크다운)은 일반 텍스트 기반의 경량 Markup (마크업) 언어이다.

###Markup (마크업) 이란?

- 마크(Mark)로 둘러싸인 언어를 뜻한다. 마크란 글의 역할을 지정하는 표시이다.
- HTML도 마크업 언어인데, 글에 제목의 역할을 부여할 때 <h1>제목1</h1> 과 같이 작성한다.

### 마크다운의 장점과 단점

1. 장점
   - 문법이 직관적이고 쉽다.
   - 지원 가능한 플랫폼과 프로그램이 다양하다.
2. 단점
    - 표준이 없어서 사용자마다 문법이 상이하다.
    - 모든 HTML의 기능을 대신하지는 못한다.

### 주의 사항

- 마크다운의 본질은 글에 역할을 부여하는 것이다.
- 반드시 역할에 맞는 마크다운 문법을 작성한다. 글씨를 키우고 싶다고 해서 본문에 제목의 역할을 부여하면 안된다.

### 참고 자료

- [Markdown Guide](https://www.markdownguide.org/basic-syntax/)
- [마크다운 문법 정리](https://gist.github.com/ihoneymon/652be052a0727ad59601)

## Git 기초

1. Git 기초설정

   - 누가 커밋을 남겼는지 이름, 이메일 주소를 설정합니다.

     ```bash
     $git config --global user.name  "이름"
     
     bash$git config --global user.email  "000@naver.com"
     ```

   - 작성자가 올바르게 작성하였는지 확인 합니다.

     ```bash
     $git config --global -l  
     또는
     $git config --global -list
     ```

     

2. Git 기본 명령어
   - 로컬 저장소
     - Working Directory
       - 사용자의 일반적인 작업이 일어나는 공간
     - Staging Area
       - 커밋을 위한 파일 및 폴더가 추가되는 공간
     - Commit(Repository)
       - Staging Area에 있던 파일 및 폴더의 변경사항(커밋)을 저장하는 공간
     - Git의 버전관리 순서
       - Working Directory > Staging Area > Repository(Commit)
     
   - git init
   
     ```bash
     $git init
     Initialized empty Git repository in c:/users/kyeon/ooo/.git/
     
     kyeon@KYEON MING64 ~/ooo(master)
     ```
   
     - 현재 작업중인 디렉토리를 git으로 관리 한다는 명령어
     - git 이라는 숨김폴더를 생성하고, 터미널에는 (master)라고 표기됩니다.
     
   - git status(가장 중요한 명령어)
   
     ```bash
     $ git status
     On branch master
     
     No commits yet
     
     nothing to commit (create/copy files and use "git add" to track)
     ```
   
     - Working Directory와 Staging Area에 있는 파일의 현재 상태를 알려주는 명령어
   
     - 어떤 작업을 수행할 때 수시로 status확인하는 습관을 들이면 좋습니다
   
     - 상태
   
       1. Untracked : Git이 관리하지 않는 파일(한 번도 Staging Area에 올라가지 않은 파일)
   
       2. Tracked : Git이 관리하는 파일
   
          a. Unmodified : 최신상태
   
          b. Modified : 수정되었지만 아직 Staging Area에 올라가지는 않은 상태
   
          c. Staged : Staging Area에 올라간 상태
          
   
   - git add
   
     ```bash
     # 특정 파일
     $ git add a.txt
     
     # 특정 폴더
     $ git add my_folder/
     
     # 현재 디렉토리에 속한 파일/폴더 전부
     $ git add .
     ```
   
     - Working Directory에 있는 파일을 Staging Area로 올리는 명령어
   
     - Git이 해당 파일을 추적(관리)할 수 있도록 만듭니다.
   
     - Untracked, Tracked > Staged 로 상태를 변경합니다
   
     - Ex)
   
       ```bash
       $ touch a.txt b.txt
       
       $ git status
       On branch master
       
       No commits yet
       
       Untracked files: # 트래킹 되고 있지 않는 파일 목록
         (use "git add <file>..." to include in what will be committed)
               a.txt
               b.txt
       
       nothing added to commit but untracked files present (use "git add" to track)
       ```
   
       ```bash
       # a.txt만 Staging Area에 올립니다.
       
       $ git add a.txt
       ```
   
       ```bash
       $ git status
       
       On branch master
       
       No commits yet
       
       Changes to be committed: # 커밋 예정인 변경사항(Staging Area)
         (use "git rm --cached <file>..." to unstage)
               new file:   a.txt
       
       Untracked files: # 트래킹 되고 있지 않은 파일
         (use "git add <file>..." to include in what will be committed)
               b.txt
       ```
   
   - git commit
   
     ```bash
     $ git commit -m "first commit"
     [master (root-commit) c02659f] first commit
      1 file changed, 0 insertions(+), 0 deletions(-)
      create mode 100644 a.txt
     ```
   
     - Staging Area에 올라온  파일의 변경사항을 하나의 버전(커밋)으로 저장하는 명령어
     - 커밋 메세지는 현재 변경사항들을 잘 나타낼 수 있도록 의미있게 작성하는 것이 좋습니다.
     - 각각 커밋은 SHA-1알고리즘에 의해 반환된 고유의 해시 값을 ID로 가집니다.
   
   - git log
   
     ```bash
     $ git log
     commit 1870222981b4731d14ef91d401c68c0bbb2f6e7d (HEAD -> master)
     Author: kyle <kyle123@hphk.kr>
     Date:   Thu Dec 9 15:26:46 2021 +0900
     
         first commit
     ```
   
     - 커밋의 내역(ID, 작성자, 시간, 메세지 등)을 조회할 수 있는 명령어
     - 옵션
       - --oneline > 한 줄로 축약해서 보여줍니다.
       - --graph > 브랜치와 머지 내역을 그래프로 보여줍니다.
       - --all > 현재 브랜치를 포함한 모든 브랜치의 내역을 보여줍니다.
       - --reverse > 커밋 내역의 순서를 반대로 보여줍니다.(최신내역이 가장 아래)
       - -p > 파일의 변경내용도 같이 보여줍니다.
       - -2 > 원하는 갯수만큼 내역을 보여줍니다(2말도 다른 숫자 사용가능)