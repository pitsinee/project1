def sum(int) :
    x = 0
    for i in range(1, int+1) :
       x += i
    return(x) 

#sum(10)

def test1(int) :
    x = ''
    for i in range(1, int+1) :
        if i == 10 :
            y = str(i)
            x += y
        else :
            y = str(i) + '+'
            x += y
    print(x, '=', sum(int))

test1(10)