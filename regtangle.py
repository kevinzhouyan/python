width=50
height=6
step=1
print('-' * width)
for i in range(1, height-2, step):
    print('|' + ' '*(width-2) + '|')
print('-' * width)