# Support utility for getting coords from png picture and write them to file

import tkinter, os

def file_path(file_name):
    base_folder = os.path.dirname(__file__)
    return os.path.join(base_folder, file_name)

img_file_name = file_path("polar-bear.png")
coords_file_name = file_path("polar-bear.txt")
zoom = 2

def on_canvas_click(event):
    subor = open(coords_file_name, "a" if os.path.exists(coords_file_name) else "w")
    print(f"({event.x},{event.y}),", end=" ", file=subor)
    subor.close()

tk_root = tkinter.Tk()

img = tkinter.PhotoImage(file=img_file_name)
img = img.zoom(zoom, zoom)
w, h = img.width(), img.height()   

canvas = tkinter.Canvas(tk_root, width=w, height=h, bg='blue', highlightthickness=0)
canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)
canvas.create_image(0, 0, image=img, anchor=tkinter.NW)

canvas.update()

canvas.bind("<Button-1>", on_canvas_click)

tk_root.mainloop()
