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
            'dye': DyeFrame(self),
            'mini': MiniFrame(self),
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
        self.dye_button = ttk.Button(
            self,
            text='Dyes',
            command=lambda: self.show_frame('dye'),
            ).pack(side='top')
        self.mini_button = ttk.Button(
            self,
            text='Minis',
            command=lambda: self.show_frame('mini'),
            ).pack(side='top')

    def show_frame(self, frame):
        self.dashboard.current_frame.pack_forget()
        self.dashboard.current_frame = self.dashboard.frames[frame]
        self.dashboard.current_frame.pack(side='right')


class CollectionFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.weapon = ListFrame(self, data.collections('weapon')).pack(side='left')
        self.heavy = ListFrame(self, data.collections('heavy')).pack(side='left')
        self.medium = ListFrame(self, data.collections('medium')).pack(side='left')
        self.light = ListFrame(self, data.collections('light')).pack(side='left')


class StandaloneFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.weapon = ListFrame(self, data.skins('weapon')).pack(side='left')
        self.heavy = ListFrame(self, data.skins('heavy')).pack(side='left')
        self.medium = ListFrame(self, data.skins('medium')).pack(side='left')
        self.light = ListFrame(self, data.skins('light')).pack(side='left')


class DyeFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.exclusive = ListFrame(self, data.dyes('exclusive')).pack(side='left')
        self.rare = ListFrame(self, data.dyes('rare')).pack(side='left')
        self.uncommon = ListFrame(self, data.dyes('uncommon')).pack(side='left')
        self.common = ListFrame(self, data.dyes('common')).pack(side='left')
        self.starter = ListFrame(self, data.dyes('starter')).pack(side='left')


class MiniFrame(ttk.Frame):

    def __init__(self, parent):
        super().__init__(parent)

        self.minis = ListFrame(self, data.minis()).pack(side='left')


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
            self.treeview.insert('', 'end', item['id'], text=item['name'], tags=item['tag'])
            for child in (item.get('children') or []):
                self.treeview.insert(item['id'], 'end', child['id'],
                                     text=child['name'], tags=child['tag'])


root = tk.Tk()
root.title('Guild Wars 2 Dashboard')
dashboard = Dashboard(root)
root.mainloop()
