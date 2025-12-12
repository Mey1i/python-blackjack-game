import random


def deal_card():
    cards = [11, 10, 10, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    return random.choice(cards)


def calculate_score(cards):
    score = sum(cards)

    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)

    return score

def play_blackjack():
    user_cards = []
    computer_cards = []


    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    game_over = False

    while not game_over:
        user_score = calculate_score(user_cards)
        comp_score = calculate_score(computer_cards)

        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")


        if user_score == 21 or comp_score == 21 or user_score > 21:
            game_over = True
        else:
            should_continue = input("Type 'y' to get another card, 'n' to pass: ")

            if should_continue == "y":
                user_cards.append(deal_card())
            else:
                game_over = True


    comp_score = calculate_score(computer_cards)
    while comp_score < 17:
        computer_cards.append(deal_card())
        comp_score = calculate_score(computer_cards)

    print("\n=== RESULTS ===")
    print(f"Your final cards: {user_cards}, final score: {user_score}")
    print(f"Computer's final cards: {computer_cards}, final score: {comp_score}")

 
    if user_score > 21:
        print("You bust. Computer wins!")
    elif comp_score > 21:
        print("Computer busts. You win!")
    elif user_score == comp_score:
        print("Draw!")
    elif user_score == 21:
        print("Blackjack! You win!")
    elif comp_score == 21:
        print("Computer got Blackjack. You lose.")
    elif user_score > comp_score:
        print("You win!")
    else:
        print("Computer wins!")


play_blackjack()
