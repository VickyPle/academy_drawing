from p5 import *

window_height = 640
window_width = 360

#Star_myStar1:
#Star_myStar2:

def my_setup():
    size(window_width, window_height)
    no_stroke()
    fill(255, 255, 0)

def my_draw():
    background(20)
    y = window_height * 0.5
    #line((0, y), (window_width, y))
    #circle(window_width*0.5, window_height*0.5, 100)
    #circle(window_width*0.2, window_height*0.2, 50)
    scale(0.5)
    my_star1 = (triangle((0,426), (180,106), (window_width, 426)), triangle((0,212), (180,534), (window_width, 212)))
    scale(.25)
    my_star2 = (triangle((0,426), (180,106), (window_width, 426)), triangle((0,212), (180,534), (window_width, 212)))
    scale(9)
    my_star3 = (triangle((0,426), (180,106), (window_width, 426)), triangle((0,212), (180,534), (window_width, 212)))

        
    
    

if __name__ == '__main__':
    run(sketch_setup=my_setup, sketch_draw=my_draw)
