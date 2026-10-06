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

player =FirstPersonController(position=(8,1,2)) 

def input(key):
    alvo = mouse.hovered_entity
    if not alvo:
        return
    if key == 'right mouse down':
        Entity(model='cube', color=color.gray,
               texture='while_cube',
               position=alvo.position + mouse.normal,
               collider='box')
    app.run()    
