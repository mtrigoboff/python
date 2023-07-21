f = open('miscellaneous/csv_file/test_file.csv', 'r')
lines = f.readlines()

labels = True
data = []
for line in lines:
    # print(line.strip())
    items = line.strip().split(',')
    if not labels:
    	for i in range(len(items)):
            items[i] = int(items[i])		# convert strings to ints
    data.append(items)
    labels = False

for d in data:
    print(d)

f.close()