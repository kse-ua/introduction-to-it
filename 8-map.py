ages = {}

ages["Vasia Pupkin"] = 19
ages["Marcus Aurelius"] = 1860

print(ages)

ages["Vasia Pupkin"] = 20

print(ages)

ages.pop("Vasia Pupkin")

print(ages)

print(f"Vasia Pupkin: {'Vasia Pupkin' in ages},\nMarcus Aurelius: {'Marcus Aurelius' in ages}")

ages.clear()

print(ages)
