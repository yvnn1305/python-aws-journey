import csv

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

def write_csv(filename):
    tab = []
    data = word_file(filename)
    for mot in data:
        tab.append({'mot': mot, 'occurences': data[mot]})
    tab.sort(key=lambda x: x['occurences'], reverse=True)
    print(tab)

    with open('fichier_python.csv', 'w', newline='') as csvfile:
        fieldnames = ['mot', 'occurences']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(tab)
        
write_csv("mots.txt")