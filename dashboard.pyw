import redis
from tkinter import *
from tkinter import ttk

root = Tk()
root.state('zoomed')
root.title('Guild Wars 2 Dashboard')

frame = ttk.Frame(root)
frame.pack(fill='both', padx=(20), pady=(20))

red  = redis.Redis()
ids  = list(map(int, red.smembers('skin_ids')))
tree = ttk.Treeview(frame, height=red.scard('skin_ids'))
tree.pack(fill='both')

for id in red.smembers('skin_ids'):
    name = red.hget('skin:%s' %(int(id)), 'name')
    tree.insert('', 'end', text=name)

root.mainloop()
