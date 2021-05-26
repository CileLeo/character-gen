import random

class Character:
    def __init__(self, age, homeCountry, ethnicity, firstName, lastName):
        self.age = age
        self.homeCountry = homeCountry
        self.ethnicity = ethnicity
        self.firstName = firstName
        self.lastName = lastName

def random_line(file):
    lines = open(file).read().splitlines()
    line = random.choice(lines)
    return line

c1 = Character(
    random.randint(14,93),
    random_line('info/countries.txt'),
    random_line('info/ethnicities.txt'),
    random_line('info/fNames.txt'),
    random_line('info/lNames.txt')
)

print('age = %i' % (c1.age))
print('home country = %s' % (c1.homeCountry))
print('ethnicity = %s' % (c1.ethnicity))
print('name = %s %s' % (c1.firstName, c1.lastName))