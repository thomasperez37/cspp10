import random
def create_deck(month_groups):
    deck = {}
    points = ['20','10','05','00']
    japan_letters = ['__i','_ro','_ha','_ni','_ho','_he','_to','chi','___']
    for card in month_groups:
        if card[-1] == '4' or card[-1] == '3' and card[0:3] != 'nov':
            card_value = points[3] + japan_letters[8] + japan_letters[8]
        elif card[0:3] == 'jan':
            if card[-1] == '1':
                card_value = points[0] + japan_letters[8] + japan_letters[1]
            elif card[-1] == '2':
                card_value = points[1] + japan_letters[8] + japan_letters[2]
        elif card[0:3] == 'feb':
            if card[-1] == '1':
                card_value = points[1] + japan_letters[8] + japan_letters[2]
            elif card[-1] == '2':
                card_value = points[2] + japan_letters[8] + japan_letters[1]
        elif card[0:3] == 'mar':
            if card[-1] == '1':
                card_value = points[0] + japan_letters[0] + japan_letters[1]
            elif card[-1] == '2':
                card_value = points[1] + japan_letters[8] + japan_letters[2]
        elif card[0:3] == 'apr' or card[0:3] == 'may':
            if card[-1] == '1':
                card_value = points[1] + japan_letters[8] + japan_letters[5]
            elif card[-1] == '2':
                card_value = points[2] + japan_letters[8] + japan_letters[6]
        elif card[0:3] == 'jun':
            if card[-1] == '1':
                card_value = points[1] + japan_letters[8] + japan_letters[3]
            elif card[-1] == '2':
                card_value = points[2] + japan_letters[8] + japan_letters[4]
        elif card[0:3] == 'jul':
            if card[-1] == '1':
                card_value = points[1] + japan_letters[8] + japan_letters[5]
            elif card[-1] == '2':
                card_value = points[2] + japan_letters[7] + japan_letters[6]
        elif card[0:3] == 'aug':
            if card[-1] == '1':
                card_value = points[0] + japan_letters[8] + japan_letters[0]
            elif card[-1] == '2':
                card_value = points[2] + japan_letters[8] + japan_letters[7]
        elif card[0:3] == 'sep':
            if card[-1] == '1':
                card_value = points[1] + japan_letters[8] + japan_letters[3]
            elif card[-1] == '2':
                card_value = points[2] + japan_letters[4] + japan_letters[0]
        elif card[0:3] == 'oct':
            if card[-1] == '1':
                card_value = points[1] + japan_letters[8] + japan_letters[3]
            elif card[-1] == '2':
                card_value = points[2] + japan_letters[7] + japan_letters[4]
        elif card[0:3] == 'nov':
            if card[-1] == '1':
                card_value = points[1] + japan_letters[8] + japan_letters[8]
            elif card[-1] == '2' or card[-1] == '3':
                card_value = points[2] + japan_letters[8] + japan_letters[8]
        elif card[0:3] == 'dec':
            if card[-1] == '1':
                card_value = points[0] + japan_letters[8] + japan_letters[8]
            if card[-1] == '2':
                card_value = points[1] + japan_letters[8] + japan_letters[8]
        deck[card] = card[0:3] + card_value
    return deck
def print_score(pscore,cscore):
    print("Player Score: {}".format(pscore))
    print("Computer Score: {}".format(cscore))
def check_month_match(field_card,chosen_card):
    if field_card[0:3] == chosen_card[0:3]:
        return field_card[3:5] + chosen_card[3:5]
    else:
        return False
