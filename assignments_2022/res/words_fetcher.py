def fetch_words(min_letters=0, max_letters=20):
    result = []
    file = open("words.txt")
    for word in file.read().split('\n'):
        if min_letters <= len(word) <= max_letters:
            result.append(word)
    return result
