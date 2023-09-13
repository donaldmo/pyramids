"""
The end parameter in the print function is used to add any string. At the end of the output of the print statement in python.

By default, the print function ends with a newline.

Passing the whitespace to the end parameter (end='') indicates that the end character has to be identified by whitespace and not a newline.
"""

#For example:
print('Donald ', end='')

print('is awesome')

'''

'''

rows = 5

i = 0
i = 1

print('*', end='')
i=2
print('')

print('*', end='')
print('*', end='')
i = 3

print('')

print('*', end='')
print('*', end='')
print('*', end='')
i = 4

print('')

print('*', end='')
print('*', end='')
print('*', end='')
print('*', end='')
i = 5

print('')

print('*', end='')
print('*', end='')
print('*', end='')
print('*', end='')
print('*', end='')

print('')

'''
#outer loop
for i in range (0, rows + 1):

    for j in range(0, i):
        print(i, end='')
        
    print('')
'''