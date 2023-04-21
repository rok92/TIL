# Mysql 삭제하는 방법(Mac)

#### homebrew를 이용한 방법

###### 1. 먼저 실행되어 있는 mysql server를 멈춥니다.

`mysql.server stop` 명령어를 실행시켜 줍니다.

##### 2. 관련 파일 삭제

- 위치 확인하기

  `which mysql`명령어를 실행시켜 주면 위치를 확인 시켜줌으로써 mysql이 설치되어 있다는 것을 알 수 있습니다.

- mysql 삭제

  `brew uninstall --force mysql`  명령어를 실행시켜 줌으로써 삭제합니다.
  
- 잔여 파일들 삭제

  ```mysql
  sudo rm -rf /usr/local/mysql
  sudo rm -rf /usr/local/bin/mysql
  sudo rm -rf /usr/local/var/mysql
  sudo rm -rf /usr/local/Cellar/mysql
  sudo rm -rf /usr/local/mysql*
  sudo rm -rf /tmp/mysql.sock.lock
  sudo rm -rf /tmp/mysqlx.sock.lock
  sudo rm -rf /tmp/mysql.sock
  sudo rm -rf /tmp/mysqlx.sock
  sudo rm ~/Library/LaunchAgents/homebrew.mxcl.mysql.plist
  sudo rm -rf /Library/StartupItems/MySQLCOM
  sudo rm -rf /Library/PreferencePanes/My*
  ```

  한 줄씩 입력하여 삭제해주고 재부팅합니다.

##### 3. 재설치

- 설치하기

  `brew install mysql` 명령어 실행

- 서버 시작하기

  `mysql.server start` 명령를 실행했을 때 'SUCCESSFUL'이 뜨면 재대로 실행된 것 입니다.

- 비밀번호 설정

  `mysql -uroot` 명령어로 비밀번호 입력 없이 root에 로그인 후

  `mysql_secure_installation` 명령어로 비밀번호를 설정해 줍니다.

##### 4. 혹시 완벽히 제거가 되지 않을 경우(이럴 경우 재설치시 실행하면 에러가 납니다.)

- 환경설정에 따라 가끔 완벽하게 파일들이 지워지지 않거나 재설치를 했을 때 기존파일과 겹쳐 실행이 안되는 경우가 있습니다.

  저의 경우 homebrew를 지우고 재설치 했으나 /tmp/homebrew/ 경로에 잔여파일들이 남아있어 하나하나 확인하기 힘들었습니다.

  그래서 homebrew를 재설치 하는 방법을 선택했습니다.

- `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/uninstall.sh)"` 먼저 이 명령어로 삭제 후 위에서 말한 경로에 homebrew가 없어진지 확인합니다. 만약 계속 있을 경우 home-brew 폴더를 삭제해 주고 재설치 하면 됩니다.

- 재설치

  `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"` 명령어를 실행하고 `brew --verion` 명령어를 통해 버전을 확인하면서 재설치 된 것을 알 수 있습니다.

