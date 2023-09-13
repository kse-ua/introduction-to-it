def binary_search(cards, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        guess = cards[mid]
        if guess == x:
            return mid
        elif guess > x:
            return binary_search(cards, low, mid - 1, x)
        else:
            return binary_search(cards, mid + 1, high, x)
    else:
        return None


cards = [1, 2, 3, 4, 5]
print(binary_search(cards, 0, len(cards) - 1, 5))