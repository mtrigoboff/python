words = {}

text_file = open('basics/constitution.txt', 'r')
lines = text_file.readlines()
text_file.close()

for line in lines:
    for word in line.split():
        try:
            words[word] += 1
        except KeyError:
            words[word] = 1

for key, value in sorted(words.items()):
    print(f'{key}: {value}')
