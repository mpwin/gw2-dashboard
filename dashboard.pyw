import redis
from tkinter import *
from tkinter import ttk

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

red = redis.Redis()
ids = list(map(int, red.smembers('skin_ids')))

tree1 = ttk.Treeview(frame, height=red.scard('skin_ids'))
tree1.grid(column=0, row=0, sticky=(W, E))
tree2 = ttk.Treeview(frame, height=red.scard('skin_ids'))
tree2.grid(column=1, row=0, sticky=(W, E))
tree3 = ttk.Treeview(frame, height=red.scard('skin_ids'))
tree3.grid(column=2, row=0, sticky=(W, E))
tree4 = ttk.Treeview(frame, height=red.scard('skin_ids'))
tree4.grid(column=3, row=0, sticky=(W, E))

for id in red.smembers('skin_ids'):
    name = red.hget('skin:%s' %(int(id)), 'name')
    tree1.insert('', 'end', text=name)
    tree2.insert('', 'end', text=name)
    tree3.insert('', 'end', text=name)
    tree4.insert('', 'end', text=name)

root.mainloop()
