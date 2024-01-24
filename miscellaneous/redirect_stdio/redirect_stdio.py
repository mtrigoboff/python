import os.path, sys

print('redirect stdio')
print(sys.argv[1], sys.argv[2], sys.argv[3])
sys.stdin = open(os.path.join(sys.argv[1], sys.argv[2]), 'r')
sys.stdout = open(os.path.join(sys.argv[1], sys.argv[3]), 'w')
line1 = input()
print(line1)
sys.stdin.close()
sys.stdout.close()