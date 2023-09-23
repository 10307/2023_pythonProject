#f(x) = 3x +5

def tmpFunction(x):
    return 3 * x + 5

print (tmpFunction(5))

#함수는 기능을 쪼갠다
#게임
# 화면 뿌려주기 <- 기능
# 랜덤값 할당받기 <- 기능
# 사용자 입력받기 <- 기능
# 값이랑 사용자 입력 비교하가 <- 기능
# 결과 분석하기


# _ _ _ _ _
# 있으면 통과, 없으면 1데카
# 데카가 n개 이상이면 out

# 게임선택 -> 행맨, updown , 종료
# "행맨"
# -> 랜덤으로 단어 선정
# -> 사용자 입력받기
# -> 결과판단

def menuPrint():
    print("=======GAME=======")
    print("1. 행맨")
    print("2. 업다운")
    print("0. 종료")
    print("==================")

def getRandomWord():
        words = ["hang", "pretty", "apple", "ant", "water", "samsung", "MCdonalds", "fluent", "voca", "galaxy"]
        return words[random.randrange(0, len(words))]

hangman_input_history = []

def getHangmanInput():
    while True:
        user_input = input("Input alphabet ::: ")
        if(user_input.isalpha()):
            alphabet = user_input[0].lower()
            if(hangman_input_history.index(alphabet)):
                print("이미 입력한 값입니다. 새로운 알파벳을 입력해주세요.")
            else:
                return alphabet

def runHangman():
   hangman_input_history = []
   word = getRandomWord()
   alphabet = getHangmanInput()

    user_input = getHangmanInput()


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

while userInput !=0:
    menuPrint()
    userInput = int(input("SELECT MENU :::"))

    if userInput == 1:
        runHangMan()
    elif userInput == 2:
        runupdown()

        # 전역변수 :전지역 사용가능
        # 지역변수 :정해진 지역 사용가능