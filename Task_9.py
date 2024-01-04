# Не разобралась с этой задачей до конца, если честно. Посмотрела решение в chatGPT.
# Почему нужно использовать "raise Stop Iteration" - иначе получается бесконечный цикл +
# даже сейчас при запуске падают ошибки.

class CardDeck:
    def __init__(self):
        self.length = 52
        self.suits = ['clubs', 'diamonds', 'hearts', 'spades']
        self.ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A']
        self.current_index = 0
    def __next__(self):
        if self.current_index < self.length:
            suit_index = self.current_index // len(self.ranks)
            rank_index = self.current_index % len(self.ranks)
            current_card = f"{self.suits[suit_index]} {self.ranks[rank_index]}"
            self.current_index += 1
            return current_card
        else:
            raise StopIteration

    def __iter__(self):
        return self

deck = CardDeck()
while True:
    print(next(deck))