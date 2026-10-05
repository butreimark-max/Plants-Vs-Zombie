import arcade
import Animation
import Constant
from Constant import SCREEN_WIDTH


class Zombie(Animation.Animation):
    def __init__(self,image,hp,row,center_y,window):
        super().__init__(image,0.8)
        self.hp=hp
        self.row=row
        self.set_position(SCREEN_WIDTH,center_y)
        self.change_x=0.2
        self.eating=False
        self.window=window
    def update(self):
        if not self.eating:
            self.center_x-=self.change_x
        self.eating=False
        food=arcade.check_for_collision_with_list(self,self.window.plants)
        for plant in food:
            if self.row==plant.row:
                self.eating=True
                plant.hp-=0.3



        if self.hp<=0:
            self.kill()

class Ordinare_Zombie(Zombie):
    def __init__(self,row,center_y,window):
        super().__init__("Pictures/zombies/OrdinaryZombie/Zombie_0.png",10,row,center_y,window)
        for i in range(22):
            self.append_texture(arcade.load_texture(f"Pictures/zombies/OrdinaryZombie/Zombie_{i}.png"))
class Conehead_Zombie(Zombie):
    def __init__(self,row,center_y,window):
        super().__init__("Pictures/zombies/ConeheadZombie/ConeheadZombie_0.png",20,row,center_y,window)
        for i in range(21):
            self.append_texture(arcade.load_texture(f"Pictures/zombies/ConeheadZombie/ConeheadZombie_{i}.png"))
class Backethead_Zombie(Zombie):
    def __init__(self,row,center_y,window):
        super().__init__("Pictures/zombies/BucketheadZombie/BucketheadZombie_0.png",30,row,center_y,window)
        for i in range(15):
            self.append_texture(arcade.load_texture(f"Pictures/zombies/BucketheadZombie/BucketheadZombie_{i}.png"))


