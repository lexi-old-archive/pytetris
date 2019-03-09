import tile
import gameobject

class Block(gameobject.Gameobject):
    def __init__(self, blocktype, x=0, y=0, dx=0, dy=0, alive=True):
        super().__init__(dx, dy, alive)
        self.x = x
        self.y = y
        self.blocktype = blocktype
        self.tiles = []
        self.make_tiles()

    def make_tiles(self):
        if self.blocktype == 'o':
            # **
            # **
            #yellow
            red=235
            green=235
            blue=0
            self.tiles.append(tile.Tile(x=self.x, y=self.y, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+50, y=self.y, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+50, y=self.y+50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x, y=self.y+50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
        elif self.blocktype == 'i':
            # ****
            #lightblue
            red=150
            green=200
            blue=255
            self.tiles.append(tile.Tile(x=self.x, y=self.y, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+50, y=self.y, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+100, y=self.y, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+150, y=self.y, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
        elif self.blocktype == 'l':
            # ..*
            # ***
            #orange
            red=255
            green=150
            blue=0
            self.tiles.append(tile.Tile(x=self.x+100, y=self.y, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x, y=self.y+50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+50, y=self.y+50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+100, y=self.y+50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))

        elif self.blocktype == 'j':
            # *..
            # ***
            #darkblue
            red=70
            green=70
            blue=255
            self.tiles.append(tile.Tile(x=self.x, y=self.y, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x, y=self.y+50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+50, y=self.y+50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+100, y=self.y+50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
        elif self.blocktype == 's':
            # .**
            # **.
            #green
            red=0
            green=200
            blue=0
            self.tiles.append(tile.Tile(x=self.x+50, y=self.y, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+100, y=self.y, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x, y=self.y+50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+50, y=self.y+50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
        elif self.blocktype == 'z':
            # **.
            # .**
            #red
            red=235
            green=0
            blue=0
            self.tiles.append(tile.Tile(x=self.x, y=self.y, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+50, y=self.y, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+50, y=self.y+50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+100, y=self.y+50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
        elif self.blocktype == 't':
            # .*.
            # ***
            #red
            red=225
            green=0
            blue=255
            self.tiles.append(tile.Tile(x=self.x+50, y=self.y, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x, y=self.y+50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+50, y=self.y+50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))
            self.tiles.append(tile.Tile(x=self.x+100, y=self.y+50, w=50, h=50, r=red, g=green, b=blue, dx=0, dy=0, alive=True))


    def draw(self, surface):
        for tile in self.tiles:
            tile.draw(surface)
