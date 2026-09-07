import random


def guess_number(computer_number, client_remaining_attempt):
    count = 0
    player = True
    while client_remaining_attempt > 0:
        count += 1
        client_remaining_attempt -= 1
        client_guess = int(input())

        if client_remaining_attempt == 0:
            if client_guess == computer_number:
                pass
            else:
                player = False
                break

        if computer_number > client_guess:
            print(
                f"ohhh, your guess is small {client_remaining_attempt} attempts remaining"
            )

        elif computer_number < client_guess:
            print(
                f"ohhh, yours is so big! {client_remaining_attempt} attempts remaining"
            )

        else:
            print("GZ mate you WON!")
            player = True
            break
    return count, client_remaining_attempt, player


def select_difficulty():
    difficulty_selected = False
    while difficulty_selected == False:
        client_choose = int(input())
        if client_choose == 1:
            computer_number = random.randint(1, 10)
            client_remaining_attempt = 7
            difficulty_selected = True
        elif client_choose == 2:
            computer_number = random.randint(1, 50)
            client_remaining_attempt = 5
            difficulty_selected = True
        elif client_choose == 3:
            computer_number = random.randint(1, 100)
            client_remaining_attempt = 3
            difficulty_selected = True
        else:
            print("Invalid choice!")
    return computer_number, client_remaining_attempt, client_choose


def game_result(result, computer_number, player, point):
    if player == True:
        print(f"you found with {result} attempt ")
        print(f"you also get {point} POINT ! from 100 point")
    elif player == False:
        print(f"ahhh you lost sorry the computer number was {computer_number}")


def point_calculator(attempts, dificalty):
    point = 0
    if dificalty == 1:
        if attempts == 1:
            point = 100
        elif attempts == 2:
            point = 75
        elif attempts in (3, 4, 5):
            point = 50
        elif attempts == 6:
            point = 20
    elif dificalty == 2:
        if attempts == 1:
            point = 100
        elif attempts == 2:
            point = 75
        elif attempts in (3, 4):
            point = 50
        elif attempts == 5:
            point = 20
    elif dificalty == 3:
        if attempts in (3, 2):
            point = 100
        elif attempts == 1:
            point = 75
    return point


playing = True
while playing:
    print("welcome to guess game please select your dificulty")
    print("1. Easy 2. Medium 3. Hard")
    computer_number, client_remaining_attempt, clinet_chose = select_difficulty()
    print("game start please write your answer")
    print(f"btw you have only {client_remaining_attempt} ateempts")
    result, attempts, player = guess_number(computer_number, client_remaining_attempt)
    point = point_calculator(result, clinet_chose)
    game_result(result, computer_number, player, point)
    print("do you wana play again?")
    client_Answer = input()
    if client_Answer.lower() == "yes":
        playing = True
    else:
        playing = False
