
from math import sin, cos, sqrt, atan2, radians


def calculateDistance(lat1, lon1, lat2, lon2):
    R = 6373.0
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


print(calculateDistance(radians(52.2296756), radians(21.0122287), radians(52.406374), radians(16.9251681)))
