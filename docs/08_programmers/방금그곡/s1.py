# 방금그곡_문제풀이
# 2022-04-08

# 음이 A#, C#, D#, F#, G# 데이터를 한단어로 변환해줘야 비교하기 편할거같아서 딕셔너리로 변환해준다.
# 악보 변환 12개여서 숫자로 표현하기 어려워 영어소문자로 표기
# 27번 테케의 경우 조건에 주어진 음표가 아닌경우가 있어서 런타임 에러가 발생했다
music_score = {
    'A': 'a', 'A#': 'b', 'B': 'c', 'C': 'd',
    'C#': 'e', 'D': 'f', 'D#': 'g', 'E': 'h',
    'F': 'i', 'F#': 'j', 'G': 'k', 'G#': 'm',
}


def change_score(data):
    res = ''
    i = 0
    while i < len(data):
        if (i+1) < len(data) and data[i+1] == '#':
            # 딕셔너리에서 값을 못찾을 경우
            if music_score.get(data[i:i+2]) == None:
                res += 'Z' # 연관없는 단어 넣어주기
            else:
                res += music_score[data[i:i+2]]
            i += 2
        else:
            res += music_score[data[i]]
            i += 1
    return res


# 분단위로 시간변환
def change_time(start_time, end_time):
    start = list(map(int, start_time.split(':')))
    end = list(map(int, end_time.split(':')))
    res = (end[0] - start[0]) * 60 + (end[1] - start[1])
    return res


def solution(m, musicinfos):
    answer = ''
    ans = change_score(m)
    play_time = 0
    for i in musicinfos:
        music_info = list(i.split(','))
        # 음악 재생시간, 제목, 악보
        music_time = change_time(music_info[0], music_info[1])

        if music_time < 0:
            music_time = 0
        music_title = music_info[2]
        music_data = change_score(music_info[3])
        # 데이터 만들기
        data = music_data * (music_time//len(music_data)) + music_data[:(music_time%len(music_data))]
        # 답이 데이터 안에 있을경우 동작
        if ans in data:
            # 플레이타임이 가장긴 음악을 선택해야 하므로
            if music_time > play_time:
                play_time = music_time
                answer = music_title

    if answer == '':
        answer = '(None)'
    return answer





print(solution('ABCDEFG',["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("CC#BCC#BCC#BCC#B", ["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))