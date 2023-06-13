import math as m
# Use of offset_3Ddistance, the other functions are not used
# or were used in other files


def offset_distance(x1, y1, x2, y2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    return dist

def offset_3Ddistance(x1, x2, y1, y2, z1, z2):
    dist = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
    return dist

def findAngle(x1, y1, x2, y2, x3, y3):
    # Caculate the angle between the left shoulder and the left elbow using the cosine rule
    a = offset_distance(x1, y1, x3, y3)
    b = offset_distance(x1, y1, x2, y2)
    c = offset_distance(x2, y2, x3, y3)

    theta = m.atan2((y3 - y1), (x3 - x1)) - m.atan2((y2 - y1), (x2 - x1))
    degree = theta * int(180 / m.pi)  # + 90
    return round(degree, 2)


def findRotation(x1, y1, x2, y2):
    # Calculate the rotation of an arm
    theta = m.atan2((y2 - y1), (x2 - x1))
    degree = theta * int(180 / m.pi)
    return round(degree, 2)


def findTheta(member1_y, member1_z, member2_y, member2_z):
    lenght = offset_distance(member1_y, member1_z, member2_y, member2_z)
    theta = m.acos(lenght / member2_y)
    degree = theta * int(180 / m.pi)
    return round(degree, 2)