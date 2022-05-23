import data
import tkinter as tk
from tkinter import ttk

class Dashboard:
    def __init__(self, root):
        mainframe = ttk.Frame(root, padding=20)
        mainframe.pack()

        nav = ttk.Frame(mainframe, padding=(0, 0, 10, 0))
        nav.pack(side='left', fill='both')

        collection_btn = ttk.Button(nav, text='Collection', command=lambda: self.show_frame(self.frames['collection']))
        standalone_btn = ttk.Button(nav, text='Standalone', command=lambda: self.show_frame(self.frames['standalone']))
        collection_btn.pack(side='top')
        standalone_btn.pack(side='top')

        self.frames = dict(
            collection = CollectionFrame(mainframe),
            standalone = StandaloneFrame(mainframe)
        )

        self.current_frame = self.frames['collection']
        self.current_frame.pack(side='left')

    def show_frame(self, frame):
        self.current_frame.pack_forget()
        self.current_frame = frame
        self.current_frame.pack(side='left')

class CollectionFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.treeview = ttk.Treeview(self, height=40, show='tree')
        self.treeview.pack(side='left')

        for i in range(40):
            self.treeview.insert('', 'end', text=i+1)

class StandaloneFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        weapon_frame       = ListFrame(self, data.weapon_list())
        heavy_armor_frame  = ListFrame(self, data.heavy_armor_list())
        medium_armor_frame = ListFrame(self, data.medium_armor_list())
        light_armor_frame  = ListFrame(self, data.light_armor_list())

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

root = tk.Tk()
root.title('Guild Wars 2 Dashboard')
dashboard = Dashboard(root)
root.mainloop()
