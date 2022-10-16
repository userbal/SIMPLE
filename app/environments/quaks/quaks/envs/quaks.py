from importlib.metadata import metadata
import gym
import numpy as np

import config


class Player():
    def __init__(self, id, bag, pot):
        self.id = id
        self.bag = bag
        self.pot = pot


class Bag():
    def __init__(self, chips):
        self.chips = chips


class Chip():
    def __init__(self, color, value, action, when):
        self.color = color
        self.value = value
        self.action = action
        self.when = when


class Pot():
    def __init__(self):
        self.locations = []
        self.totalWhite = 0
        self.ingredients = []
        self.position = 0


class QuaksEnv(gym.env):
    metadata = {'render.modes': ['human]']}

    def __init__(self, verbose=False, manual=False):
        super(QuaksEnv, self).__init__()
        self.name = 'quaks'
        self.manual = manual

        self.scoreBoard = []
        self.n_players = 4
        self.verbose = verbose

    @property
    def observation(self):
        
