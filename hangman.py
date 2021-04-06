import random

HANGMAN_SUGGESTED_WORD_START_INDEX = 1
UNDER_BAR = "_"
INPUT_ATTEMPT_WORD_MESSAGE = "도전할 문자를 적어주세요 : "
INPUT_ATTEMPT_WRONG_WORD_MESSAGE = "올바른 형식으로 입력해주세요.(영어, 한글자)"
PRINTER_FINISH_GAME_MESSAGE = "MISSION COMPLETE: 행맨을 살렸습니다."
PRINTER_FAIL_GAME_MESSAGE = "GAME OVER: 행맨이 죽었습니다."
PRINTER_WRONG_LETTER_MESSAGE = "단어에 없는 문자입니다!"


hangman_suggested_word = {
    1: "orange",
    2: "apple",
    3: "watermelon",
    4: "people"
}


def main():
    run()


def input_attempt_word():
    input_word = input(INPUT_ATTEMPT_WORD_MESSAGE)
    return input_word

def check_input_attempt_word():
    while True:
        input_word = input_attempt_word()
        if input_word.isalpha() and len(input_word) == 1:
            break
        print(INPUT_ATTEMPT_WRONG_WORD_MESSAGE)
    return input_word

def printer_hangman(count):
    if count >= 1:
        head = "(.,.)"
    else:
        head = "     "
    if count >= 2:
        body = "|"
    else:
        body = " "
    if count >= 3:
        left_arm = "/"
    else:
        left_arm = " "
    if count >= 4:
        right_arm = "\\"
    else:
        right_arm = " "
    if count >= 5:
        left_leg = "/"
    else:
        left_leg = " "
    if count >= 6:
        right_leg = "\\"
    else:
        right_leg = " "

    print("----------")
    print("  |     ||")
    print("%s   ||" % head)
    print(" %s%s%s    ||" % (left_arm, body, right_arm))
    print("  %s     ||" % body)
    print(" %s %s    ||" % (left_leg, right_leg))
    print("        ||")
    print("     -----")


def printer_new_line():
    print()


def printer_wrong_letter():
    print(PRINTER_WRONG_LETTER_MESSAGE)


def printer_under_bar():
    print(UNDER_BAR, " ", end="")


def printer_matched_lettering(lettering):
    print(lettering, " ", end="")

def printer_hangman_answer_word(hangman_answer_word):
    print("제시된 단어 : ", hangman_answer_word)

def printer_finish_game():
    print(PRINTER_FINISH_GAME_MESSAGE)

def printer_fail_game():
    print(PRINTER_FAIL_GAME_MESSAGE)


def get_hangman_suggested_word_size():
    return len(hangman_suggested_word)


def get_hangman_answer_word():
    random_word_index = random.randint(HANGMAN_SUGGESTED_WORD_START_INDEX, get_hangman_suggested_word_size())
    hangman_answer_word = hangman_suggested_word.get(random_word_index)
    return hangman_answer_word

def is_fail_game(fail_count):
    if fail_count == 7:
        return True
    return False

def compare_suggested_word(attempt_word, hangman_answer_word):
    is_succeed = True

    for lettering in hangman_answer_word:
        if lettering in attempt_word:
            printer_matched_lettering(lettering)
        else:
            printer_under_bar()
            is_succeed = False

    return is_succeed

def append_letter_attempt_word(letter, attempt_word):
    if letter not in attempt_word:
        attempt_word += letter
    return attempt_word

def check_letter_in_answer_word(letter, hangman_answer_word, fail_count):
    if letter not in hangman_answer_word:
        printer_wrong_letter()
        printer_new_line()
        fail_count += 1
    return fail_count

def run():
    attempt_word = ""
    hangman_answer_word = get_hangman_answer_word()
    fail_count = 0
    while True:
        game_succeed = compare_suggested_word(attempt_word, hangman_answer_word)

        printer_new_line()

        if game_succeed:
            printer_finish_game()
            printer_hangman_answer_word(hangman_answer_word)
            break

        printer_new_line()

        letter = check_input_attempt_word()
        attempt_word = append_letter_attempt_word(letter, attempt_word)
        fail_count = check_letter_in_answer_word(letter, hangman_answer_word, fail_count)

        if is_fail_game(fail_count):
            printer_fail_game()
            break

        printer_hangman(fail_count)



if __name__ == "__main__":
    main()
