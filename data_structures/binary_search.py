# returns index in items if search_item is found
def binarySearch(search_item, items):
	left = 0
	right = len(items) - 1

	while left <= right:
		mid = (left + right) // 2

		if items[mid] == search_item:
			return mid

		if items[mid] < search_item:
			left = mid + 1
		else:
			right = mid - 1

	return -1			# search_item not found


numbers = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

while True:
	search_for = int(input('search for number: '))
	if search_for == -1:
		break
	result = binarySearch(search_for, numbers)
	if result != -1:
		print(f'found {search_for} at index {result}')
	else:
		print(f'{search_for} not found')
