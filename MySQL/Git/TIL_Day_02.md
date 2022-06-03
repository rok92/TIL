## .gitignore

1. .gitignore

   > 특정 파일 혹은 폴더에 대해 Git이 버전관리를 하지 못하도록 지정하는 것

- .gitignore에 작성하는 목록

  - 민감한 개인 정보가 담긴 파일(전화번호, 계좌번호, 비밀번호, 주민등록번호, API Key 등)
  - Os운영체제에서 활용되는 파일
  - IDE(통합 개발 환경) 혹은 Text-editor(vscode)등에서 활용되는 파일
    - 예>pycharm -> .idea/

  - 개발언어(java, python) 혹은 프레임워크(Spring)에서 사용되는 파일
    - 가상환경 : venv/
    - __ pycache __

- .gitignore 작성시 주의사항
  - 반드시 .gitignore로 작성해야 합니다. (.)은 숨김 파일 이라는 뜻입니다.
  - .gitignore파일은 .git폴더와 동일한 위치에 생성합니다.
  - __제외하고 싶은 파일은 반드시 git add전에 .gitignore에 작성합니다.__

- .gitignore 쉽게 작성하기
  - .gitignore를 쉽게 작성할 수 있는 사이트 2개
  - [사이트1]([gitignore.io - 자신의 프로젝트에 꼭 맞는 .gitignore 파일을 만드세요 (toptal.com)](https://www.toptal.com/developers/gitignore/)), [사이트2]([github/gitignore: A collection of useful .gitignore templates](https://github.com/github/gitignore))

## Clone, Pull

1. 원격 저장소 가져오기

   >원격저장소의 내용을 로컬 저장소로 가져오는 방법(clone, pull) > 협업

- __git clone__ 

  - 원격 저장소의 커밋 내역을 모두 가져와서, 로컬 저장소를 생성하는 명령어 입니다.

  - clone은 복제라는 의미로 git clone 명령어를 사용하면 원격 저장소를 통째로 복사(다운로드)해서 로컬컴퓨터(Personal Computer)로 옮길 수 있다.

  - 순서

    - 먼저 클론(다운로드)할 깃허브의 주소를 복사해서 저장할 장소의 폴더로 가서 git bash here를 한다.

      <img src="TIL_Day_02.assets/복제.JPG" style="zoom:50%;" />

    - $git clone https://github.com/000/0000000.git 입력후 enter

      <img src="TIL_Day_02.assets/image-20220520202926711.png" alt="image-20220520202926711" style="zoom: 50%;" />

    - clone하려는 폴더가 생긴다.

      

- __Pull__

  - vscode를 오픈하고 Terminer을 실행하여 깃허브에 있는 업데이트되어 있는 파일들을 끌어온다.

    $git pull origin master

    ![image-20220520203642490](TIL_Day_02.assets/image-20220520203642490.png)

  - ```bash
    $ git pull origin master
    From https://github.com/edukyle/git-practice
     * branch            master     -> FETCH_HEAD
    Updating 6570ecb..56809a9
    Fast-forward
     README.md | 1 +
     1 file changed, 1 insertion(+)
    
    
    [풀이]
    git 명령어를 사용할건데, origin이라는 원격 저장소의 master 브랜치의 내용을 가져온다(pull).
    ```

    