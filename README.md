# 2week-Python-Practice

- Python을 이용해 단어맞추기 게임인 Hangman Game을 만들어봅시다.
- Dictionary, 반복문, 제어문 등을 이용해 함수형으로 만들 수 있도록 합니다.

## 함수 구성
- main(): run() 함수 실행
- run(): 전체적인 Hangman 게임 실행 코드


- input_attempt_word(): 플레이어가 시도해보고 싶은 단어를 입력
- check_input_attempt_word(): 플레이어가 입력한 단어가 조건에 맞는지 확인


- printer_new_lint(): 엔터
- printer_wrong_letter(): "단어에 없는 문자입니다!" 출력 함수
- printer_under_bar(): 언더바 출력 함수
- printer_matched_lettering: 일치하는 문자 출력 함수
- printer_finish_game(): "MISSION COMPLETE: 행맨을 살렸습니다." 출력 함수
- printer_fail_game(): "GAME OVER: 행맨이 죽었습니다." 출력 함수
- printer_hangman_answer_word(hangman_final_answer_word): 선택된 단어를 출력해주는 함수
- printer_hangman(count): 틀린 횟수에 따라 행맨 보여주는 함수


- get_hangman_suggested_word_size(): 단어리스트 길이
- get_hangman_answer_word(): 랜덤 모듈을 이용해 랜덤으로 단어 하나를 고르는 함수


- is_fail_game(fail_count): 게임의 패를 판단하는 함수
- compare_suggested_word(attempt_word, hangman_answer_word): 시도한 단어 문자열과 선택된 단어를 비교해 언더바와 글자로 출력해주는 함수. 언더바가 출력될 경우 성공한 것이 아니므로 False를 리턴한다.
- append_letter_attempt_word(letter, attempt_word): 시도한 단어 문자열에 입력한 글자가 없다면 넣어주는 함수
- check_letter_in_answer_word(letter, hangman_answer_word, fail_count): 선택된 단어에 입력한 글자가 없다면 fail_count를 증가하는 함수
- 
