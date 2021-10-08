from pathlib import Path


def validate_name(name):
    return name[0].isupper()


def read_names(path):
    return Path(path).read_text().split(" ")


def validate_names():
    values = read_names("data.txt")
    for name in values:
        if not validate_name(name):
            return False
    return True

