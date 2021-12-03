def diference(s1, s2):
    print(s1)
    print(s2)
    diference = []
    for country in s1:
        if country not in s2:
            diference.append(country)
    return(diference)
def compliment(s1,s2):
    return diference(s2,s1)

cities1 = ['Beijing', 'Kiev']
cities2 = ['Kiev', 'London', 'Baghdad']
print(compliment(cities1,cities2))
