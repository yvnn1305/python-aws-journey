string = "Je m'appelle Yann et Yann"

def word_count(text):
    word_list = text.split()
    result = {}
    for mot in word_list:
        if mot in result:
            result[mot] += 1
        else:
            result[mot] = 1
    return result

print(word_count(string))
