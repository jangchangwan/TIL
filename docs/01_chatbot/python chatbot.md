# 파이썬 챗봇

1. 텔레그램 설치



	1. 기존 휴대폰번호에 연동 후 파이썬 챗봇 검색후 시작
	2. 아무단어나 입력후  계정 연동 작업을 한다. 연결코드는 다시 챗봇에서 입력!



![image-20220114105242404](C:\Users\Changwan\Desktop\GIT\TIL\01_chatbot\python chatbot.assets\image-20220114105242404.png)



2. Web에서 텔레그램 사용하기위한 프로그램 설치

```
1. chrome 에서 Telegram extension 검색 후 Telegram for Chrome 설치
2. https://py.hphk.io 로 들어가서 로그인 후 파이썬 챗봇을 수정한다.
```



3. Chatbot 에서 기존 명령어에 코드를 추가하여 시험해보기

   -  안녕

     - ``` python
       # 아래에 코드를 작성하세요
       name = '장창완'
       team = '2반'
       location = '부울경'
       
       print(f'안녕하세요. \n\t {location} {team} {name}입니다.')
       print('안녕하세요. \n\t {} {} {}'.format(location,team,name))
       # \n : 줄바꿈
       # \t : 띄어쓰기
       # 문자열 내에 변수를 넣는방법 
       # 1. print(f'{변수1}{변수2}{변수3}')
       # 2. print('{}{}{}'.format(변수1,변수2,변수3))
       ```

   - 점심메뉴

     - ``` python
       # 아래에 코드를 작성하세요
       import random # 랜덤 라이브러리를 사용하겠다.
       orders = [0,1,2,3]
       # menu 리스트를 만드세요.
       menu = ['찐빵','라면','햄버거','김밥']
       # 전화번호부를 만드세요.
       nums = ['051-329-4291','031-324-6341','011-423-4442','010-4244-2332']
       picked = random.choice(orders)
       
       print('오늘의 메뉴는 {}이고 전화번호는 {}이다'.format(menu[picked],nums[picked]))
       for i in range(len(menu)):
           print('{}번 째 메뉴는 {}이고 번호는 {}이다'.format(i+1,menu[i],nums[i]))
       for idx, m in enumerate(menu):
       #enumerate를 쓸경우 변수로 index,menu를 설정해줘야한다
       	print('{}번 째 메뉴는 {}이고, 번호는 {}이다'.format(idx+1,menu[idx],nums[idx]))
       ```

       
