import arcade
import Animation
import  Suns
import time

from Constant import CELL_WIDTH, SCREEN_WIDTH


class Plant(Animation.Animation):
    def __init__(self,image,hp,price,window):
        super().__init__(image,scale=0.12)
        self.window=window
        self.hp=hp
        self.price=price
        self.row=0
        self.col=0
        self.timer=0
    def update(self):

        if self.hp<=0:
            self.window.lawns.remove((self.row,self.col))
            self.kill()
    def planting(self,x,y,row,col):
        self.set_position(x,y)
        self.row=row
        self.col=col

class Sunflower(Plant):
    def __init__(self,window):
        super().__init__("Pictures/plants/sun1.png",50,50,window)
        self.append_texture(arcade.load_texture("Pictures/plants/sun1.png"))
        self.append_texture(arcade.load_texture("Pictures/plants/sun2.png"))
        self.window=window

        self.timer+=time.time()
    def update(self):
        super().update()


        if time.time()-self.timer> 15:


            sun = Suns.Sun(self.center_x+30, self.center_y - 30)
            self.window.suns_list.append(sun)
            self.timer=time.time()
        self.window.suns_list.update()
class Peashooter(Plant):
    def __init__(self,window):
        super().__init__("Pictures/plants/pea1.png",75,100,window)
        for i in range(1,4):
            self.append_texture(arcade.load_texture(f"Pictures/plants/pea{i}.png"))
        self.window=window
        self.timer=time.time()
    def update(self):
        super().update()
        zombie_on_line=False
        for zombie in self.window.zombies_list:
            if zombie.row == self.row :
                zombie_on_line = True
                break
        if time.time()-self.timer> 2 and zombie_on_line:
            new_bullet = Bullet(self.right,self.top-10,self.window)
            self.window.bullets_list.append(new_bullet)
            self.timer=time.time()

class Bullet(arcade.Sprite):
    def __init__(self,center_x,center_y,window):
        super().__init__("Pictures/items/bul.png",0.12)

        self.set_position(center_x,center_y)
        self.change_x=7
        self.damege=1
        self.window=window
    def update(self):
        self.center_x+=self.change_x
        if self.center_x>SCREEN_WIDTH:
            self.kill()
        zombies=arcade.check_for_collision_with_list(self,self.window.zombies_list)
        for zombie in zombies:
            zombie.hp-=self.damege
            self.kill()
class Nut(Plant):
    def __init__(self,window):
        super().__init__("Pictures/plants/nut1.png" ,200,50,window)
        for i in range(1,4):
            self.append_texture(arcade.load_texture(f"Pictures/plants/nut{i}.png"))
        self.window=window






















