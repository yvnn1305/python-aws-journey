def reverse_dict(text):
    inverse = {valeur: cle for cle, valeur in text.items()}
    return inverse

original = {"a": 1, "b": 2, "c": 3}

print(reverse_dict(original))