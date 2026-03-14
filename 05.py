# Write a program to do the following functions with a given string
# Display the first largest and second-largest word
# Display the first smallest and second-smallest word
# Display the reverse of sentence
# Convert all words to title case
# Display words starting with the given character
# Exit

def largest(x: str) -> None:
    words: list = x.split()
    word1: str = str(max(words, key=len))
    words.remove(word1)
    word2: str = str(max(words, key=len))

    print(f'Largest word: {word1}, Second largest word: {word2}')
    return

def smallest(x: str) -> None:
    words: list = x.split()
    word1: str = str(min(words, key=len))
    words.remove(word1)
    word2: str = str(min(words, key=len))

    print(f'Smallest word: {word1}, Second smallest word: {word2}')
    return

def reverse_sentence(x: str) -> None:
    print('Sentence in reverse: ')
    print(x[::-1])
    return

def title_case(x: str) -> None:
    words: list = x.split()
    new_str: str = ''

    for i in words:
        new_str += str(i.capitalize()) + ' '

    print(f'Sentence in Title form: {new_str}')
    return

def check_char(x: str) -> None:
    new_str: str = ''
    words: list = x.split()
    letter: str = input("Enter a letter: ")

    if len(letter) > 1:
        print('Please enter only a single letter')
        del letter

    for i in words:
        if i[0] == letter:
            new_str += str(i)
            print(f'Words starting with {letter} are {new_str}')
        else:
            continue

    return

input_string = input('Enter a sentence here: ')

while True:
    x = int(input('''
====================
1. Display the first largest and second-largest word
2. Display the first smallest and second-smallest word
3. Display the reverse of sentence
4. Convert all words to title case
5. Display words starting with the given character
6. Exit
Enter your choice: '''))

    if x == 1:
        largest(input_string)

    elif x == 2:
        smallest(input_string)

    elif x == 3:
        reverse_sentence(input_string)

    elif x == 4:
        title_case(input_string)

    elif x == 5:
        check_char(input_string)

    elif x == 6:
        break

