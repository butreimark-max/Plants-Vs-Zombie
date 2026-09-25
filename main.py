from arcade import SpriteList
from arcade.examples.nested_loops_bottom_left_triangle import column
import Zombies
import Plants
import arcade
import time
import random
from arcade.gui.examples.anchor_widgets import window

from Constant import *
import Animation
def lawn_x(x):
    right_x=250+CELL_WIDTH
    column=1
    while right_x<=x :
        right_x=right_x+CELL_WIDTH
        column+=1
    center_x=right_x-CELL_WIDTH/2
    return center_x, column
def lawn_y(y):
    top_y=25+CELL_HEIGHT
    row=1
    while top_y<=y :
        top_y=top_y+CELL_HEIGHT
        row+=1
    center_y=top_y-CELL_HEIGHT/2
    return center_y, row
class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width,height,title)
        """Background image"""
        self.bg_picture=arcade.load_texture("Pictures/textures/background.jpg")
        self.menu_picture=arcade.load_texture("Pictures/textures/menu_vertical.png")
        self.plants_sound=arcade.load_sound("Sounds/seed.mp3")

        self.seed=None
        self.zombies_list=SpriteList()
        self.plants=SpriteList()
        self.suns_list=SpriteList()
        self.bullets_list=SpriteList()
        self.lawns=[]
        self.suns=150
        self.zombie_timer=time.time()
        self.setup()
    def setup(self):
        pass
    def on_draw(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,self.bg_picture)
        arcade.draw_texture_rectangle(67,SCREEN_HEIGHT/2,134,SCREEN_HEIGHT,self.menu_picture)
        arcade.draw_text(f"{self.suns}",30,490,(0,0,0),30)
        self.plants.draw()
        self.suns_list.draw()
        self.zombies_list.draw()
        self.bullets_list.draw()

        if self.seed != None:
            self.seed.draw()



    def update(self, delta_time):
        self.plants.update()
        self.zombies_list.update()
        self.plants.update_animation(delta_time)
        self.bullets_list.update()
        self.zombies_list.update_animation(delta_time)
        for plant in self.plants:
            if isinstance(plant, Plants.Sunflower):
                plant.update()
        if time.time() - self.zombie_timer > 3:
            center_y,row=lawn_y(random.randint(25,520))
            self.zombies_list.append(Zombies.Ordinare_Zombie(center_y,row))
            self.zombie_timer=time.time()
    def on_mouse_press(self, x, y, button, key_modifiers):
        print(x,y)
        if 16<=x<=111:
            if 375<=y<=475:
                print("sunflower")
                self.seed=Plants.Sunflower(self)

            if 263<=y<=363:
                print("peashooter")
                self.seed=Plants.Peashooter(self)
            if 146<=y<=246:
                print("wallnut")
            if 31<=y<=132:
                print("torch tree")
        if self.seed!=None:
            self.seed.set_position(x,y)
            self.seed.alpha=150
        for sun in self.suns_list:
            if  sun.left<=x<=sun.right and sun.bottom<=y<=sun.top:
                self.suns+=sun.value
                sun.kill()




    def on_mouse_motion(self, x: int, y: int, dx: int, dy: int):
        if self.seed != None:
            self.seed.set_position(x, y)
            self.seed.alpha = 150
    def on_mouse_release(self, x, y, button, key_modifiers):
        if 25<=y<=520 and 250<=x<=950 and self.seed != None :
            self.seed.alpha =255
            center_x,column=lawn_x(x)
            center_y,row=lawn_y(y)

            if (row,column) in self.lawns or self.suns<self.seed.price:

                self.seed=None
                return
            self.suns-=self.seed.price

            self.seed.planting(center_x,center_y,row,column)
            self.lawns.append((row,column))
            self.plants.append(self.seed)
            self.seed=None
            arcade.play_sound(self.plants_sound,0.2)
        else:
            self.seed=None








window_1=MyGame(SCREEN_WIDTH,SCREEN_HEIGHT,SCREEN_TILE)
arcade.run()










