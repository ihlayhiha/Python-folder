class Player(object):

    def __init__(self, name) -> None:
        self.name = name
        self._lives = 3
        self._level = 1
        self._score = 0

    def _get_lives(self):       # getter for lives
        return self._lives
    
    def _set_lives(self, lives):    # setter for lives
        if lives >= 0:
            self._lives = lives
        else:
            print("Lives cannot be negative")
            self._lives = 0

    def _get_level(self):       # getter for level
        return self._level

    def _set_level(self, level):    # setter for level
        if level > 0:
            self._score += ((level - self._level) * 1000)
            self._level = level
        else:
            print("Cannot go beneath Level: 1")

    lives = property(_get_lives, _set_lives)   
    level = property(_get_level, _set_level)   

    @property
    def score(self):
        return self._score
    
    @score.setter
    def score(self, score):
        self._score = score
    
    def __str__(self) -> str:
        return "Name: {0.name}, Lives: {0._lives}, Level: {0.level}, Score: {0.score}".format(self)
