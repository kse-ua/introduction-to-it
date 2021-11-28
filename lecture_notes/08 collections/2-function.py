# Implementation

def get_first_and_last(array):
    first = ages[0]
    last = ages[-1]
    return first, last


# Usage

ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]
first, last = get_first_and_last(ages)
print({'first': first, 'last': last})

# The two functions are pretty much the same except that return types are not equivalent: a tuple in the python version
# and an object in the js one. And, also, python allows negative indexing which is prohibited in js that is why
# ages[-1] is used instead of ages[len(ages) - 1]. Generally, in python for any sequence S, we can write S[-n]
# where 0 <= n < len(S) <=> S[len(S) - n].
