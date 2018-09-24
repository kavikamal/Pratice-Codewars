"""
A famous casino is suddenly faced with a sharp decline of their revenues.
They decide to offer Texas hold'em also online. Can you help them
by writing an algorithm that can rank poker hands?
Task:

Create a poker hand that has a method to compare itself to another poker hand:
    compare_with(self, other_hand)
A poker hand has a constructor that accepts a string containing 5 cards:
    PokerHand(hand)
The characteristics of the string of cards are:
A space is used as card seperator
Each card consists of two characters
The first character is the value of the card, valid characters are:
2, 3, 4, 5, 6, 7, 8, 9, T(en), J(ack), Q(ueen), K(ing), A(ce)
The second character represents the suit, valid characters are:
S(pades), H(earts), D(iamonds), C(lubs)

The result of your poker hand compare can be one of these 3 options:
    RESULT = ["Loss", "Tie", "Win"]
Apply the Texas Hold'em rules for ranking the cards.
There is no ranking for the suits.

"""


class PokerHand(object):

    RESULT = ["Loss", "Tie", "Win"]
    card_value = {"2": 2, "3": 3, "4": 4,
                  "5": 5, "6": 6, "7": 7,
                  "8": 8, "9": 9, "T": 10,
                  "J": 11, "Q": 12, "K": 13, "A": 14}
    final_value = []

    def __init__(self, hand):
        temp_hand_list = hand.split()
        self.hand_list = []
        for hand in temp_hand_list:
            self.hand_list.append((self.card_value[hand[0]], hand[1]))
        self.hand_list = sorted(self.hand_list, key=lambda x: x[0])
        self.card_numbers, self.card_shapes = zip(*self.hand_list)

    def compare_with(self, other):
        self.final_value = self.find_result()
        other.final_value = other.find_result()
        if self.final_value[0] > other.final_value[0]:
            return self.RESULT[2]
        elif self.final_value[0] < other.final_value[0]:
            return self.RESULT[0]
        elif self.final_value[0] == other.final_value[0]:
            if self.final_value[1] > other.final_value[1]:
                return self.RESULT[2]
            elif self.final_value[1] < other.final_value[1]:
                return self.RESULT[0]
            else:
                if self.final_value[0] in [8, 7, 6, 4, 3, 2, 1]:
                    filtered_res = set(self.final_value[2]) ^ set(
                        other.final_value[2])
                    if len(filtered_res) == 0:
                        return self.RESULT[1]
                    elif max(filtered_res) in self.card_numbers:
                        return self.RESULT[2]
                    elif max(filtered_res) in other.card_numbers:
                        return self.RESULT[0]
                else:
                    return self.RESULT[1]

    def find_result(self):
        """10: 'Royal flush' 9: 'Straight flush' 8: 'Four of a kind'
           7: 'Full house' 6: 'Flush' 5: 'Straight' 4: 'Three of a kind'
           3: 'Two pairs' 2: 'Pair' 1: 'Highcard'"""
        result_val = [0, 0]
        if self.check_flush():
            # 6: 'Flush'
            result_val = [6, max(self.card_numbers),
                          list(set(self.card_numbers))]
        if self.check_straight():
            if result_val[0] == 6:
                if max(self.card_numbers) == 14:
                    # 10: 'Royal flush'
                    result_val = [10, max(self.card_numbers), list(
                        set(self.card_numbers))]
                else:
                    # 9: 'Straight flush'
                    result_val = [9, max(self.card_numbers),
                                  list(set(self.card_numbers))]
            else:
                # 5: 'Straight'
                result_val = [5, max(self.card_numbers),
                              list(set(self.card_numbers))]
        if result_val[0] < 8:
            res = self.check_n_of_a_kind()
            n = res[0]
            if result_val[0] < n:
                result_val = res
        return result_val

    def check_flush(self):
        """ Check for Flush	5 cards of the same suit """
        return True if len(set(self.card_shapes)) == 1 else False

    def check_straight(self):
        """
        Straight - Sequence of 5 cards in increasing value
        (Ace can precede 2 and follow up King)
        """
        L = self.card_numbers
        if list(range(len(L)+L[0]))[L[0]:] == list(L) or sum(L) == 28:
            return True
        return False

    def check_n_of_a_kind(self):
        """
        Finds if there is a Four/Three/Two of a kind or
        if there is a full house
        """
        count = 1
        L = self.card_numbers
        L1 = list(set(L))
        temp = 0
        temp1 = 0
        temp2 = 0
        if len(L1) < 5:
            for card_value in L1:
                if L.count(card_value) == 4:
                    # Four of a kind so return 8
                    return [8, card_value, L1]
                elif (L.count(card_value) == 2 and count == 3
                      or L.count(card_value) == 3 and count == 2):
                        # its full house so return 7
                    if temp1 != 0:
                        return [7, temp1, [temp1, card_value]]
                    elif temp2 != 0:
                        return [7, card_value, [card_value, temp2]]
                elif L.count(card_value) == 2 and count == 2:
                    # if there are 2 pairs
                    return [3, card_value, L1]
                elif L.count(card_value) > 1:
                    temp = card_value
                    if L.count(card_value) == 3:
                        temp1 = card_value
                    elif L.count(card_value) == 2:
                        temp2 = card_value
                    count = L.count(card_value)
        if count == 3:
            #  Three of a kind so return 4
            return [4, temp, L1]
        elif count == 2:
            # Two cards with the same value
            return [2, temp, L1]
        return [1, max(L1), L1]


# PokerHand("4H 5H 6S 2H 3H").compare_with(PokerHand("KS AS TS QS JS"))
# PokerHand("2H 3H 4H 5H 6H").compare_with(PokerHand("KS AS TS QS JS"))
# PokerHand("2H 3H 4H 5H 6H").compare_with(PokerHand("AS AD AC AH JD"))
# PokerHand("AS AH 2H AD AC").compare_with(PokerHand("JS JD JC JH 3D"))
# PokerHand("2S AH 2H AS AC").compare_with(PokerHand("JS JD JC JH AD"))
# PokerHand("2S AH 2H AS AC").compare_with(PokerHand("2H 3H 5H 6H 7H"))
# PokerHand("AS 3S 4S 8S 2S").compare_with(PokerHand("2H 3H 5H 6H 7H"))
# PokerHand("2H 3H 5H 6H 7H").compare_with(PokerHand("2S 3H 4H 5S 6C"))
# PokerHand("2S 3H 4H 5S 6C").compare_with(PokerHand("3D 4C 5H 6H 2S"))
# Straight wins of three of a kind
# PokerHand("2S 3H 4H 5S 6C").compare_with(PokerHand("AH AC 5H 6H AS"))
# PokerHand("2S 2H 4H 5S 4C").compare_with(PokerHand("AH AC 5H 6H AS"))
# 2 Pair wins of pair
# PokerHand("2S 2H 4H 5S 4C").compare_with(PokerHand("AH AC 5H 6H 7S"))
PokerHand("KH KC 3S 3H 3D").compare_with(PokerHand("2H 2C 3S 3H 3D"))
# PokerHand("2S AH 4H 5S KC").compare_with(PokerHand("AH AC 5H 6H 7S"))
# PokerHand("2S 3H 6H 7S 9C").compare_with(PokerHand("7H 3C TH 6H 9S"))
# PokerHand("4S 5H 6H TS AC").compare_with(PokerHand("3S 5H 6H TS AC"))
# PokerHand("2S AH 4H 5S 6C").compare_with(PokerHand("AD 4C 5H 6H 2C"))
