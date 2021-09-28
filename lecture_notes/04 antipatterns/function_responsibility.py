from pathlib import Path


def process():
    values = Path('data.txt').read_text().split(" ")
    for name in values:
        if not name[0].isupper():
            return False
    return True

