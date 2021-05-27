import character_gen

character = character_gen.generate()

print('age = %i' % (character.age))
print('home country = %s' % (character.homeCountry))
print('ethnicity = %s' % (character.ethnicity))
print('gender = %s' % (character.gender))
print('name = %s %s' % (character.firstName, character.lastName))
