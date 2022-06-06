class House:
    def __init__(self,paint_color,floor_material):
        self.paint_color=paint_color
        self.floor_material=floor_material
    def myhome(self):
            print("paint color is %s and floor material is %s" %(self.paint_color,self.floor_material))
suja_home=House("white","granite")
suja_home.myhome()
anu_home=House("blue","marble")
anu_home.myhome()
