import redis
from tkinter import *
from tkinter import ttk

class Dashboard:
    def __init__(self, root):
        self.redis = redis.Redis()

        mainframe = ttk.Frame(root, padding=20)
        mainframe.pack()

        nav = ttk.Frame(mainframe, padding=(0, 0, 10, 0))
        nav.pack(side='left', fill='both')

        collection_btn = ttk.Button(nav, text='Collection')
        standalone_btn = ttk.Button(nav, text='Standalone')
        weapon_btn     = ttk.Button(nav, text='Weapon')
        heavy_btn      = ttk.Button(nav, text='Heavy')
        medium_btn     = ttk.Button(nav, text='Medium')
        light_btn      = ttk.Button(nav, text='Light')

        collection_btn.pack(side='top')
        standalone_btn.pack(side='top')
        weapon_btn.pack(side='top')
        heavy_btn.pack(side='top')
        medium_btn.pack(side='top')
        light_btn.pack(side='top')

        listframe = ttk.Frame(mainframe)
        listframe.pack(side='right')

        treeview = ttk.Treeview(listframe, height=40, show='tree')
        treeview.tag_configure('unlocked', background='green', foreground='white')
        treeview.pack(side='left')

        scrollbar = ttk.Scrollbar(listframe, orient='vertical', command=treeview.yview)
        scrollbar.pack(side='right', fill='y')
        treeview.configure(yscrollcommand=scrollbar.set)

        def by_name(item):
            return item['name']

        weapon_list = []

        for id in self.redis.smembers('weapon_ids'):
            name = self.redis.hget('skin:%s' %(int(id)), 'name')
            tag  = 'unlocked' if self.redis.sismember('unlocked_skin_ids', id) else 'locked'
            weapon_list.append({ 'name': name, 'tag': tag })

        weapon_list.sort(key=by_name)

        for skin in weapon_list:
            treeview.insert('', 'end', text=skin['name'], tags=skin['tag'])

root  = Tk()
root.title('Guild Wars 2 Dashboard')
dashboard = Dashboard(root)
root.mainloop()
