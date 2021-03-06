import re


print(re.search('^(?:A\.|\(a\))', '(b)'))

if re.search('^(?:A\.|\(a\))', 'A.'):
    print("yessssssssss")
else:
    print('Nooooooooooo')


