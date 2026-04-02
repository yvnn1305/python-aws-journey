import csv
import sys

def word_file(filename):
        if len(sys.argv[1]) < 1:
            print("Usage : python exercice_05.py <fichier.txt>. Retry please")
        try:
            with open(filename, 'r') as f:
                content = f.read()
        except FileNotFoundError:
            print("Error : The file doesn't exist")
            sys.exit()
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

if len(sys.argv) != 2:
    print("Usage : python exercice_05.py <fichier.txt>. Retry please")
else:
    write_csv(sys.argv[1])