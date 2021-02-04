import random
'''
    5001 - HW 9
    Xiamiao Lin
    Nov 24, 2020
'''


class Card():
    '''Store card's value and face'''
    def __init__(self, value=0):
        self.value = value
        self.face = False

    def revealface(self):
        self.face = True

    def setface(self):
        self.face = False

    def __str__(self):
        if self.face is True:
            show = str(self.value)
        else:
            show = "*"
        return show


def shuffle(card):
    for i in range(4):
        for j in range(4):
            row = random.randint(0, 3)
            col = random.randint(0, 3)
            card[row][col], card[i][j] = card[i][j], card[row][col]


def display(card):
    for i in range(4):
        for j in range(4):
            print(card[i][j], end="")
        print("")
    print('========================')


def main():
    # initialize card
    card = [[Card(1), Card(2), Card(3), Card(4)],
            [Card(1), Card(2), Card(3), Card(4)],
            [Card(5), Card(6), Card(7), Card(8)],
            [Card(5), Card(6), Card(7), Card(8)]]

    shuffle(card)
    # to record if card is already facing up
    already_up_one = False
    already_up_two = False

    pair = 0
    while pair != 8:
        x1 = int(input("Enter x-coordinate of first card: "))
        y1 = int(input("Enter y-coordinate of first card: "))
        x2 = int(input("Enter x-coordinate of second card: "))
        y2 = int(input("Enter x-coordinate of second card: "))

        # if the card is already up, set already_up to true
        if (card[x1][y1].face is True):
            already_up_one = True
        else:
            card[x1][y1].revealface()

        if (card[x2][y2].face is True):
            already_up_two = True
        else:
            card[x2][y2].revealface()

        if card[x1][y1].value == card[x2][y2].value:
            pair += 1
        else:
            display(card)
            print("\n" * 30)
            # if card is already up, we won't setface to False
            if (already_up_one is False):
                card[x1][y1].setface()
            if (already_up_two is False):
                card[x2][y2].setface()
            already_up_one = False
            already_up_two = False
            print("Not match, please choose again")
        display(card)

    # if all cards are facing up, game is over
    print("Congrats! You win the game!")


main()
