from random import *

shapes = [
    {
        'text': 'blue',
        'color': '#3F51B5',
        'rect': [20, 60, 100, 100]
    },
    {
        'text': 'red',
        'color': '#C62828',
        'rect': [140, 60, 100, 100]
    },
    {
        'text': 'yellow',
        'color': '#FFD600',
        'rect': [20, 180, 100, 100]
    },
    {
        'text': 'green',
        'color': '#4CAF50',
        'rect': [140, 180, 100, 100]
    }
]

def get_shapes():
    return shapes

def generate_quiz():
    text = choice(['RED','BLUE','YELLOW','GREEN'])
    color = choice(['#C62828','#3F51B5','#FFD600','#4CAF50'])
    quiz_type = choice([0,1])
    return [
                text,
                color,
                quiz_type
                # randint(0, 1) # 0 : meaning, 1: color
            ]

def mouse_press(x, y, text, color, quiz_type):
    if 20 <= x <= 120 and 60 <= y <= 160:
        if quiz_type == 0:
            if text == 'BLUE':
                return True
            else:
                return False
        elif quiz_type == 1:
            if color == '#3F51B5':
                return True
            else:
                return False
    if 140 <= x <= 240 and 60 <= y <= 160:
        if quiz_type == 0:
            if text == 'RED':
                return True
            else:
                return False
        elif quiz_type == 1:
            if color == '#C62828':
                return True
            else:
                return False
    if 20 <= x <= 120 and 180 <= y <= 280:
        if quiz_type == 0:
            if text == 'YELLOW':
                return True
            else:
                return False
        elif quiz_type == 1:
            if color == '#FFD600':
                return True
            else:
                return False
    if 140 <= x <= 240 and 180 <= y <= 280:
        if quiz_type == 0:
            if text == 'GREEN':
                return True
            else:
                return False
        elif quiz_type == 1:
            if color == '#4CAF50':
                return True
            else:
                return False
