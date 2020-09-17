squad_713_file = open('general_assembly.txt', 'w')

squad_713 = [
    'Alice',
    'Alpha',
    'Anthony',
    'Barent',
    'Branden',
    'Channee',
    'Cristina',
    'Cabassa',
    'Elaine',
    'Han',
    'Irene',
    'Joshua',
    'Levin',
    'Lizz',
    'Margaret',
    'Nicholas',
    'Philip',
    'Rohun',
    'Sameh',
    'Shane',
    'Steven',
    'Subrata',
    'Tanner',
    'Yoel',
    'Adam',
    'Pete',
    'Rome',
    'Taylor'
]

for i in range(len(squad_713)):
    folk = squad_713[i]
    squad_713_file.write('{}\n'.format(folk))

squad_713_file.close()

read_squad_713_file = open('general_assembly.txt')
list_of_people = read_squad_713_file.readlines()
print(list_of_people)
#list_of_people = read_ga_file.readlines()
#print(list_of_people)
#print(squad_713_file.read())

#squad_713_file.close()
