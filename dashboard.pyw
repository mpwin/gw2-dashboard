import redis
from tkinter import *
from tkinter import ttk

red  = redis.Redis()
root = Tk()
root.state('zoomed')
root.title('Guild Wars 2 Dashboard')

frame = ttk.Frame(root, padding=20)
frame.pack(fill='both')
frame.rowconfigure(0, weight=1)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)

weapon_tree = ttk.Treeview(frame, height=red.scard('weapon_ids'))
heavy_tree  = ttk.Treeview(frame, height=red.scard('heavy_armor_ids'))
medium_tree = ttk.Treeview(frame, height=red.scard('medium_armor_ids'))
light_tree  = ttk.Treeview(frame, height=red.scard('light_armor_ids'))

weapon_tree.grid(column=0, row=0, sticky=(W, E))
heavy_tree.grid(column=1, row=0, sticky=(W, E))
medium_tree.grid(column=2, row=0, sticky=(W, E))
light_tree.grid(column=3, row=0, sticky=(W, E))

for id in red.smembers('weapon_ids'):
    name = red.hget('skin:%s' %(int(id)), 'name')
    weapon_tree.insert('', 'end', text=name)
for id in red.smembers('heavy_armor_ids'):
    name = red.hget('skin:%s' %(int(id)), 'name')
    heavy_tree.insert('', 'end', text=name)
for id in red.smembers('medium_armor_ids'):
    name = red.hget('skin:%s' %(int(id)), 'name')
    medium_tree.insert('', 'end', text=name)
for id in red.smembers('light_armor_ids'):
    name = red.hget('skin:%s' %(int(id)), 'name')
    light_tree.insert('', 'end', text=name)

root.mainloop()
