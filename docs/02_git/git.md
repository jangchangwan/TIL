# git



1. 다른 커밋으로 이동
   1. `git log` : commit 한 로그 확인
      - ![image-20220115113930603](C:\Users\Changwan\Desktop\GIT\TIL\docs\02_git\git.assets\image-20220115113930603.png)
   2. `git check <로그번호>` : 해당 커밋했던 자료로 변경된다.
      - `git check -` :  최신 버전으로 업데이트
   
   

`Branch`

1. 사용하는 이유 

``` 
1. 새로운 기능추가
2. 버그 수정
3. 병합과 리베이스 테스트
4. 이전 코드 개선
```

2. `branch` 관련 명령어

   - `git branch [-v]` :  로컬 저장소의 브랜치 목록을 보는 명령
   - `git branch [-f] <브랜치이름> [커밋체크섬]` : 새로운 branch 생성
     - 커밋체크섬을 안줄경우 head로부터 branch를 생성
     - 이미 있는 branch를 다른 커밋으로 옮기고 싶을 경우 -f 에 옵션을 줘야함
   - `git branch -r[v]` : 원격 저장소에 있는 브랜치를 보고 싶을 때 사용
     - -v에 옵션을 추가하여 커밋을 볼 수 도 있다.
   - `git checkout <branch_name>` : 특정 브랜치로 들어갈때 사용한다.
   - `git checkout -b <branch_name> <commit_check>` : 특정 커밋에서 브랜치를 새로 생성하고 동시에 들어간다.
   - `git merge <대상 브랜치> `  : 현재 브랜치와 대상 브랜치를 병합할 때 사용한다.
   - `git rebase <대상 브랜치> ` : 내 브랜치의 커밋들을 대상 브랜치에 재배치시킴
   - `git branch -d <브랜치이름>` :특정 브랜치를 삭제할 때  사용함
     - head 브랜치와 병합이 되지 않은 브랜치는 삭제할 수 없습니다.

   - `git branch -D <브랜치이름>` : 브랜치를  강제로 삭제할 경우 사용



-  `git revert`  : 특정 커밋의 내용을 되돌리는 커밋

 



