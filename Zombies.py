import arcade
import Animation
import Constant
from Constant import SCREEN_WIDTH


class Zombie(Animation.Animation):
    def __init__(self,image,hp,row,center_y):
        super().__init__(image,0.9)
        self.hp=hp
        self.row=row
        self.set_position(SCREEN_WIDTH,center_y)
        self.change_x=0.2
    def update(self):
        self.center_x=-self.change_x
        if self.hp<=0:
            self.kill()
class Ordinare_Zombie(Zombie):
    def __init__(self,row,center_y):
        super().__init__("Pictures/zombies/OrdinaryZombie/Zombie_0.png",10,row,center_y)
        for i in range(22):
            self.append_texture(arcade.load_texture(f"Pictures/zombies/OrdinaryZombie/Zombie_{i}.png"))
