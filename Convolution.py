import pygame as pg
import numpy as np
import sys

############################ Definitions #############################################################
def importimg():

    #loading image
    img = pg.image.load('C:/Users/alexa/Documents/AE 1/Python/Colleges jaar 1/Assignment 5/assignment6_data/beach_holiday.jpg')
    width = img.get_width()
    height = img.get_height()
    reso  = (width, height)
    screen = pg.display.set_mode(reso)
    screen.blit(img, (0,0))
    pg.display.flip()
    #accessing sub-arrays
    pg.surfarray.use_arraytype("numpy")
    screenpix = pg.surfarray.pixels3d(img) #pixels in array

    return screenpix, width, height

def importfilt():
    #importing desired filter
    filename = input("Enter the name of the filter you want to use: ")
    file = np.genfromtxt("C:/Users/alexa/Documents/AE 1/Python/Colleges jaar 1/Assignment 5/assignment6_data/"+filename+".txt")

    filt = np.zeros
    with open(file, "r", encoding="utf-8", errors="ignore") as reader:
        lines = reader.readlines()
        shape = len(lines)
        
        filt = np.zeros((shape,shape), dtype=float, order="C") #array of all zeros in shape of image
        for index1, row in enumerate(lines):
            for index2, item in enumerate(row.split()):
                filt[index1, index2] = float(item)

        


    return 


############################ MAIN PROGRAM ##########################################################################
pg.init()

#width = importimg()[1]
#height = importimg()[2]

#sizeInput = (width, height)

#new_size = (sizeInput[0] - 2, sizeInput[1] - 2)

#for i in range(new_size[0]):
 #   for i in range(new_size[1]):

importimg()
importfilt()


running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        
    pg.display.update()
pg.quit()


# step 2: load the filters
    # numpy.genfromtxt(filename)

# step 3: 
    # size output picture = size input picture - 2 pixels on both sides  (this is with 3 x 3 matrix)

# step 4: nested loop
    # for i in range(new width):
        #for j in ramge(new height)

# step 5:  .flip()