def check_yaku_match(card1,card2,card3):
    if card1[-3:] == '___' or card2[-3:] == '___' or card3[-3:] == '___':
        return False
    elif card1[5:8] == '___' and card2[5:8] == '___' and card3[5:8] == '___':
        if card1[-3:] == card2[-3:] and card2[-3:] == card3[-3:]:
            return True
        else:
            return False
    elif card1[5:8] == '___' and card2[5:8] == '___':
        if card1[-3:] == card2[-3:] and card2[-3:] == card3[5:8] or card1[-3:] == card2[-3:] and card2[-3:] == card3[-3:]:
            return True
        else:
            return False
    elif card2[5:8] == '___' and card3[5:8] == '___':
        if card1[-3:] == card2[-3:] and card2[-3:] == card3[-3:] or card1[5:8] == card2[-3:] and card2[-3:] == card3[-3:]:
            return True
        else:
            return False
    elif card1[5:8] == '___' and card3[5:8] == '___':
        if card1[-3:] == card2[-3:] and card2[-3:] == card3[-3:] or card1[-3:] == card2[5:8] and card2[5:8] == card3[-3:]:
            return True
        else:
            return False
    elif card1[5:8] == '___':
        if card1[-3:] == card2[-3:] and card2[-3:] == card3[-3:] or card1[-3:] == card2[-3:] and card2[-3:] == card3[5:8] or card1[-3:] == card2[5:8] and card2[5:8] == card3[5:8] or card1[-3:] == card2[5:8] and card2[5:8] == card3[-3:]:
            return True
        else:
            return False
    elif card2[5:8] == '___':
        if card1[-3:] == card2[-3:] and card2[-3:] == card3[-3:] or card1[-3:] == card2[-3:] and card2[-3:] == card3[5:8] or card1[5:8] == card2[-3:] and card2[-3:] == card3[5:8] or card1[5:8] == card2[-3:] and card2[-3:] == card3[-3:]:
            return True
        else:
            return False
    elif card3[5:8] == '___':
        if card1[-3:] == card2[-3:] and card2[-3:] == card3[-3:] or card1[-3:] == card2[5:8] and card2[5:8] == card3[-3:] or card1[5:8] == card2[5:8] and card2[5:8] == card3[-3:] or card1[5:8] == card2[-3:] and card2[-3:] == card3[-3:]:
            return True
        else:
            return False
    elif card1[-3:] == card2[-3:] and card2[-3:] == card3[-3:] or card1[-3:] == card2[-3:] and card2[-3:] == card3[5:8] or card1[-3:] == card2[5:8] and card2[5:8] == card3[-3:] or card1[5:8] == card2[-3:] and card2[-3:] == card3[-3:] or card1[-3:] == card2[5:8] and card2[5:8] == card3[5:8] or card1[5:8] == card2[5:8] and card2[5:8] == card3[-3:] or card1[5:8] == card2[-3:] and card2[-3:] == card3[5:8] or card1[5:8] == card2[5:8] and card2[5:8] == card3[5:8]:
        return True
    else:
        return False
def deal_player_cards(decko,months):
    your_cards = {}
    for card in range(8):
        card = card + 1
        chosen_month = random.choice(months)
        months.remove(chosen_month)
        value = decko[chosen_month]
        del decko[chosen_month]
        your_cards['card' + str(card)] = value
    return your_cards
def deal_field_cards(decko,montho):
    field_cards = {}
    for card in range(8):
        card = card + 1
        chosen_month = random.choice(montho)
        montho.remove(chosen_month)
        value = decko[chosen_month]
        del decko[chosen_month]
        field_cards['card' + str(card)] = value
    return field_cards
def give_options():
    print("You have 5 options. Type in \'match months\' to ")
    print("Type in \'match yaku cards\' to")
    print("Type in \'end turn\' to")
    print("Type in \'check cards\' to")
    print("Type in \'exit\' to end the program.")
    selected_option = input("Please choose one of the 5 options: ")
def hanafuda():
    months = ['jan1','feb1','mar1','apr1','may1','jun1','jul1','aug1','sep1','oct1','nov1','dec1',
            'jan2','feb2','mar2','apr2','may2','jun2','jul2','aug2','sep2','oct2','nov2','dec2',
            'jan3','feb3','mar3','apr3','may3','jun3','jul3','aug3','sep3','oct3','nov3','dec3',
            'jan4','feb4','mar4','apr4','may4','jun4','jul4','aug4','sep4','oct4','nov4','dec4',]
    deck = create_deck(months)
    player_deck = deal_player_cards(deck,months)
    print("Your Cards: {}".format(player_deck))
    field = deal_field_cards(deck,months)
    print("Field Cards: {}".format(field))
    print("--------------------------------")
    give_options()
    while chosen_option != 'exit' and end_game == False:
        