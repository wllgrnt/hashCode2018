def getDistance(start, finish):
    """Given a start (x,y) and finish (a,b), return the distance."""
    x, y = start
    a, b = finish
    return abs(int(x) - int(a)) + abs(int(y) - int(b))
