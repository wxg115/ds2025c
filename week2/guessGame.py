import random

win = False
guess = 0
cnt = 1
answer = random.randint(1, 100)

while cnt < 7:
    guess = int(input("정수 입력: "))
    print(f"{7-cnt}번의 기회가 남았습니다.")
    cnt += 1

    if answer == guess:
        print("정답입니다.")
        win = True
        break
    elif answer > guess:
        print("입력한 수는 정답보다 작은 수입니다.")
    else:
        print("입력한 수는 정답보다 큰 수입니다.")

if win == True:
    print("승리")
else:
    print("패배")
