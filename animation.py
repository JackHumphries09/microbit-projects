import microbit as m

def open():
    m.display.clear()
    m.sleep(100)
    m.display.set_pixel(0,0,9)
    m.sleep(100)
    m.display.set_pixel(1,0,9)
    m.sleep(100)
    m.display.set_pixel(0,1,9)
    m.sleep(100)
    m.display.set_pixel(2,0,9)
    m.sleep(100)
    m.display.set_pixel(1,1,9)
    m.sleep(100)
    m.display.set_pixel(0,2,9)
    m.sleep(100)
    m.display.set_pixel(0,3,9)

    
while True:
    if m.button_b.was_pressed():
       m.display.clear()
    elif m.button_a.was_pressed():
        open()      
