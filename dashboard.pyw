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
weapon_tree.tag_configure('unlocked', background='green', foreground='white')
heavy_tree.grid(column=1, row=0, sticky=(W, E))
heavy_tree.tag_configure('unlocked', background='green', foreground='white')
medium_tree.grid(column=2, row=0, sticky=(W, E))
medium_tree.tag_configure('unlocked', background='green', foreground='white')
light_tree.grid(column=3, row=0, sticky=(W, E))
light_tree.tag_configure('unlocked', background='green', foreground='white')

def by_name(item):
    return item['name']

weapon_list = []
heavy_list  = []
medium_list = []
light_list  = []

for id in red.smembers('weapon_ids'):
    name = red.hget('skin:%s' %(int(id)), 'name')
    tag  = 'unlocked' if red.sismember('unlocked_skin_ids', id) else 'locked'
    weapon_list.append({ 'name': name, 'tag': tag })
for id in red.smembers('heavy_armor_ids'):
    name = red.hget('skin:%s' %(int(id)), 'name')
    tag  = 'unlocked' if red.sismember('unlocked_skin_ids', id) else 'locked'
    heavy_list.append({ 'name': name, 'tag': tag })
for id in red.smembers('medium_armor_ids'):
    name = red.hget('skin:%s' %(int(id)), 'name')
    tag  = 'unlocked' if red.sismember('unlocked_skin_ids', id) else 'locked'
    medium_list.append({ 'name': name, 'tag': tag })
for id in red.smembers('light_armor_ids'):
    name = red.hget('skin:%s' %(int(id)), 'name')
    tag  = 'unlocked' if red.sismember('unlocked_skin_ids', id) else 'locked'
    light_list.append({ 'name': name, 'tag': tag })

weapon_list.sort(key=by_name)
heavy_list.sort(key=by_name)
medium_list.sort(key=by_name)
light_list.sort(key=by_name)

for skin in weapon_list:
    weapon_tree.insert('', 'end', text=skin['name'], tags=skin['tag'])
for skin in heavy_list:
    heavy_tree.insert('', 'end', text=skin['name'], tags=skin['tag'])
for skin in medium_list:
    medium_tree.insert('', 'end', text=skin['name'], tags=skin['tag'])
for skin in light_list:
    light_tree.insert('', 'end', text=skin['name'], tags=skin['tag'])

root.mainloop()
