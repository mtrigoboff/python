#!/usr/bin/env python

import os.path, sys

N_BINS = 128

def word_start_end_chars(words, fileNameRoot):
	# collect stats on word start and end chars
	words_with_start_char = [0] * 26
	words_with_end_char =   [0] * 26
	for word in words:
		startIndex = ord(word[0]) - ord('a')
		endIndex = ord(word[len(word) - 1]) - ord('a')
		if startIndex < 0 or startIndex > 25 or endIndex < 0 or endIndex > 25:
			continue
		words_with_start_char[startIndex] += 1
		words_with_end_char[endIndex] += 1
	out_file = open(fileNameRoot + '.wordchars.csv', 'w')
	for i in range(0, 25):
		print(f'{chr(i + ord("a"))},{words_with_start_char[i]},{words_with_end_char[i]}', file=out_file)
	out_file.close()
	
def hash_sum(word):
	hash_code = 0
	for ch in word:
		hash_code += ord(ch)
	return hash_code

def hash_java(word):
	hash_code = 0;
	pow31 = 1;
	for i in range(len(word) - 1, -1, -1):
		hash_code += ord(word[i]) * pow31;
		pow31 *= 31;
	return hash_code & 0xFFFFFFFF		# limit to range of unsigned int

def collect_bins(words, hashFn):
	bins = [0] * N_BINS
	for word in words:
		bins[hashFn(word) >> 25] += 1
	return bins

def main(fileName):
	fileNameRoot = os.path.splitext(fileName)[0]

	# collect words in set
	words = set()
	in_file = open(fileName, 'r')
	lines = in_file.readlines()
	for line in lines:
		for word in line.split():
			words.add(word)
	in_file.close()

	# hash words into .csv file
	out_file = open(fileNameRoot + '.hash.csv', 'w')
	for word in words:
		print(f'{word},{hash_sum(word)},{hash_java(word)}', file=out_file)
	out_file.close()
	
	# collect generated hash codes into bins
	hash1Bins = collect_bins(words, hash_sum)
	hash2Bins = collect_bins(words, hash_java)
	out_file = open(fileNameRoot + '.bins.csv', 'w')
	for i in range(N_BINS):
		print(f'{hash1Bins[i]}, {hash2Bins[i]}', file=out_file, sep='')
	out_file.close()

#def test(arg):
#	for word in ("limited", "optimism", "listening", "founder"):
#		print '%s,%X' % (word, hash2(word))

# when invoked from the command line
if __name__ == '__main__':
	main(sys.argv[1])
#	test(sys.argv[1])
