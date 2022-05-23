import data
from tkinter import *
from tkinter import ttk

class Dashboard:
    def __init__(self, root):
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

        weapon_frame       = ListFrame(mainframe, data.weapon_list())
        heavy_armor_frame  = ListFrame(mainframe, data.heavy_armor_list())
        medium_armor_frame = ListFrame(mainframe, data.medium_armor_list())
        light_armor_frame  = ListFrame(mainframe, data.light_armor_list())

        weapon_frame.pack(side='left')
        heavy_armor_frame.pack(side='left')
        medium_armor_frame.pack(side='left')
        light_armor_frame.pack(side='left')

class ListFrame(ttk.Frame):
    def __init__(self, parent, list):
        super().__init__(parent)

        self.treeview = ttk.Treeview(self, height=40, show='tree')
        self.treeview.tag_configure('unlocked', background='green', foreground='white')
        self.treeview.pack(side='left')

        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.treeview.yview)
        self.scrollbar.pack(side='right', fill='y')
        self.treeview.configure(yscrollcommand=self.scrollbar.set)

        for item in list:
            self.treeview.insert('', 'end', text=item['name'], tags=item['tag'])

root  = Tk()
root.title('Guild Wars 2 Dashboard')
dashboard = Dashboard(root)
root.mainloop()
