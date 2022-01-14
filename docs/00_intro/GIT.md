### GIT 명령어.ZIP

##### * 내 컴퓨터에서 최초로 `깃-깃허브` 매핑시켜줄때

* username, pw
* chrome
  * git / django, javascript, vue 

1. `git_config_--global_user.username_'<username>'` : username 등록

   * 확인하고싶을때 잘 들어갔는지?

     * `git config --global user.username`

       * ```
         edujihye
         ```

2. `git config --global user.email '<email>'` : email등록

   * 확인하고 싶을때 잘 들어갔는지?

     * `git config --global user.email`

       * ```
         edujihye21@gmail.com
         ```



##### * Working Directory (내 로컬에서 폴더 만들었을 때만 ***1회***) 

* `git init` : git 시작
* `git remote add origin <git repo url>` : repo 연결

​		Hi, it's me jihye

- `git push -u origin master` :  첫 푸쉬할때 사용
  - `git remote add origin __`안될시 입력후 다시 푸쉬

##### Staging Area(.git) ***N회***

* `git remote`  : remote 별명확인
* `git remote -v` : remote 주소 확인

* `git add .` : `.` 전부다!!!! 
* `git add 파일명.확장자` : 특정 파일만 올려
* `git status` :  `add`가 잘 됐는지 확인
* `git commit -m '<commit message>'` :  why 를 적어주





### git clone : git에 있는 자료를 복제하는법

- `git init` : 생성후.

- `git clone <git url>` : 복제한다.

  

`clone`  :  복제

`pull` : 수정하기위해 가져오는 것



### git pull

- `git init`

- `git remote add origin <git url>`

- `git pull origin master`

  