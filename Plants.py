import arcade
import Animation
class Plant(Animation.Animation):
    def __init__(self,image,hp,price):
        super().__init__(image,scale=0.12)
        self.hp=hp
        self.price=price
        self.row=0
        self.col=0
    def update(self):
        if self.hp<=0:
            self.kill()
    def planting(self,x,y,row,col):
        self.set_position(x,y)
        self.row=row
        self.col=col

class Sunflower(Plant):
    def __init__(self):
        super().__init__("Pictures/plants/sun1.png",50,50)
        self.append_texture(arcade.load_texture("Pictures/plants/sun1.png"))
        self.append_texture(arcade.load_texture("Pictures/plants/sun2.png"))




