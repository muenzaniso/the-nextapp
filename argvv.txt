# first import built-in sys module.
import sys
# get command line argument length.
argv_len = len(sys.argv)
print('there are ' + str(argv_len) + ' arguments.')
# loop in all arguments.
for i in range(argv_len):
  tmp_argv = sys.argv[i]
  # print out argument index and value.
  print(str(i))
  print(tmp_argv)
  print('argv ' + str(i) + ' = ' + tmp_argv)