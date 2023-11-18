def runUpDown():
    answer = random.randrange(1, 10)
    chance = 3

#2. 내가 맞춘 정답들이 어디에 위치해있는지 알 수 없음
#-> s _ _ s _ _ _출력
# print CorrectWords ()함수를 선언해서 그안에서 입력되었던 맞는 항목들 위치에 맞게 출력


        #a.find(b) -> b가 a에 없으면 -1을 출력






     #기회가 8번 이상 틀렸을 때는 GAME OUT
     #




def runupdown():
    def runUpDown():
        answer = random.randrange(0, 10)
        chance = 3

        # 사용자가 answer 맞출때까지 반복
        # 1. 사용자에게 기회주기(3번)
        # 2. 틀렸을때 updown 출력해주기


        while chance > 0:
            user_input = int(input("값을 입력하세요 >>"))

            if user_input == answer:
                print("정답입니다!")
                break
            else:
                chance = chance - 1
                if user_input > answer:
                    print("down")
                else:
                    print("up")


userInput = -1

while userInput != 0:
    menuPrint()
    userInput = int(input("SELECT MENU ::: "))

    if userInput == 1:
        runHangman()
    elif userInput == 2:
        runUpDown()