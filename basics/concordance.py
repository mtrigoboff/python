words = {}

text_file = open('basics\\constitution.txt', 'r')
lines = text_file.readlines()
text_file.close()

for line in lines:
    for word in line.split():
        if word in words:
            words[word] += 1
        else:
            words[word] = 1

for key, value in sorted(words.items()):
    print(f'{key}: {value}')
