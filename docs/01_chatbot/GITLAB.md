# GITLAB



gitlab  = Project   

github = Repo 가 동일하다

`--global` : 전역, 현재위치 뿐만 아니라 전체가 참조할 수 있음

`--local` : 지역, 현재 위치에서만 참조함



### Gitlab 시작하기

- 최초 한번만 할것

1. 폴더 생성
2. `git init`

3. `git config --local user.name '이름'`
4. `git config --local user.email 'e-mail'`
5. `git remote add origin url`
6. `git remote -v` : 확인용
7. `git pull origin master`
8.  Git Credential 나오면
   - username : `email`
   - pw : S(이메일)7   or 변경된 비밀번호로!

​	



- 자료올릴때 ( 보통 하면 안된다.)

  - `git add`

  - `git status`

  - `git commit -m '오늘도 화이팅'`

    

  

- 자료 받을때 ( 받을 때마다 )
  - `git pull origin master` 





- `master` : 최초로 만든사람 main Branch 

  

  ![image-20220114102008271](C:\Users\Changwan\Desktop\GIT\TIL\01_chatbot\GITLAB.assets\image-20220114102008271.png)

  1. `Git Branch` 의 종류

     1. `HOTFIX` : 최우선적으로 수정해야 할 것
     2. `PUBLISH` :  사용하고있는 것
     3. `MASTER` : 최선
     4. `DEVELOP` : 수정
     5. `FEATURE`

     



## CRLF  정의 를 공부할것

CR = mac   LF = window  둘의

- git config --global core.autocrlf true   : crlf 오류 없애는 방법







