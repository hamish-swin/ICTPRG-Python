userIn = input('Please submit input below: \n')

arr = userIn.split()
print('User submitted', len(arr), 'word/s')
print('First Word =', arr[0])
print('Third Word =', arr[2])

del arr[0]
del arr[len(arr) - 1]

print('Every word except the first and last word:', arr)