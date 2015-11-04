import random,pdb

class MovieFinder(object):
    def __init__(self):
        f = open('movie_ground.txt')
        self.lines = f.readlines()
        self.N = len(self.lines)
        f.close()

    def _readline(self, line):
        p = self.lines[line].split(' ')
        return int(p[0]), float(p[1])

    def get_movie_ground(self, movie_id):
        #binary search
        left = 0
        right = self.N
        while left <= right:
            i,ground = self._readline(int(left+right)/2)
            if i == movie_id: return ground
            if i < movie_id: left = i
            else: right = i
        return None

finder = MovieFinder()
print finder.get_movie_ground(5000)
