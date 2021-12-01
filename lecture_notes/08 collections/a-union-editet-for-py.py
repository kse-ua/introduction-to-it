def union(s1, s2):
    print(s1)
    print(s2)
    union = []
    for country in s1:
        if country not in union:
            union.append(country)
    for country in s2:
        if country not in union:
            union.append(country)
    return(union)


cities1 = ['Beijing', 'Kiev']
cities2 = ['Kiev', 'London', 'Baghdad']
print(union(cities1,cities2))
