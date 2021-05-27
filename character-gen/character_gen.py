def generate():
    import random
    import json

    class Character:
        def __init__(self, age, homeCountry, ethnicity, gender, firstName, lastName):
            self.age = age
            self.homeCountry = homeCountry
            self.ethnicity = ethnicity
            self.gender = gender
            self.firstName = firstName
            self.lastName = lastName
    
    def randomJson(array, file):
        j = json.loads(open(file).read())
        i = random.randint(0, len(j[array])-1)
        return j[array][i]

    def random_line(file):
        lines = open(file).read().splitlines()
        line = random.choice(lines)
        return line

    c1 = Character(
        random.randint(14,93),
        random_line('info/countries.txt'),
        random_line('info/ethnicities.txt'),
        random_line('info/genders.txt'),
        "",
        ""
    )

    c1.__init__(
        c1.age,
        c1.homeCountry,
        c1.ethnicity,
        c1.gender,
        randomJson(c1.gender, 'info/fNames.json'),
        random_line('info/lNames.txt')
    )

    return(c1)
    