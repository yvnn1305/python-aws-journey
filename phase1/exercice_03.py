def word_file(filename):
    with open(filename, 'r') as f:
        content = f.read()
        word_list = content.split()
        result = {}
        for mot in word_list:
            if mot in result:
                result[mot] += 1
            else:
                result[mot] = 1
        return result
    
print(word_file("mots.txt"))