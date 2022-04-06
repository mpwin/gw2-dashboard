from tkinter import *
from tkinter import ttk

root = Tk()
root.state('zoomed')
root.title('Guild Wars 2 Dashboard')

frame = ttk.Frame(root)
frame.pack(fill='both', padx=(20), pady=(20))

tree = ttk.Treeview(frame, height=40)
for item in range(40):
    tree.insert('', 'end', text=f'Item {item + 1}')
tree.pack(fill='both')

root.mainloop()
