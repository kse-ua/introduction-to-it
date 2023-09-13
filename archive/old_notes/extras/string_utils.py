def capitalize(row: str):
    if row[0].isupper():
        return row
    return row[0].upper() + row[1 : ]


if __name__ == '__main__':
    print(capitalize("hello"))
    print(capitalize("Hi"))