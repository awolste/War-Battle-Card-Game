# Python program to shuffle a deck of card

# importing modules
import itertools, random

# make a deck of cards
deck = list(itertools.product(range(1,14),['Spades','Hearts','Diamonds','Clubs']))

# shuffle the cards
random.shuffle(deck)
multipleWarList = []
inWar = False
p1 = []
p2 = []
for i in range(len(deck)):
    if i%2 == 0:
        p1.append((deck[i][0], deck[i][1]))
    else:
        p2.append((deck[i][0], deck[i][1]))

while len(p1) != 0 and len(p2) != 0:
    if p1[0][0] > p2[0][0]:
        print("P1 puts ", p1[0][0], " over ", p2[0][0])
        p1.append(p2.pop(0))
        p1.append(p1.pop(0))
    elif p2[0][0] > p1[0][0]:
        print("P2 puts ", p2[0][0], " over ", p1[0][0])
        p2.append(p1.pop(0))
        p2.append(p2.pop(0))
    else:
        inWar = True
        while inWar:
            # figure out multiple wars in a row
            # account for when dont have enough cards for war
            print("War for ", p1[0][0], " VS ", p2[0][0])
            if len(p1) < 5:
                if p1[len(p1) - 1][0] > p2[4][0]:
                    print("P1 won with a ", p1[len(p1) - 1][0], " over ", p2[4][0])
                    p1.append(p2.pop(0))
                    p1.append(p2.pop(0))
                    p1.append(p2.pop(0))
                    p1.append(p2.pop(0))
                    p1.append(p2.pop(0))
                    random.shuffle(p1)
                    inWar = False
                elif p1[len(p1) - 1][0] < p2[4][0]:
                    print("P2 won with a ", p2[4][0], " over ", p1[len(p1) - 1][0])
                    print("Game Over. Player 2 wins")
                    exit()

            elif len(p2) < 5:
                if p2[len(p2) - 1][0] > p1[4][0]:
                    print("P2 won with a ", p2[len(p2) - 1][0], " over ", p1[4][0])
                    p2.append(p1.pop(0))
                    p2.append(p1.pop(0))
                    p2.append(p1.pop(0))
                    p2.append(p1.pop(0))
                    p2.append(p1.pop(0))
                    random.shuffle(p2)
                    inWar = False
                elif p2[len(p2) - 1][0] < p1[4][0]:
                    print("P1 won with a ", p1[4][0], " over ", p2[len(p2) - 1][0])
                    print("Game Over. Player 1 wins")
                    exit()
            else:
                if p1[4][0] > p2[4][0]:
                    print("P1 won with a ", p1[4][0], " over ", p2[4][0])
                    p1.append(p2.pop(0))
                    p1.append(p1.pop(0))
                    p1.append(p2.pop(0))
                    p1.append(p1.pop(0))
                    p1.append(p2.pop(0))
                    p1.append(p1.pop(0))
                    p1.append(p2.pop(0))
                    p1.append(p1.pop(0))
                    p1.append(p2.pop(0))
                    p1.append(p1.pop(0))
                    while(len(multipleWarList) > 0):
                        p1.append(multipleWarList.pop(0))
                    multipleWarList = []
                    inWar = False
                elif p2[4][0] > p1[4][0]:
                    print("P2 won with a ", p2[4][0], " over ", p1[4][0])
                    p2.append(p1.pop(0))
                    p2.append(p2.pop(0))
                    p2.append(p1.pop(0))
                    p2.append(p2.pop(0))
                    p2.append(p1.pop(0))
                    p2.append(p2.pop(0))
                    p2.append(p1.pop(0))
                    p2.append(p2.pop(0))
                    p2.append(p1.pop(0))
                    p2.append(p2.pop(0))
                    while(len(multipleWarList) > 0):
                        p2.append(multipleWarList.pop(0))
                    multipleWarList = []
                    inWar = False
                else:
                    print("War Again!")
                    multipleWarList.append(p1.pop(0))
                    multipleWarList.append(p2.pop(0))
                    multipleWarList.append(p1.pop(0))
                    multipleWarList.append(p2.pop(0))
                    multipleWarList.append(p1.pop(0))
                    multipleWarList.append(p2.pop(0))
                    multipleWarList.append(p1.pop(0))
                    multipleWarList.append(p2.pop(0))
                    multipleWarList.append(p1.pop(0))
                    multipleWarList.append(p2.pop(0))



if len(p1)  ==0:
    print("Game Over. Player 2 wins")
else:
    print("Game Over. Player 1 wins")
