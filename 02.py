x = input('Enter names: ')
y = input('Enter age: ')
d = dict()

x1 = list(map(str, x.split()))
y1 = list(map(int, y.split()))

for i in range(len(x1)):
    d[x1[i]] = y1[i]

while True:
    y = int(input('''
    1. Add an element to the dictionary
    2. Search element from the dictionary
    3. Edit element from the dictionary
    4. Delete an element from the dictionary
    5. Display average age from the dictionary
    6. Exit
    Select your choice: '''))

    if y == 1:
        inp1 = input('Enter name: ')
        inp2 = int(input('Enter age: '))
        d[inp1] = inp2
        print(f'Element {inp1} added to the dictionary')

    elif y == 2:
        inp1 = input('Enter name to search: ')
        if inp1 in d:
            print(f'Element {inp1} found with age {d[inp1]}')
        else:
            print(f'Element {inp1} not found')

    elif y == 3:
        inp1 = input('Enter name to edit: ')
        inp2 = int(input('Enter new age: '))
        if inp1 in d:
            d[inp1] = inp2
            print(f'Element {inp1} edited to age {inp2}')

    elif y == 4:
        inp1 = input('Enter name to delete: ')
        if inp1 in d:
            del d[inp1]
            print(f'Element {inp1} deleted from the dictionary')
        else:
            print(f'Element {inp1} not found')

    elif y == 5:
        print(f'Average age is {sum(d.values())/len(d)}')

    elif y == 6:
        break

    else:
        print('Invalid choice')



