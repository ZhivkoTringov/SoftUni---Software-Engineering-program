cards = input().split(' ')
count_shuffles = int(input())
for shuffle in range(count_shuffles):
    final_deck = []
    lef_side = cards[:len(cards)//2:]
    right_side = cards[len(cards)//2::]
    for index in range(len(lef_side)):
        final_deck.append(lef_side[index])
        final_deck.append(right_side[index])
    cards = final_deck
print(cards)