import random

HANGMAN_SUGGESTED_WORD_START_INDEX = 1
UNDER_BAR = "_"
PRINTER_FINISH_GAME_MESSAGE = "game 이 끝났습니다!"
PRINTER_WRONG_LETTER_MESSAGE = "잘못된 문자가 들어가 있습니다!"
INPUT_ATTEMPT_WORD_MESSAGE = "도전할 단어를 적어주세요 : "

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


def printer_people(count):
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
    print("  |    || ")
    print("%s  || " % head)
    print(" %s%s%s   || " % (left_arm, body, right_arm))
    print("  %s    || " % body)
    print(" %s %s   || " % (left_leg, right_leg))
    print("       || ")
    print("----------")


def printer_new_line():
    print()


def printer_wrong_letter():
    print(PRINTER_WRONG_LETTER_MESSAGE)


def printer_under_bar():
    print(UNDER_BAR, " ", end="")


def printer_matched_lettering(lettering):
    print(lettering, " ", end="")


def printer_finish_game():
    print(PRINTER_FINISH_GAME_MESSAGE)


def printer_hangman_suggested_word(hangman_final_answer_word):
    print("제시된 단어 : ", hangman_final_answer_word)


def get_hangman_suggested_word_size():
    return len(hangman_suggested_word)


def get_hangman_final_answer_word():
    random_word_index = random.randint(HANGMAN_SUGGESTED_WORD_START_INDEX, get_hangman_suggested_word_size())
    hangman_final_answer_word = hangman_suggested_word.get(random_word_index)
    return hangman_final_answer_word


def compare_suggested_word(attempt_word, hangman_final_answer_word):
    is_succeed = True

    for lettering in hangman_final_answer_word:
        if lettering in attempt_word:
            printer_matched_lettering(lettering)
        else:
            printer_under_bar()
            is_succeed = False

    return is_succeed


def run():
    attempt_word = ""
    hangman_final_answer_word = get_hangman_final_answer_word()
    fail_count = 0
    while True:
        game_succeed = compare_suggested_word(attempt_word, hangman_final_answer_word)

        if game_succeed:
            printer_finish_game()
            printer_hangman_suggested_word(hangman_final_answer_word)
            break

        printer_new_line()

        letter = input_attempt_word()

        # 분리
        if letter not in attempt_word:
            attempt_word += letter

        # business logic 분리
        if letter not in hangman_final_answer_word:
            printer_wrong_letter()
            fail_count += 1
        if fail_count == 7:
            print("행맨이 죽었습니다!!")
            break
        printer_people(fail_count)



if __name__ == "__main__":
    main()
