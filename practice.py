# import sys
#
#
# def division():
#     a = int(input("Set the first number: "))
#     b = int(input("Set the second number: "))
#     if b != 0:
#         print(a / b)
#     else:
#         # The string below will look like an error message.
#         print("The second number cannot be a zero!", file=sys.stderr)
#
#
# division()

my_file = open('file1.txt', 'a')
# print('This string will be in the file...', file=my_file)
print('This string will be in the file...'
      'Manita Tejas'
      'ManiTeja', file=my_file, flush=True)
# my_file.close()
