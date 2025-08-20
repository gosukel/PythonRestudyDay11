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

def play():
    playing = True
    p_hand = [draw_card(), draw_card()]
    p_total = get_hand_value(p_hand)

    cpu_hand = [draw_card(), draw_card()]
    cpu_total = get_hand_value(cpu_hand)
    while playing:
        print(f"dealers hand: [{cpu_hand[0]}, -]")
        print(p_hand)   
        print(f"current hand total: {p_total}")
        next_play = input("[h]it \n[c]all \n")
        if next_play.lower() != "h" and next_play.lower() != "c":
            continue
        if next_play.lower() == "h":
            p_hand.append(draw_card())
            p_total = get_hand_value(p_hand)
            did_overdraw = check_overdraw(p_total)
            if did_overdraw:
                print(p_hand)
                print(f"You drew {p_total} - Busted!  You lose...")
                playing = False
        if next_play.lower() == "c":
            playing = False
        while cpu_total < 17:
            cpu_hand.append(draw_card())
            cpu_total = get_hand_value(cpu_hand)
        print(f"dealers hand: {cpu_hand}")
        print(f"you hand: {p_hand}")
        print(f"final score\nYou: {p_total} \nDealer: {cpu_total}")
        if cpu_total > 21:
            print(f"The dealer busted with {cpu_total} - You win!")
        elif p_total > cpu_total:
            print("You win!")
        else:
            print("better luck next time pal...")
        again = input("play again?  [y]es or [n]o: ")
        if again.lower() == "y":
            play()
        else:
            print("see ya round, kid...")
                


play()

# dealers hand < 17, must draw
