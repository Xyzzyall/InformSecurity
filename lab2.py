import Cifer

evgeniy = Cifer.DHActor('Evgeniy Onegin', 150, 228)
tatyana = Cifer.DHActor('Tatyana Larina', 147, 190)

print(evgeniy)
print(tatyana)
print()

evgeniy, tatyana = evgeniy & tatyana

print(evgeniy)
print(tatyana)
