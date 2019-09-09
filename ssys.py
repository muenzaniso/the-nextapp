import sys

sys.stderr.write('This is stderr text\n')
sys.stderr.flush()
sys.stdout.write('This is stdout text\n')

print(sys.argv)
print(sys.argv[0])

if len(sys.argv) > 1:
    print(float(sys.argv[1]) +5)
