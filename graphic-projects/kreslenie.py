import tkinter

def kresli(cnv, x, y, sirka=200, stat='a'):
    vyska = sirka / 3 * 2
    cnv.create_rectangle(x - sirka/2, y - vyska/2, x + sirka/2, y + vyska/2, 
            fill='silver', outline='black', width=1)
    cnv.create_text(x, y, text=stat, font=f'arial {int(sirka // 3)}')


cnv_width = 720
cnv_height = 500
canvas = tkinter.Canvas(width=cnv_width, height=cnv_height)
canvas.pack()

#tapeta
staty = ['ab', 'cd', 'ef', 'gh', 'ij']
idx = 0
okraj = 10
min_sirka_dlazdicky = 100
min_vyska_dlazdicky = int(min_sirka_dlazdicky / 3 * 2)
x_pocet = (cnv_width - 2 * okraj) // min_sirka_dlazdicky
y_pocet = (cnv_height - 2 * okraj) // min_vyska_dlazdicky
for iy in range(y_pocet):
    y = okraj + (iy + 0.5) * (cnv_height - 2 * okraj) / y_pocet
    for ix in range(x_pocet):
        x = okraj + (ix + 0.5) * (cnv_width - 2 * okraj) / x_pocet
        kresli(canvas, x, y, min_sirka_dlazdicky * 0.75, stat=staty[idx % len(staty)])
        idx += 1




canvas.mainloop()