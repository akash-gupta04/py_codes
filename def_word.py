def show_letters(word):
    for letter in show_letters([word]):
        return letter, print(end = "")

show_letters("Hello")
# Should print one line per letter