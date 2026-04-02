def count_letter(text):
    result = {}
    for lettre in text:
        if lettre in result:
            result[lettre] += 1
        else:
            result[lettre] = 1
    return result

string = "yann"
print(count_letter(string))