ages = {
  'Vasia Pupkin': 19,
  'Marcus Aurelius': 1860,
}
print(ages)

ages['Vasia Pupkin'] = 20;
print(ages)

ages.pop('Vasia Pupkin')
print(ages)

check_if_in_list = lambda a: print(a,":",True) if a in ages else print(a,":",False)
check_if_in_list('Marcus Aurelius')
check_if_in_list('Vasia Pupkin')
