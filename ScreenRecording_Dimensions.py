from pynput.mouse import Events as MousEvents

def ScreenRegionSelect():
    print('Choose Region')
    while True:
        with MousEvents() as event:
            answer = event.get()
            if hasattr(answer, 'pressed'):
                if answer.pressed == True:
                    xy = []
                    print(answer)
                    x = answer.x
                    y = answer.y
                    xy.append((x, y))
                if answer.pressed == False:
                    print(answer)
                    x = answer.x
                    y = answer.y
                    xy.append((x, y))
                    break
    xy.sort(key=lambda tup: tup[1])
    x1 = xy[0][0]
    y1 = xy[0][1]
    x2 = xy[1][0]
    y2 = xy[1][1]
    return x1, y1, x2, y2