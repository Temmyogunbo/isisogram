def isisogram(word):
    if word == " ":
        return (word, False)
    if type(word) != str:
        raise TypeError("Argument should be a string")
    words = list(word.lower())
    letters = ['a', 'b', 'c','d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for character in range(len(words)):
        if words[character] in letters:
            if words.count(words[character]) > 1:
                return (word, False)
                break
        else:
            raise TypeError("Argument should contain only alphabet")
    return (word, True)
