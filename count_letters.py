def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter]+=1
    return result
new_string = str(input("Enter a string:\n"))
print(count_letters(new_string))