# Python version
ages = {}

ages["Vasia Pupkin"] = 19
ages['Marcus Aurelius'] = 1860
print(f"ages: {ages}")

ages["Vasia Pupkin"] = 20
print(f"ages: {ages}")

print("Vasia Pupkin:", "Vasia Pupkin" in ages)
print('Marcus Aurelius:', "Marcus Aurelius" in ages)

ages.clear()
print(f"ages: {ages}")
