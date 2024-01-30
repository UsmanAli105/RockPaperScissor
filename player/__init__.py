import math
import pygame
import random
from settings import *

from abc import ABC, abstractmethod

class coords:
    def __init__(self) -> None:
        self.x = random.randint(100, WIDTH - 100)
        self.y = random.randint(100, HEIGHT - 100)

    def get_coords(self):
        return (self.x, self.y)
    
class direction:
    def __init__(self) -> None:
        dirs = ['left', 'right', 'up', 'down']
        indice = random.randint(0, len(dirs) - 1)
        self.dir = dirs[indice]
    
    def get_random_direction(self):
        return self.dir

    def get_direction_for_destinaion(self, curr: coords, dest: coords):
        if dest.x < curr.x:
            return 'left'
        if dest.x > curr.x:
            return 'right'
        if dest.y < curr.y:
            return 'up'
        if dest.y > curr.y:
            return 'down'

class player_object(ABC):
    def __init__(self, player_type) -> None:
        super().__init__()
        self.player_type = player_type
        self.player_path = './imgs/' + self.player_type + '.png'
        self.player = pygame.transform.scale(pygame.image.load(self.player_path), (20, 20))
        self.coord = coords()
        self.dir = direction()
        self.destination = coords()
       
    def draw(self, win):
        win.blit(self.player, (self.coord.x, self.coord.y))
     
    def move(self):
        curr_dir = self.dir.get_direction_for_destinaion(self.coord, self.destination)        
        if curr_dir == 'left':
            self.coord.x -= 1
        if curr_dir == 'right':
            self.coord.x += 1
        if curr_dir == 'up':
            self.coord.y -= 1
        if curr_dir == 'down':
            self.coord.y += 1
        if curr_dir is None:
            self.destination = coords()
    
    def change_player(self, player_type):
        self.player_type = player_type
        self.player_path = './imgs/' + self.player_type + '.png'
        self.player = pygame.transform.scale(pygame.image.load(self.player_path), (20, 20))

    def get_next_destination(self):
        return coords()

        
def l2_norm(obj_1: player_object, obj_2: player_object):
    return round(math.sqrt((obj_1.coord.x - obj_2.coord.x)**2 + (obj_1.coord.y - obj_2.coord.y)**2), 2)


def kill(collision_matrix, players, opponent):
    for i in range(n_player):
        for j in range(n_player):
            if i != j and players[i].player_type != opponent and collision_matrix[i][j] < COLLISION_THRESHOLD:
                players[i].change_player(opponent)