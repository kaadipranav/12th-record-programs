def is_word_chain(word1):
    words = word1.split()
    if len(words) < 2:
        return False

    for i in range(len(words) - 1):
        if words[i][-1] != words[i + 1][0]:
            return False
    return True

print(is_word_chain("abc cde efg gha"))
print(is_word_chain("abc cde efg gha hib"))

