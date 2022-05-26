import data
import tkinter as tk
from tkinter import ttk


class Dashboard(ttk.Frame):

    def __init__(self, root):
        super().__init__(root, padding=20)

        self.nav = Nav(self)
        self.frames = {
            'collection': CollectionFrame(self),
            'standalone': StandaloneFrame(self),
            }
        self.current_frame = self.frames['collection']

        self.pack()
        self.nav.pack(side='left', fill='y')
        self.current_frame.pack(side='right')


class Nav(ttk.Frame):

    def __init__(self, dashboard):
        super().__init__(dashboard, padding=(0, 0, 10, 0))

        self.dashboard = dashboard

        self.collection_button = ttk.Button(
            self,
            text='Collection',
            command=lambda: self.show_frame('collection'),
            ).pack(side='top')
        self.standalone_button = ttk.Button(
            self,
            text='Standalone',
            command=lambda: self.show_frame('standalone'),
            ).pack(side='top')

    def show_frame(self, frame):
        self.dashboard.current_frame.pack_forget()
        self.dashboard.current_frame = self.dashboard.frames[frame]
        self.dashboard.current_frame.pack(side='right')


class CollectionFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.weapon = ListFrame(self, data.weapon_collection_list()).pack(side='left')


class StandaloneFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.weapon_frame = ListFrame(self, data.weapon_list()).pack(side='left')
        self.heavy_armor_frame = ListFrame(self, data.heavy_armor_list()).pack(side='left')
        self.medium_armor_frame = ListFrame(self, data.medium_armor_list()).pack(side='left')
        self.light_armor_frame = ListFrame(self, data.light_armor_list()).pack(side='left')


class ListFrame(ttk.Frame):

    def __init__(self, parent, items):
        super().__init__(parent)

        self.treeview = ttk.Treeview(self, height=40, show='tree')
        self.scrollbar = ttk.Scrollbar(self, orient='vertical', command=self.treeview.yview)

        self.treeview.configure(yscrollcommand=self.scrollbar.set)
        self.treeview.tag_configure('unlocked', background='green', foreground='white')

        self.treeview.pack(side='left')
        self.scrollbar.pack(side='right', fill='y')

        for item in items:
            self.treeview.insert('', 'end', text=item['name'], tags=item['tag'])


root = tk.Tk()
root.title('Guild Wars 2 Dashboard')
dashboard = Dashboard(root)
root.mainloop()
