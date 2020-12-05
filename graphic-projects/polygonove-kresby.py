import tkinter


def priprav_body(points, width, height, margin):
    """pripravi nove body s upravenymi suradnicami tak, aby co najlepsie vyuzili dane platno"""
    min_x = max_x = points[0][0]
    min_y = max_y = points[0][1]
    for bod in points:
        min_x = min(bod[0], min_x)
        min_y = min(bod[1], min_y)
        max_x = max(bod[0], max_x)
        max_y = max(bod[1], max_y)

    pomer = min((width - 2 * margin) / (max_x - min_x), (height - 2 * margin) / (max_y - min_y))
    stred_platna = (width / 2, height / 2)
    stred_kresby = ((max_x + min_x) / 2, (max_y + min_y) / 2)

    body = []
    for bod in points:
        x = stred_platna[0] - (stred_kresby[0] - bod[0]) * pomer
        y = stred_platna[1] - (stred_kresby[1] - bod[1]) * pomer
        body.append((x, y))
        # print(bod[0], bod[1], '-->', x, y)
    return body

def kresli(cnv, drawing, margin=50, is_coords=False, is_indices=False):
    """vhodne umiestni a vykresli dane polygony na platno"""
    points, polygons, outline = drawing['body'], drawing['polygony'], drawing['obrys']  
    nove_body = priprav_body(points, cnv.winfo_width(), cnv.winfo_height(), margin)
    for polygon in polygons:
        farba, vrcholy_polygonu = polygon
        suradnice = ()
        for vrchol in vrcholy_polygonu:
            suradnice += nove_body[vrchol]
        canvas.create_polygon(suradnice, fill=farba, outline=outline[0], width=outline[1])
    if is_coords:
        for bod in nove_body:
            canvas.create_text(bod, text=f'{bod[0]:.1f},{bod[1]:.1f}')
    if is_indices:
        for idx in range(len(nove_body)):
            canvas.create_text(nove_body[idx], text=f'{idx}')
    

obrazec = {
    'body': [(10,20), (40,100), (150,130), (160,10)],
    'polygony': [
        ("red", (0,1,2)),
        ("gold", (2,3,0))
    ],
    'obrys': ('white', 15)
}

def canvas_vykresli():
    kresli(canvas, obrazec, is_indices=True, margin=60)

def on_canvas_resize(event):
    event.widget.delete('all')
    event.widget.vykresli()


canvas = tkinter.Canvas() #width=720, height=500, bg='grey')
canvas.pack(fill="both", expand=True)
canvas.update()

canvas.vykresli = canvas_vykresli
canvas.bind('<Configure>', on_canvas_resize)


canvas.vykresli()



canvas.mainloop()

