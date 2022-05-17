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

        listframe = ListFrame(mainframe, self.redis)
        listframe.pack(side='right')

class ListFrame(ttk.Frame):
    def __init__(self, parent, redis):
        super().__init__(parent)

        self.treeview = ttk.Treeview(self, height=40, show='tree')
        self.treeview.tag_configure('unlocked', background='green', foreground='white')
        self.treeview.pack(side='left')

        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.treeview.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.treeview.configure(yscrollcommand=self.scrollbar.set)

        self.weapon_list = []

        for id in redis.smembers('weapon_ids'):
            name = redis.hget('skin:%s' %(int(id)), 'name')
            tag  = 'unlocked' if redis.sismember('unlocked_skin_ids', id) else 'locked'
            self.weapon_list.append({ 'name': name, 'tag': tag })

        self.weapon_list.sort(key=self.by_name)

        for skin in self.weapon_list:
            self.treeview.insert('', 'end', text=skin['name'], tags=skin['tag'])

    def by_name(self, item):
        return item['name']

root  = Tk()
root.title('Guild Wars 2 Dashboard')
dashboard = Dashboard(root)
root.mainloop()
