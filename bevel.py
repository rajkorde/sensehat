from sense_hat import SenseHat

sense = SenseHat()

sensitivity = 30

def draw_pixel(p, r):
    if p == 4 and r == 4:
        color = [0, 255, 0]
    else:
        color = [255, 0, 0]

    sense.clear()
    sense.set_pixel(p, 7 - r, color)

def normalize_coord(c):
    if c > sensitivity and c < 180:
        c = sensitivity
    elif c > 180 and c < (360 - sensitivity):
        c = 360 - sensitivity
    c = (c + sensitivity) % 360
    if c > ((sensitivity * 2) - 1):
        c = (sensitivity * 2) - 1
    return int((c / (sensitivity * 2)) * 8)
    

while True:
    orientation = sense.get_orientation()
    pitch = orientation["pitch"]
    roll = orientation["roll"]

    #print("pitch={0}, roll={1}, yaw={2}".format(pitch,yaw,roll))

    p = normalize_coord(pitch)
    r = normalize_coord(roll)

    draw_pixel(p, r)
