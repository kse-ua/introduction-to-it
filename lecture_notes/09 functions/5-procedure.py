def add(a, b):
    return a + b


def cached_add(a, b, cache):  # sorry, i hate globals :)
    key = f'{a},{b}'
    cached_result = cache.get(key)
    if cached_result is None:
        result = a + b
        cache[key] = result
    else:
        result = cached_result

    return result


if __name__ == '__main__':
    def main():
        cache = {}

        print([add(10, 20), add(1, 2), add(100, 20), add(100, 200)])
        print([
            cached_add(10, 20, cache),
            cached_add(1, 2, cache),
            cached_add(100, 20, cache),
            cached_add(100, 200, cache)
        ])


    main()
