 
start=1
end=5
step=1
for i in range (start, end+1, step):
    print(' '*(end-i)  + '*'*(i*2-1))
 
start=4
end=1
step=-1
for i in range (start, end-1, step):
    print(' '*(start - i + 1) + '*'*(i*2-1))