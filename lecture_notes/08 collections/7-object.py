class Object:
    pass


ages = Object()

setattr(ages, 'Vasia Pupkin', 19)
setattr(ages, 'Marcus Aurelius', 1860)
print(f'ages: {ages.__dict__}')

setattr(ages, 'Vasia Pupkin', 20)
print(f'ages: {ages.__dict__}')

delattr(ages, 'Vasia Pupkin')

print({
    'Vasia Pupkin': hasattr(ages, 'Vasia Pupkin'),
    'Marcus Aurelius': hasattr(ages, 'Marcus Aurelius'),
})
