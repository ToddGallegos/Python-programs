weight = int(input('What is your weight? '))

unit = input('Convert to (K)g or (L)b? ')


if unit.lower() == 'k':
    weight = int(weight / 2.2)
    print('Your weight is ' + str(weight) + ' kilograms.')
elif unit.lower() == 'l':
    weight = int(weight * 2.2)
    print('Your weight is ' + str(weight) + ' pounds.')

