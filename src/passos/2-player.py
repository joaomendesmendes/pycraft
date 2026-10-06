from ursina import *
from ursina.prefabs.first_person_controller \
     import FirstPersonController

app = Ursina()
Sky()

for x in range(18):
    for z in range(18):
        Entity(model='cube', color=color.lime,
               texture='white_cube',
               position=(x,0,z), collider='box')

player = FirstPersonController(position=(8,1,2))
app.run()        