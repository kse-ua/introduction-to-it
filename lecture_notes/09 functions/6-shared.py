def cached_add(a, b, cache):  # sorry, i hate globals :)
    key = f'{a}+{b}'
    cached_result = cache.get(key)
    if cached_result is None:
        result = a + b
        cache[key] = result
    else:
        result = cached_result

    return result


def cached_sub(a, b, cache):
    key = f'{a}-{b}'
    cached_result = cache.get(key)
    if cached_result is None:
        result = a - b
        cache[key] = result
    else:
        result = cached_result

    return result


if __name__ == '__main__':
    def main():
        cache = {}

        print(f'sub: {cached_sub(5, 2, cache)}')
        print(f'add: {cached_add(5, 2, cache)}')


    main()
