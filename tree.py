import turtle
from functools import reduce

t = turtle.Pen()
t2 = turtle.Pen()

GREEN = "#00ff00"
RED = "#ff0000"
BLACK = "#000000"

# ------------------------------------------------

# 나뭇잎 그리기 함수
def draw_leaf(mode, t):
    def draw(acc, cur):
        d = 0
        a = 180
        부호 = 0
        
        if cur % 2 == 0:
            d = 50
            a -= mode*45
            부호 = 1
        else:
            d = 15
            a += mode*45
            부호 = -1
                
        t.forward(d)
        t.left(a)

        return acc+부호*(((d**2)/2)**(1/2))
    
    return draw

# 나무 그리기 함수
def draw_tree(mode, t):
    def draw(acc, cur):
        t.forward(25)
        t.right(mode*90)

        return 0
    
    return draw

# ------------------------------------------------

# 나뭇잎 색 지정
t.color(BLACK, GREEN)
t2.color(BLACK, GREEN)

# 왼쪽 나뭇잎
t.begin_fill()
t.right(180-45)
t.forward(reduce(draw_leaf(1, t), range(5), 0)-9)
t.end_fill()
# 오른쪽 나뭇잎
t2.begin_fill()
t2.right(45)
t2.forward(reduce(draw_leaf(-1, t2), range(5), 0)-9)
t2.end_fill()

# ------------------------------------------------

# 나무 색 지정
t.color(BLACK, RED)
t2.color(BLACK, RED)

# 왼쪽 나무
t2.begin_fill()
reduce(draw_tree(-1, t2), range(3), 0)
t2.end_fill()
# 오른쪽 나무
t.begin_fill()
reduce(draw_tree(1, t), range(3), 0)
t.end_fill()
