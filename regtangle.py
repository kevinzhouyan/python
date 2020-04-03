def draw_rectangle(width, height):
    step=1
    print('-' * width)
    for i in range(1, height-2, step):
        print('|' + ' '*(width-2) + '|')
    print('-' * width)

draw_rectangle(4, 5)