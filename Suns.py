import arcade
class Sun (arcade.Sprite):
    def __init__(self,x,y):
        super().__init__("Pictures/items/sun.png",0.1)
        self.value=25
        self.center_x=x
        self.center_y=y
    def update(self):
        self.angle+=1