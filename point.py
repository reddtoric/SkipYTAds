class Point:
    """ Point class represents and manipulates x,y coords. """

    def __init__(self, x=None, y=None):
        """ Create a new point at the origin """
        self.x = x if x is not None else 0
        self.y = y if y is not None else 0
