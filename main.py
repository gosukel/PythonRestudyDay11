import random

cards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
card_vals = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "10": 10,
    "J": 10,
    "Q": 10,
    "K": 10,
    "A": {
        "A_low": 1,
        "A_high": 11
    }
}

title_screen = '''
-------------------------------------
--------- B L A C K J A C K ---------
-------------------------------------'''

player_score = {
    "money": 100,
    "streak": 0,
}

def print_screen(cpu_hand, player_hand, player_hand_total, state="play"):
    new_screen = ''
    if state == "end":
        new_screen = f'''
Dealer's Hand - {cpu_hand} ({get_hand_value(cpu_hand)})
Your Hand     - {player_hand} ({player_hand_total}) '''
    else: 
        new_screen = f'''
Dealer's Hand - [{cpu_hand[0]}, -]    
Your Hand     - {player_hand} ({player_hand_total})
-------------------------------------'''
    print(new_screen)

def draw_card():
    card = random.choice(cards)
    return card

def get_hand_value(cards):
    hand = cards[:]
    total = 0
    while len(hand) > 0:
        card = hand.pop(0)
        if card == "A":
            if len(hand) > 0:
                hand.append(card)
            else:
                if total > 10:
                    total += 1
                else:
                    total += 11
            
            continue
        total += card_vals[card]
    
        
    return total

def check_overdraw(hand_total):
    if hand_total > 21:
        return True
    else:
        return False

def update_player_score(result):
    if result == "l":
        player_score["money"] = player_score["money"] - 10
        player_score["streak"] = 0
        return
    if result == "w":
        winnings = 10 
        if player_score["streak"] > 0:
            extra_winnings = 10 * (player_score["streak"] / 2)
            winnings += extra_winnings
        player_score["streak"] += 1 
        player_score["money"] += winnings
        return

def play():
    # INITIALIZE GAME STATE
    playing = True
    p_hand = [draw_card(), draw_card()]
    p_total = get_hand_value(p_hand)

    cpu_hand = [draw_card(), draw_card()]
    cpu_total = get_hand_value(cpu_hand)

    while playing:
        # START PLAY
        print(title_screen)
        print(f"${player_score['money']}                     Streak x{player_score['streak']}")
        print_screen(cpu_hand, p_hand, p_total)
        next_play = input("[h]it  -or-  [c]all \n")
        if next_play.lower() != "h" and next_play.lower() != "c":
            print("invalid selection")
            continue
        if next_play.lower() == "h":
            p_hand.append(draw_card())
            p_total = get_hand_value(p_hand)
            did_overdraw = check_overdraw(p_total)
            if did_overdraw:
                playing = False
                print(p_hand)
                print(f"You drew {p_total} - Busted!  You lose...")
                update_player_score("l")
            continue
            
        if next_play.lower() == "c":
            playing = False
            while cpu_total < 17:
                cpu_hand.append(draw_card())
                cpu_total = get_hand_value(cpu_hand)
            print_screen(cpu_hand, p_hand, p_total, state="end")
            if cpu_total > 21:
                print(f"The dealer busted with {cpu_total} - You win!")
                update_player_score("w")
            elif p_total > cpu_total:
                print("You win!")
                update_player_score("w")
            else:
                update_player_score("l")
                print("better luck next time pal...")
            print("-------------------------------------")
    again = input("play again?  [y]es or [n]o: ")
    if again.lower() == "y":
        play()
    else:
        print("see ya round, kid...")
                


play()


