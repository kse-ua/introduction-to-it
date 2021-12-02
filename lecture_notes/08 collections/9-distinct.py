def distinct(dataset: list):
    filtered = dict()

    # FOR FANCY ONES
    # if you were wondering how to apply lambda
    # HERE YOU GO!
    # dataset.sort(key=lambda direction: direction["from"])

    for record in dataset:
        departure, arrival = record["from"], record["to"]
        empty = filtered.setdefault(departure, True)

        if empty == True:
            filtered[departure] = set()

        # We always add, because values of dict filtered
        # are sets :)
        filtered[departure].add(arrival)

    result = list()
    for departure, arrivals in filtered.items():

        for arrival in arrivals:
            result.append(
                {"from": departure, "to": arrival}
            )

    return result


# // Usage
flights = [
    {"from": 'Kiev', "to": 'Rome'},
    {"from": 'Kiev', "to": 'Warsaw'},
    {"from": 'Dublin', "to": 'Riga'},
    {"from": 'Riga', "to": 'Dublin'},
    {"from": 'Kiev', "to": 'Rome'},
    {"from": 'Cairo', "to": 'Paris'},
]

directions = distinct(flights)

for direction in directions:
    print(direction)
