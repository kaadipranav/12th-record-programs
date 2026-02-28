x = input('Enter integers separated by spaces: ')
l = list(map(int, x.split()))
l.sort()
print(l)
list1 = list()

while True:
    y = int(input('''
    =================================================
    Select and option from the following:
    1. Add element
    2. Delete element
    3. Arrange in ascending order
    4. Arrange in descending order
    5. Display reverse of elements
    6. Display list
    7. exit
    Enter your choice (1/2/3/4/5/6/7): '''))

    if y == 1:
        add1 = int(input("Enter the element to add: "))
        l.append(add1)
        print("Element added")

    elif y == 2:
        del1 = int(input("Enter the element to delete: "))
        if del1 in l:
            l.remove(del1)
            print("Element deleted")
        else:
            print("Element not found in the list")

    elif y == 3:
        print("List sorted in ascending order:")
        print(sorted(l))

    elif y == 4:
        print("List sorted in descending order:")
        print(sorted(l, reverse=True))

    elif y == 5:
        list1 = [i[::-1] for i in l]
        print(f"Reverse of all elements: {list1}")

    elif y == 6:

        print(l)
    elif y == 7:
        break

    else:
        print("Invalid choice. Please select a valid option.")

