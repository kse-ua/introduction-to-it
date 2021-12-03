def diference(s1, s2):
    print(s1)
    print(s2)
    diference = []
    for country in s1:
        if country not in s2:
            diference.append(country)
    return(diference)


cities1 = ['Beijing', 'Kiev']
cities2 = ['Kiev', 'London', 'Baghdad']
print(diference(cities1,cities2))
