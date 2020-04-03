 
def draw_diamond(size):
    start=1
    end=size
    step=1
    for i in range (start, end+1, step):
        print(' '*(end-i)  + '*'*(i*2-1))
 
    start=size -1
    end=1
    step=-1
    for i in range (start, end-1, step):
        print(' '*(start - i + 1) + '*'*(i*2-1))

draw_diamond(5)
