'''
Created on Apr 7, 2024

@author: twendt
'''
def pp(t):
    path = [(0,90), (150,90), (150,510), (270,510), (270,150), (450,150), (450,390), (600,390)]
    x = 0
    y = 0
    
    current_node = 0
    dist_travelled = 0
    this_point = path[current_node]
    next_point = path[current_node + 1]
    next_dist = max(abs(next_point[0] - this_point[0]), abs(next_point[1] - this_point[1]))
    while current_node < len(path) - 1 and t > next_dist:
        current_node += 1
        dist_travelled += next_dist
        t -= next_dist
        this_point = path[current_node]
        next_point = path[current_node + 1]
        next_dist = max(abs(next_point[0] - this_point[0]), abs(next_point[1] - this_point[1]))
    
    
    
    if current_node < len(path) - 1:
        if next_point[0] == this_point[0]:
            x = this_point[0]
        else:
            direction = (next_point[0] - this_point[0]) / abs((next_point[0] - this_point[0]))
            x = path[current_node][0] + direction * t
        if next_point[1] == this_point[1]:
            y = this_point[1]
        else:
            direction = (next_point[1] - this_point[1]) / abs((next_point[1] - this_point[1]))
            y = path[current_node][1] + direction * t

    else:
        x = 0
        y = 90 
    
    return (x,y)
        


def parameterized_path(t):
    '''
    Function used to force enemies to follow the road.
    '''
    # Follow the center of the parameterized path.
    # (  0,  90) -> (150,  90)     150 units
    # (150,  90) -> (150, 510)     420 units
    # (150, 510) -> (270, 510)     120 units
    # (270, 510) -> (270, 150)     360 units
    # (270, 150) -> (450, 150)     180 units
    # (450, 150) -> (450, 390)     240 units
    # (450, 390) -> (600, 390)     150 units
    x = 0
    y = 0
    if t < 150:
        # Move right, but stay at y = 90
        x = t
        y = 90
    elif t < 150 + 420:
        # Move down (i.e. increasing y) but stay at x = 150
        x = 150
        y = 90 + (t - 150)
    elif t < 150 + 420 + 120:
        # Move right, but stay at y = 510
        x = 150 + (t - 150 - 420)
        y = 510
    elif t < 150 + 420 + 120 + 360:
        # Move up, but stay at x = 270
        x = 270
        y = 510 - (t - 150 - 420 - 120)
    elif t < 150 + 420 + 120 + 360 + 180:
        # Move right, but stay at y = 150
        x = 270 + (t - 150 - 420 - 120 - 360)
        y = 150
    elif t < 150 + 420 + 120 + 360 + 180 + 240:
        # Move down, but stay at x = 450
        x = 450
        y = 150 + (t - 150 - 420 - 120 - 360 - 180)
    elif t < 150 + 420 + 120 + 360 + 180 + 240 + 150:
        # Move right, but stay at y = 390
        x = 450 + (t - 150 - 420 - 120 - 360 - 180 - 240)
        y = 390
    else:
        # Go back to the origin
        x = 0
        y = 90
    return (x,y)

if __name__ == "__main__":
    for t in range(1620):
        if pp(t) != parameterized_path(t):
            print(f"pp({t}) = {pp(t)}    parameterized_path({t}) = {parameterized_path(t)}")