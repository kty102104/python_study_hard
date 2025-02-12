# 사용하는 파일 import
import random
#import hangman_arts -> import hangman_word_list와 동일한 방법
from hangman_arts import logo, stages   # from - import 문
import hangman_word_list

print(logo) # from - import문으로 작성하면 파일(모듈)명을 명시하지 않아도 됨.

# hangman_word_list.py 파일에 있는 변수인 word_list를 가지고 와서,
# random.choice()를 적용하는 방법
chosen_word = random.choice(hangman_word_list.word_list)

'''
hangman_word_list에 있는 word_list를 가지고 와서 random.choice를 적용시키려면
어떻게 해야 할지 코드를 작성하시오.

이제 hangman 만드세요.
'''

display = []
used_alphabet = []

for _ in chosen_word:
    display.append("_")

lives = 6

end_of_game = False

while not end_of_game:
    guess = input("알파벳 입력 >>> ").lower()
    for i in range(len(chosen_word)):
        if chosen_word[i] == guess:
            display[i] = guess

    if guess not in chosen_word:
        lives -= 1
        used_alphabet.append(guess)
        print(stages[lives])
        print(f"당신의 기회는 {lives}번 남았습니다.")
        if lives == 0:
            print("모든 기회를 잃었습니다.")
            print(f"정답은 {chosen_word} 입니다.")

            end_of_game = True

    print(" ".join(display))
    print(f"사용한 알파벳 : {used_alphabet}")

    if not "_" in display:
        print("정답입니다!")
        break
