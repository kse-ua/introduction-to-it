ages = [10, 12, 15, 15, 17, 18, 18, 19, 20]

print({'ages': ages})

ages.extend([24, 27, 30])

print({'extended ages': ages})

slice_of_ages = ages[1:8]

print({'slice_of_ages': slice_of_ages})

ages.reverse()

print({'reversed ages': ages})
